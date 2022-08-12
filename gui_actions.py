#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 8/11/2022 10:23 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_actions
# ---------------------

import yaml
import ui_actions
from PySide6.QtWidgets import QGroupBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class GuiActionsWindow(QGroupBox, ui_actions.Ui_Actions):

    def __init__(self, parent):
        super(GuiActionsWindow, self).__init__()
        self.parent = parent
        self.act_config = None
        self.is_hex = None
        self.acts = None
        self.act_ind = None
        self.load_config()

    def load_config(self):
        with open(self.parent.config.get_actions_config_filename()) as f:
            self.act_config = yaml.safe_load(f)['actions']

    def init_cmb(self):
        self.cmb_select.clear()
        tmp = ['']
        tmp.extend(self.act_config.keys())
        self.cmb_select.addItems(tmp)
        self.cmb_select.setCurrentText('')
        self.tbl_actions.clear()

    def setupUi(self, p_wnd):
        super(GuiActionsWindow, self).setupUi(self)
        self.setParent(p_wnd)
        self.setAutoFillBackground(True)
        self.hide()
        self.btn_refresh.clicked.connect(self.refresh)
        self.cmb_select.currentIndexChanged.connect(self.action_change)
        self.refresh()

    # slot functions
    def refresh(self):
        self.load_config()
        self.init_cmb()

    @staticmethod
    def _generate_table_item(v):
        if v is None or (v is str and v == ''):
            v = 'none'
        if v is int:
            v = float(v)
        if v is float and v < 0.0:
            v = 0.0
        tmp = QTableWidgetItem(str(v))
        tmp.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        return tmp

    def _generate_table_header_item(self, v):
        tmp = self._generate_table_item(v)
        tmp.setBackground(QColor(100, 100, 100))
        return tmp

    def action_change(self):
        self.tbl_actions.clear()
        tmp = self.cmb_select.currentText()
        if tmp in self.act_config:
            tmp = self.act_config[tmp]
            self.btn_switch.setEnabled(True)
            self.is_hex = tmp['is_hex']
            self.acts = tmp['actions']
            self.act_ind = 0
            self.tbl_actions.clear()
            self.tbl_actions.setFocusPolicy(Qt.NoFocus)
            self.tbl_actions.setColumnCount(3)
            self.tbl_actions.setColumnWidth(0, 200)
            self.tbl_actions.setColumnWidth(1, 50)
            self.tbl_actions.setColumnWidth(2, 200)
            self.tbl_actions.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tbl_actions.setRowCount(len(self.acts))
            self.tbl_actions.setHorizontalHeaderItem(0, self._generate_table_header_item('flag'))
            self.tbl_actions.setHorizontalHeaderItem(1, self._generate_table_header_item('delay'))
            self.tbl_actions.setHorizontalHeaderItem(2, self._generate_table_header_item('command'))
            self.tbl_actions.horizontalHeader().setEnabled(True)
            for i, a in enumerate(tmp['actions']):
                self.tbl_actions.setRowHeight(i, 17)
                cmd = self._generate_table_item(a['cmd'])
                flag = self._generate_table_item(a['flag'])
                delay = self._generate_table_item(a['delay'])
                self.tbl_actions.setItem(i, 0, flag)
                self.tbl_actions.setItem(i, 1, delay)
                self.tbl_actions.setItem(i, 2, cmd)
            self.tbl_actions.selectRow(0)
        else:
            self.btn_switch.setEnabled(False)
