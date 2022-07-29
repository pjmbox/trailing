#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 11:00
# @Author  : jiang.pan
# @Email   : jiang.pan@signify.com
# @File    : serial_tool.py
# ---------------------

import io
import os
import time
import binascii
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
                tmp = super(io.IOBase, self._uart_client).readline()
                ctx = self.get_received_line_context()
                ctx.line_raw = tmp
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


class SerialToolEx(SerialTool):

    def __init__(self, signal, name, port, baud, databit, paritybit, stopbit, hex_input, hex_output):
        super(SerialToolEx, self).__init__(signal, name, port, baud, databit, paritybit, stopbit)
        self.encoding = 'ascii'
        self.error_policy = 'ignore'
        self.serial_log_filename = 'log' + os.sep + '%s_%s.log' % (name, datetime.datetime.now().strftime('%Y%m%d'))
        self.hex_input = hex_input
        self.hex_output = hex_output
        self.serial_log_fd = None
        self.parsers = []

    @staticmethod
    def remove_sep(text):
        return text.replace('\r', '').replace('\n', '')

    def convert_to_io(self, ctx):
        if ctx.is_hex:
            ctx.line_raw = binascii.unhexlify(ctx.line_text)
        else:
            ctx.line_raw = ctx.line_text.encode(encoding=self.encoding, errors=self.error_policy)

    def convert_from_io(self, ctx):
        if ctx.is_hex:
            ctx.line_text = str(binascii.hexlify(ctx.line_raw), encoding=self.encoding)
        else:
            ctx.line_text = self.remove_sep(str(ctx.line_raw, encoding=self.encoding, errors=self.error_policy))

    def serial_logging(self, ctx):
        if not self._terminated:
            tmp = ctx.time_raw.strftime('%Y-%m-%d %H:%M:%S.%f')
            tmp = '%s %s %s\n' % (tmp, ctx.dir.value, ctx.line_text)
            self.serial_log_fd.write(tmp)
            self.serial_log_fd.flush()

    def gui_logging(self, ctx):
        if not self._terminated:
            self.signal.append_log(ctx)

    def parser_register(self, parser_func):
        self.parsers.append(parser_func)

    def parser_unregister(self, parser_func):
        tmp = []
        for parser in self.parsers:
            if parser != parser_func:
                tmp.append(parser)
        self.parsers = tmp

    def parser_clean(self):
        self.parsers = []

    def parser_handling(self, ctx):
        for parser in self.parsers:
            parser(ctx)

    def send(self, text):
        ctx = common.UpstreamLineContext()
        ctx.line_text = text
        ctx.is_hex = self.hex_output
        self.convert_to_io(ctx)
        super(SerialToolEx, self).send(ctx)
        self.serial_logging(ctx)
        self.gui_logging(ctx)

    def get_received_line_context(self):
        tmp = common.DownstreamLineContext()
        tmp.is_hex = self.hex_input
        return tmp

    def init_receive_handlers(self):
        self.register_last_line_handler(self.convert_from_io)
        self.register_last_line_handler(self.serial_logging)
        self.register_last_line_handler(self.parser_handling)
        self.register_last_line_handler(self.gui_logging)

    def un_init_receive_handlers(self):
        self.unregister_line_handler(self.gui_logging)
        self.unregister_line_handler(self.parser_handling)
        self.unregister_line_handler(self.serial_logging)
        self.unregister_line_handler(self.convert_from_io)

    def pre_loop(self):
        self.serial_log_fd = open(self.serial_log_filename, 'a')
        self.init_receive_handlers()
        super(SerialToolEx, self).pre_loop()

    def after_loop(self):
        super(SerialToolEx, self).after_loop()
        self.un_init_receive_handlers()
        self.serial_log_fd.close()
