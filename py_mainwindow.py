#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/18/2022 2:56 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : py_mainwindow.py
# ---------------------
import gui_agent
import py_uart_settings_window
import serial_tool_ex
import ui_mainwindow
from PySide6.QtGui import QImage, QPixmap, QIcon, QTextCursor
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer


class MainWindow(ui_mainwindow.Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.uart = None
        self.signal = None
        self.last_vb_max = None
        self.tgt_vb_pos = None
        self.win_root = QMainWindow()
        self.setupUi(self.win_root)
        self.win_root.resize(800, 600)
        self.win_settings = py_uart_settings_window.UartSettingsWindow(self)
        self.win_settings.setupUi(self.win_root)

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

    # misc gui functions
    def show(self):
        self.win_root.show()

    @staticmethod
    def set_icon(wgt, fn):
        wgt.setIcon(QIcon(QPixmap(QImage(fn))))

    def set_max_lines(self, n):
        self.textEdit.document().setMaximumBlockCount(n)

    def clear_uart_log(self):
        self.textEdit.clear()

    # windows signal handle functions
    def textedit_vb_value_changed(self, p):
        self.tgt_vb_pos = p

    def textedit_vb_range_changed(self, _, m):
        if m < self.last_vb_max:
            self.tgt_vb_pos = max(self.tgt_vb_pos - (self.last_vb_max - m), 0)
            QTimer.singleShot(0, lambda: self.textEdit.verticalScrollBar().setValue(self.tgt_vb_pos))
        self.last_vb_max = m

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

    def switch_max_line(self, v):
        pass

    def switch_uart_settings(self, v):
        if v:
            x = self.btn_uart_settings.x()
            y = self.btn_uart_settings.y()
            h = self.btn_uart_switch.height()
            self.win_settings.move(x + 1, y + h + 4)
            self.win_settings.show()
        else:
            self.win_settings.hide()

    def switch_uart(self):
        if self.uart is None:
            if self.btn_uart_settings.isChecked():
                self.btn_uart_settings.setChecked(False)
            self.btn_uart_switch.setEnabled(False)
            self.btn_uart_settings.setEnabled(False)
            p, b, db, pb, sb = self.win_settings.get_settings()
            self.uart = serial_tool_ex.SerialToolEx(self.signal, p.lower(), p, b, db, pb, sb)
            self.uart.start()
        else:
            self.btn_uart_switch.setEnabled(False)
            self.uart.stop()

    # thread signal handle functions
    def _gui_agent(self, method, args):
        m = getattr(self, method)
        m(*args)

    def append_log(self, dt, dirs, text):
        old_pos = self.textEdit.verticalScrollBar().value()
        tmp = dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        tmp = '%s %s %s' % (tmp, dirs.value, text)
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
