#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/26/2022 4:22 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : py_gui_max_rows
# ---------------------
import ui_gui_max_rows
from PySide6.QtWidgets import QGroupBox
from PySide6.QtGui import QIntValidator


class GuiMaxRowsWindow(ui_gui_max_rows.Ui_gui_settings_max_rows):

    def __init__(self, p_main):
        super(GuiMaxRowsWindow, self).__init__()
        self.p_main = p_main
        self.win_root = None

    def setupUi(self, parent_root):
        self.win_root = QGroupBox()
        self.win_root.setParent(parent_root)
        self.win_root.setAutoFillBackground(True)
        self.win_root.hide()
        super(GuiMaxRowsWindow, self).setupUi(self.win_root)
        self.edt_max_rows.setValidator(QIntValidator(200, 100000))
        self.edt_max_rows.returnPressed.connect(self.return_pressed)

    # gui functions
    def show(self):
        self.edt_max_rows.setText(str(self.p_main.get_max_lines()))
        self.win_root.show()

    def hide(self):
        self.win_root.hide()

    def move(self, x, y):
        self.win_root.move(x, y)

    def return_pressed(self):
        self.p_main.set_max_lines(int(self.edt_max_rows.text()))
        self.p_main.btn_max_line.setChecked(False)
