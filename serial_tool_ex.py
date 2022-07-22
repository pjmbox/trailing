#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/18/2022 2:56 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : serial_tool_ex
# ---------------------
import datetime
import serial_tool
import binascii
import common
import os


class SerialToolEx(serial_tool.SerialTool):

    def __init__(self, signal, name, port, baud, databit, paritybit, stopbit):
        super(SerialToolEx, self).__init__(signal, name, port, baud, databit, paritybit, stopbit)
        self.encoding = 'ascii'
        self.error_policy = 'ignore'
        self.serial_log_filename = 'log' + os.sep + '%s_%s.log' % (name, datetime.datetime.now().strftime('%Y%m%d'))
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

    def send(self, text, is_hex=False):
        ctx = common.UpstreamLineContext()
        ctx.line_text = text
        ctx.is_hex = is_hex
        self.convert_to_io(ctx)
        super(SerialToolEx, self).send(ctx)
        self.serial_logging(ctx)
        self.gui_logging(ctx)

    @staticmethod
    def get_received_line_context():
        tmp = common.DownstreamLineContext()
        tmp.is_hex = False
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
