#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 8/11/2022 10:23 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_actions
# ---------------------

import yaml
import ui_actions
from PySide6.QtWidgets import QGroupBox


class GuiActionsWindow(QGroupBox, ui_actions.Ui_Actions):

    def __init__(self, parent):
        super(GuiActionsWindow, self).__init__()
        self.parent = parent
        self.actions = None
        self.load_config()

    def load_config(self):
        with open(self.parent.config.get_actions_config_filename()) as f:
            self.actions = yaml.safe_load(f)['actions']

    def init_cmb(self):
        self.cmb_select.clear()
        tmp = ['']
        tmp.extend(self.actions.keys())
        self.cmb_select.addItems(tmp)
        self.cmb_select.setCurrentText('')
        self.tbl_actions.clear()

    def setupUi(self, p_wnd):
        super(GuiActionsWindow, self).setupUi(self)
        self.setParent(p_wnd)
        self.setAutoFillBackground(True)
        self.hide()
        self.btn_refresh.clicked.connect(self.refresh)
        self.refresh()

    # slot functions
    def refresh(self):
        self.load_config()
        self.init_cmb()