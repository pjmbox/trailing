#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 8/11/2022 10:23 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_actions
# ---------------------

import yaml

import agent_action
import ui_actions
import agent_signal
from PySide6.QtWidgets import QGroupBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class GuiActionsWindow(QGroupBox, ui_actions.Ui_Actions):

    def __init__(self, parent):
        super(GuiActionsWindow, self).__init__()
        self.parent = parent
        self.signal = agent_signal.GuiAgentAction()
        self.act_config = None
        self.is_hex = None
        self.acts = None
        self.act_ind = None
        self.agent = None
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
        self.signal.connect_gui(self._gui_agent)
        self.setAutoFillBackground(True)
        self.hide()
        self.btn_refresh.clicked.connect(self.refresh)
        self.btn_switch.clicked.connect(self.switch_action)
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
        tmp.setBackground(QColor(20, 200, 200))
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
            self.tbl_actions.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tbl_actions.setRowCount(len(self.acts))
            self.tbl_actions.horizontalHeader().setEnabled(True)
            self.tbl_actions.setColumnCount(4)
            self.tbl_actions.setColumnWidth(0, 200)
            self.tbl_actions.setColumnWidth(1, 60)
            self.tbl_actions.setColumnWidth(2, 40)
            self.tbl_actions.setColumnWidth(3, 150)
            self.tbl_actions.setHorizontalHeaderItem(0, self._generate_table_header_item('flag'))
            self.tbl_actions.setHorizontalHeaderItem(1, self._generate_table_header_item('timeout'))
            self.tbl_actions.setHorizontalHeaderItem(2, self._generate_table_header_item('delay'))
            self.tbl_actions.setHorizontalHeaderItem(3, self._generate_table_header_item('command'))
            for i, a in enumerate(tmp['actions']):
                self.tbl_actions.setRowHeight(i, 17)
                flag = self._generate_table_item(a['flag'])
                timeout = self._generate_table_item(a['timeout'])
                delay = self._generate_table_item(a['delay'])
                cmd = self._generate_table_item(a['cmd'])
                self.tbl_actions.setItem(i, 0, flag)
                self.tbl_actions.setItem(i, 1, timeout)
                self.tbl_actions.setItem(i, 2, delay)
                self.tbl_actions.setItem(i, 3, cmd)
            self.tbl_actions.selectRow(0)
        else:
            self.tbl_actions.setRowCount(0)
            self.tbl_actions.setColumnCount(0)
            self.btn_switch.setEnabled(False)

    def switch_action(self):
        self.btn_switch.setEnabled(False)
        if self.agent is None:
            self.agent = agent_action.ActionAgent(self.parent.uart, self.signal)
        else:
            self.agent.stop()

    # threading slot functions
    def _gui_agent(self, method, args):
        getattr(self, method)(*args)

    def send(self, txt):
        self.parent.send(txt)

    def is_started(self):
        pass