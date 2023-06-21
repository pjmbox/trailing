#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 6/21/2023 2:44 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_history.py
# ---------------------
import yaml
import ui_history
from PySide6.QtWidgets import QGroupBox, QListWidgetItem


class GuiHistoryWindow(QGroupBox, ui_history.Ui_History):

    def __init__(self, parent):
        super(GuiHistoryWindow, self).__init__()
        self.parent = parent
        with open(self.parent.config.get_history_config_filename()) as f:
            self.history = yaml.safe_load(f)

    def setupUi(self, p_wnd):
        super(GuiHistoryWindow, self).setupUi(self)
        self.setParent(p_wnd)
        self.setAutoFillBackground(True)
        self.hide()

    def set_size(self, m, n):
        self.setFixedHeight(min(m, 15) * 17)
        self.setFixedWidth(min(n, 40) * 9)

    def save(self):
        with open(self.parent.config.get_history_config_filename(), 'w') as f:
            yaml.safe_dump(self.history, f)

    def _append_item(self, t, v):
        v = v.replace('\n', '').replace('\r', '')
        if len(v) > 0:
            tmp = self.history['history'][t]
            tmp = [x for x in tmp if x != v]
            tmp.append(v)
            if len(tmp) > 1000:
                tmp = tmp[1:]
            self.history['history'][t] = tmp

    def append_hex(self, v):
        self._append_item('hex', v)

    def append_text(self, v):
        self._append_item('text', v)
