#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 8/11/2022 10:23 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_actions
# ---------------------

import yaml
import ui_actions
from PySide6.QtWidgets import QGroupBox, QListWidgetItem


class GuiActionsWindow(QGroupBox, ui_actions.Ui_Actions):

    def __init__(self, parent):
        super(GuiActionsWindow, self).__init__()
        self.parent = parent
        self.actions = None
        self.load_config()

    def load_config(self):
        with open(self.parent.config.get_aliases_config_filename()) as f:
            self.actions = yaml.safe_load(f)

    def setupUi(self, p_wnd):
        super(GuiActionsWindow, self).setupUi(self)
        self.setParent(p_wnd)
        self.setAutoFillBackground(True)
        self.hide()
