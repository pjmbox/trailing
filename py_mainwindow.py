#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/18/2022 2:56 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : py_mainwindow.py
# ---------------------
import common
import gui_agent
import py_uart_settings
import py_gui_max_rows
import serial_tool_ex
import ui_mainwindow
import highlighter
from PySide6.QtGui import QImage, QPixmap, QIcon, QTextCursor
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer


class MainWindow(ui_mainwindow.Ui_Trailing):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.uart = None
        self.signal = None
        self.last_vb_max = None
        self.tgt_vb_pos = None
        self.highlighter = None
        self.win_root = QMainWindow()
        self.setupUi(self.win_root)
        self.win_root.setWindowTitle('Trailing')
        self.win_root.resize(800, 600)
        self.uart_settings = py_uart_settings.UartSettingsWindow(self)
        self.uart_settings.setupUi(self.win_root)
        self.gui_max_rows = py_gui_max_rows.GuiMaxRowsWindow(self)
        self.gui_max_rows.setupUi(self.win_root)

    def setupUi(self, main_window):
        super(MainWindow, self).setupUi(main_window)

        self.btn_uart_switch.clicked.connect(self.switch_uart)
        self.btn_uart_settings.toggled.connect(self.switch_uart_settings)
        self.btn_screen_down.toggled.connect(self.switch_screen_auto_scroll)
        self.btn_max_line.toggled.connect(self.switch_max_line)
        self.btn_uart_clear.clicked.connect(self.clear_uart_log)

        if not self.btn_screen_down.isChecked():
            self.last_vb_max = self.textEdit.verticalScrollBar().maximum()
            self.tgt_vb_pos = self.textEdit.verticalScrollBar().value()
            self.textEdit.verticalScrollBar().rangeChanged.connect(self.textedit_vb_range_changed)
            self.textEdit.verticalScrollBar().valueChanged.connect(self.textedit_vb_value_changed)

        self.signal = gui_agent.GuiAgent()
        self.signal.connect_gui(self._gui_agent)
        self.textEdit.document().setMaximumBlockCount(500)
        self.highlighter = highlighter.UartHighLighter()
        self.highlighter.setup_gui(self.textEdit.document())

    # misc gui functions
    def show(self):
        self.win_root.show()

    @staticmethod
    def set_icon(wgt, fn):
        wgt.setIcon(QIcon(QPixmap(QImage(fn))))

    def set_max_lines(self, n):
        self.textEdit.document().setMaximumBlockCount(n)

    def get_max_lines(self):
        return self.textEdit.document().maximumBlockCount()

    # windows signal handle functions
    def textedit_vb_value_changed(self, p):
        self.tgt_vb_pos = p

    def textedit_vb_range_changed(self, _, m):
        if m < self.last_vb_max:
            self.tgt_vb_pos = max(self.tgt_vb_pos - (self.last_vb_max - m), 0)
            QTimer.singleShot(0, lambda: self.textEdit.verticalScrollBar().setValue(self.tgt_vb_pos))
        self.last_vb_max = m

    def form_click(self):
        self.btn_uart_settings.setChecked(False)
        self.btn_max_line.setChecked(False)
        self.btn_font.setChecked(False)

    # toolbar buttons
    def switch_uart_settings(self, v):
        if v:
            g = self.btn_uart_settings.geometry()
            self.uart_settings.move(g.x() + 1, g.y() + g.height() + 4)
            self.uart_settings.show()
        else:
            self.uart_settings.hide()

    def switch_uart(self):
        if self.uart is None:
            if self.btn_uart_settings.isChecked():
                self.btn_uart_settings.setChecked(False)
            self.btn_uart_switch.setEnabled(False)
            self.btn_uart_settings.setEnabled(False)
            p, b, db, pb, sb = self.uart_settings.get_settings()
            self.uart = serial_tool_ex.SerialToolEx(self.signal, p.lower(), p, b, db, pb, sb)
            self.uart.start()
        else:
            self.btn_uart_switch.setEnabled(False)
            self.uart.stop()

    def switch_screen_auto_scroll(self, v):
        if v:
            self.textEdit.moveCursor(QTextCursor.End)
            self.textEdit.verticalScrollBar().rangeChanged.disconnect(self.textedit_vb_range_changed)
            self.textEdit.verticalScrollBar().valueChanged.disconnect(self.textedit_vb_value_changed)
        else:
            self.last_vb_max = self.textEdit.verticalScrollBar().maximum()
            self.tgt_vb_pos = self.textEdit.verticalScrollBar().value()
            self.textEdit.verticalScrollBar().rangeChanged.connect(self.textedit_vb_range_changed)
            self.textEdit.verticalScrollBar().valueChanged.connect(self.textedit_vb_value_changed)

    def clear_uart_log(self):
        self.textEdit.clear()

    def switch_max_line(self, v):
        if v:
            g = self.btn_max_line.geometry()
            self.gui_max_rows.move(g.x() + 1, g.y() + g.height() + 4)
            self.gui_max_rows.show()
        else:
            self.gui_max_rows.hide()

    # thread signal handle functions
    def _gui_agent(self, method, args):
        m = getattr(self, method)
        m(*args)

    def append_log(self, dt, dirs, text):
        old_pos = self.textEdit.verticalScrollBar().value()
        t0 = dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        t0 = '<font size="2" color="maroon">%s</font>' % t0
        if dirs == common.UartDirection.FromUart:
            t1 = '<font size="2" color="green">%s</font>' % dirs.value
        else:
            t1 = '<font size="2" color="pink">%s</font>' % dirs.value
        tmp = '%s %s %s' % (t0, t1, text)
        self.textEdit.append(tmp)
        if self.btn_screen_down.isChecked():
            self.textEdit.moveCursor(QTextCursor.End)
        else:
            self.textEdit.verticalScrollBar().setValue(old_pos)

    def uart_is_running(self):
        self.set_icon(self.btn_uart_switch, 'resources/stop')
        self.btn_uart_switch.setEnabled(True)

    def uart_is_stopped(self):
        self.uart = None
        self.set_icon(self.btn_uart_switch, 'resources/start')
        self.btn_uart_switch.setEnabled(True)
        self.btn_uart_settings.setEnabled(True)

    @staticmethod
    def show_alert(title, text):
        QMessageBox(QMessageBox.Critical, title, text, QMessageBox.Ok).exec_()
