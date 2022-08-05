#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 8/2/2022 11:08 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_aliases
# ---------------------
import yaml
import ui_aliases
from PySide6.QtWidgets import QGroupBox, QListWidgetItem


class GuiAliasesWindow(QGroupBox, ui_aliases.Ui_Aliases):

    def __init__(self, parent):
        super(GuiAliasesWindow, self).__init__()
        self.parent = parent
        with open(self.parent.config.get_aliases_config_filename()) as f:
            tmp = yaml.safe_load(f)['config']
            self.text_aliases = tmp['text']
            self.hex_aliases = tmp['hex']

    def setupUi(self, p_wnd):
        super(GuiAliasesWindow, self).setupUi(self)
        self.setParent(p_wnd)
        self.setAutoFillBackground(True)
        self.hide()
        self.list_aliases.itemDoubleClicked.connect(self.list_double_click)
        self.list_aliases.itemClicked.connect(self.list_click)

    def set_size(self, m, n):
        self.setFixedHeight(min(m, 15) * 17)
        self.setFixedWidth(min(n, 40) * 9)

    def _init_aliases_items(self, aliases):
        length = 0
        self.list_aliases.clear()
        for i in range(len(aliases)):
            c = aliases[i]['cmd']
            d = aliases[i]['desc']
            length = max(len(c), length)
            item = QListWidgetItem()
            item.setText(c)
            item.setToolTip(d)
            self.list_aliases.addItem(item)
        self.set_size(len(aliases), length)

    def setup_text_aliases(self):
        self._init_aliases_items(self.text_aliases)

    def setup_hex_aliases(self):
        self._init_aliases_items(self.hex_aliases)

    def list_double_click(self, item):
        self.parent.send(item.data(0))

    def list_click(self, item):
        self.parent.edt_sent.setText(item.data(0))
        self.parent.btn_aliases.setChecked(False)
        self.parent.edt_sent.setFocus()
