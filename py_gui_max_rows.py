#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/26/2022 4:22 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : py_gui_max_rows
# ---------------------
import ui_gui_max_rows
from PySide6.QtWidgets import QGroupBox
from PySide6.QtGui import QIntValidator, QFocusEvent


class GuiMaxRowsWindow(QGroupBox, ui_gui_max_rows.Ui_gui_settings_max_rows):

    def __init__(self, parent):
        super(GuiMaxRowsWindow, self).__init__()
        self.parent = parent

    def setupUi(self, p_wnd):
        super(GuiMaxRowsWindow, self).setupUi(self)
        self.setParent(p_wnd)
        self.setAutoFillBackground(True)
        self.hide()
        self.edt_max_rows.setValidator(QIntValidator(200, 100000))
        self.edt_max_rows.returnPressed.connect(self.slot_return_pressed)

    # gui functions
    def show(self):
        self.edt_max_rows.setText(str(self.parent.get_max_lines()))
        self.edt_max_rows.setFocus()
        super(GuiMaxRowsWindow, self).show()

    # slot functions
    def slot_return_pressed(self):
        self.parent.set_max_lines(int(self.edt_max_rows.text()))
        self.parent.btn_max_line.setChecked(False)
