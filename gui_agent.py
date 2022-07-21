#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/21/2022 10:28 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : GuiAgent
# ---------------------
from PySide6.QtCore import Signal, QObject


# noinspection PyUnresolvedReferences
class GuiAgent(QObject):

    signal = Signal(str, tuple)

    def connect_gui(self, obj):
        self.signal.connect(obj)

    def disconnect_gui(self, obj):
        self.signal.disconnect(obj)

    def _emit_gui(self, method, args):
        self.signal.emit(method, args)

    def append_log(self, ctx):
        self._emit_gui('append_log', (ctx.time_raw, ctx.dir, ctx.line_text))

    def uart_is_running(self):
        self._emit_gui('uart_is_running', ())

    def uart_is_stopped(self):
        self._emit_gui('uart_is_stopped', ())
