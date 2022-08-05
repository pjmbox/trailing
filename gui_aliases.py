#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 8/2/2022 11:08 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_aliases
# ---------------------
import ui_aliases
import yaml
from PySide6.QtWidgets import QGroupBox


class GuiAliasesWindow(QGroupBox, ui_aliases.Ui_Aliases):

    def __init__(self, parent):
        super(GuiAliasesWindow, self).__init__()
        self.parent = parent
        self.text_aliases = []
        self.hex_aliases = []
        self.text_items = []
        self.hex_items = []
        self.text_max_len = 0
        self.hex_max_len = 0
        self.load_aliases()

    @staticmethod
    def _init_aliases_items(items, aliases):
        length = 0
        for i in range(len(aliases)):
            tmp = aliases[i]['cmd']
            if len(tmp) > length:
                length = len(tmp)
            items.append(aliases[i]['cmd'])
        return length

    def set_size(self, m, n):
        m = min(m, 15)
        n = min(n, 40)
        self.setFixedHeight(m * 17)
        self.setFixedWidth(n * 9)

    def load_aliases(self):
        with open(self.parent.config.get_aliases_config_filename()) as f:
            tmp = yaml.safe_load(f)
            tmp = tmp['config']
            self.text_aliases = tmp['text']
            self.hex_aliases = tmp['hex']
        self.text_items = []
        self.text_max_len = self._init_aliases_items(self.text_items, self.text_aliases)
        self.hex_items = []
        self.hex_max_len = self._init_aliases_items(self.hex_items, self.hex_aliases)

    def setupUi(self, p_wnd):
        super(GuiAliasesWindow, self).setupUi(self)
        self.setParent(p_wnd)
        self.setAutoFillBackground(True)
        self.hide()
        self.list_aliases.itemDoubleClicked.connect(self.list_double_click)
        self.list_aliases.itemClicked.connect(self.list_click)

    def setup_text_aliases(self):
        self.list_aliases.clear()
        self.list_aliases.addItems(self.text_items)
        self.set_size(len(self.text_items), self.text_max_len)

    def setup_hex_aliases(self):
        self.list_aliases.clear()
        self.list_aliases.addItems(self.hex_items)
        self.set_size(len(self.hex_items), self.hex_max_len)

    def list_double_click(self, item):
        self.parent.send(item.data(0))

    def list_click(self, item):
        self.parent.edt_sent.setText(item.data(0))
        self.parent.btn_aliases.setChecked(False)
        self.parent.edt_sent.setFocus()
