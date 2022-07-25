#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 11:00
# @Author  : jiang.pan
# @Email   : jiang.pan@signify.com
# @File    : serial_tool.py
# ---------------------

import io
import time
import serial
import serial.tools.list_ports
import threading
import datetime
import logging
import common


class SerialTool:

    def __init__(self, signal, name, port, baud, databit, paritybit, stopbit):
        self.signal = signal
        self.name = name
        self.port = port
        self.baud = baud
        self.databit = databit
        self.paritybit = paritybit
        self.stopbit = stopbit
        self._terminated = None
        self._thread = None
        self._uart_client = None
        self.line_handlers = []
        self.err_count_max = 8
        self.last_send_time = datetime.datetime.now()
        self.last_read_time = datetime.datetime.now()

    def register_first_line_handler(self, handler_function):
        self.line_handlers.insert(0, handler_function)

    def register_last_line_handler(self, handler_function):
        self.line_handlers.append(handler_function)

    def unregister_line_handler(self, handler_function):
        tmp = []
        for handler in self.line_handlers:
            if handler != handler_function:
                tmp.append(handler)
        self.line_handlers = tmp

    def send(self, ctx):
        self._uart_client.write(ctx.line_raw)
        ctx.time_raw = datetime.datetime.now()
        self.last_read_time = ctx.time_raw

    @staticmethod
    def get_received_line_context():
        return common.LineContext()

    def pre_loop(self):
        self._uart_client = serial.Serial(port=self.port,
                                          baudrate=self.baud,
                                          bytesize=self.databit,
                                          parity=self.paritybit,
                                          stopbits=self.stopbit)
        self._uart_client.timeout = 30
        logging.info('[%s] uart open status is %s' % (self.name, self._uart_client.is_open))

    def after_loop(self):
        self._uart_client.close()
        self._uart_client = None

    def loop(self):
        try:
            self.pre_loop()
        except Exception as e:
            logging.error(e)
            self.signal.uart_is_stopped()
            self.signal.show_alert('Error', 'unexpected exceptions when open uart. %s' % e)
            return
        self.signal.uart_is_running()
        err = None
        err_count = self.err_count_max
        while not self._terminated:
            try:
                ctx = self.get_received_line_context()
                ctx.line_raw = super(io.IOBase, self._uart_client).readline()
                ctx.time_raw = datetime.datetime.now()
                self.last_read_time = ctx.time_raw
                for handler in self.line_handlers:
                    handler(ctx)
            except serial.SerialException as e:
                logging.error('[%s] [%d] uart thread: %s' % (self.name, err_count, e))
                logging.exception(e)
                err = e
            except PermissionError as e:
                logging.error('[%s] [%d] uart thread: %s' % (self.name, err_count, e))
                logging.exception(e)
                err = e
            except BaseException as e:
                logging.error('[%s] [%d] uart thread: %s' % (self.name, err_count, e))
                logging.exception(e)
                err = e
            finally:
                if err is not None:
                    err_count -= 1
                    if err_count <= 0:
                        logging.error('[%s] uart thread: too many exceptions (>%d)' % (self.name, self.err_count_max))
                        self._terminated = True
                        self.signal.show_alert('Error', 'too many exceptions in uart thread. %s' % err)
                    else:
                        time.sleep(3)
                    err = None
        self.signal.uart_is_stopped()
        try:
            self.after_loop()
        except Exception as e:
            logging.error(e)

    def start(self):
        if self._thread is None:
            self._terminated = False
            self._thread = threading.Thread(target=self.loop)
            self._thread.daemon = True
            self._thread.start()
        else:
            # shouldn't come here
            self.signal.uart_is_running()

    def stop(self):
        if self._thread is not None:
            self._terminated = True
            self._uart_client.cancel_read()
            self._thread = None
        else:
            # shouldn't come here
            self.signal.uart_is_stopped()
