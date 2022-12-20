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


class GuiAgentMain(GuiAgent):

    def append_log(self, txt):
        self._emit_gui('append_log', (txt,))

    def uart_is_running(self):
        self._emit_gui('uart_is_running', ())

    def uart_is_stopped(self):
        self._emit_gui('uart_is_stopped', ())

    def show_alert(self, title, text):
        self._emit_gui('show_alert', (title, text))


class GuiAgentAction(GuiAgent):

    def send(self, txt):
        self._emit_gui('send', (txt,))

    def is_started(self):
        self._emit_gui('is_started', ())

    def is_stopped(self):
        self._emit_gui('is_stopped', ())
