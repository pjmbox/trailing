#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/18/2022 2:56 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_main_window.py
# ---------------------
import common
import signal_agent
import gui_uart_settings
import gui_max_rows
import serial_tool
import ui_mainwindow
import config
import re
import yaml
from PySide6.QtGui import QImage, QPixmap, QIcon, QTextCursor, QMouseEvent, QCloseEvent, QSyntaxHighlighter, \
    QTextCharFormat, Qt, QFont
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer


class UartHighLighter(QSyntaxHighlighter):

    config_filename = 'highlight.yaml'

    def __init__(self, parent=None):
        super(UartHighLighter, self).__init__(parent)
        self._mappings = {}
        with open(self.config_filename) as f:
            self.config = yaml.safe_load(f)

    def highlightBlock(self, text):
        for pattern, fmt in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, fmt)

    def set_document(self, doc):
        for item in self.config['highlight']:
            fmt = QTextCharFormat()
            fmt.setFontWeight(QFont.Weight.__dict__[item['weight']])
            fmt.setForeground(Qt.GlobalColor.__dict__[item['color']])
            self._mappings[item['pattern']] = fmt
        self.setDocument(doc)


class MainWindow(QMainWindow, ui_mainwindow.Ui_Trailing):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.uart = None
        self.last_vb_max = None
        self.tgt_vb_pos = None
        self.config = config.Config()
        self.signal = signal_agent.GuiAgent()
        self.highlighter = UartHighLighter()
        self.uart_settings = gui_uart_settings.UartSettingsWindow(self)
        self.gui_max_rows = gui_max_rows.GuiMaxRowsWindow(self)
        self.setupUi(self)

    def setupUi(self, p_wnd):
        super(MainWindow, self).setupUi(p_wnd)

        self.uart_settings.setupUi(self)
        self.gui_max_rows.setupUi(self)
        self.highlighter.set_document(self.textEdit.document())
        self.signal.connect_gui(self._gui_agent)

        self.setWindowTitle('Trailing')
        self.setGeometry(self.config.get_rect())
        self.textEdit.document().setMaximumBlockCount(self.config.get_max_rows())
        self.uart_settings.set_settings(*self.config.get_uart_settings())
        self.btn_screen_down.setChecked(self.config.get_auto_scroll())

        if not self.btn_screen_down.isChecked():
            self.last_vb_max = self.textEdit.verticalScrollBar().maximum()
            self.tgt_vb_pos = self.textEdit.verticalScrollBar().value()
            self.textEdit.verticalScrollBar().rangeChanged.connect(self.textedit_vb_range_changed)
            self.textEdit.verticalScrollBar().valueChanged.connect(self.textedit_vb_value_changed)

        self.btn_uart_switch.clicked.connect(self.switch_uart)
        self.btn_uart_settings.toggled.connect(self.switch_uart_settings)
        self.btn_screen_down.toggled.connect(self.switch_screen_auto_scroll)
        self.btn_max_line.toggled.connect(self.switch_max_line)
        self.btn_uart_clear.clicked.connect(self.click_clear_uart_log)

    # misc gui functions
    @staticmethod
    def set_icon(wgt, fn):
        wgt.setIcon(QIcon(QPixmap(QImage(fn))))

    def set_max_lines(self, n):
        self.textEdit.document().setMaximumBlockCount(n)

    def get_max_lines(self):
        return self.textEdit.document().maximumBlockCount()

    # windows signal handle functions
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.btn_uart_settings.setChecked(False)
        self.btn_max_line.setChecked(False)
        self.btn_font.setChecked(False)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.config.save_rect(self.geometry())
        self.config.save_max_rows(self.get_max_lines())
        self.config.save_auto_scroll(self.btn_screen_down.isChecked())
        self.config.save_uart_settings(*self.uart_settings.get_settings())
        self.config.save()
        if self.uart is not None:
            self.uart.stop()
            self.uart = None

    # slot functions
    def textedit_vb_value_changed(self, p):
        self.tgt_vb_pos = p

    def textedit_vb_range_changed(self, _, m):
        if m < self.last_vb_max:
            self.tgt_vb_pos = max(self.tgt_vb_pos - (self.last_vb_max - m), 0)
            QTimer.singleShot(0, lambda: self.textEdit.verticalScrollBar().setValue(self.tgt_vb_pos))
        self.last_vb_max = m

    # toolbar button slot function
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
            self.uart = serial_tool.SerialToolEx(self.signal, p.lower(), p, b, db, pb, sb)
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

    def click_clear_uart_log(self):
        self.textEdit.clear()

    def switch_max_line(self, v):
        if v:
            g = self.btn_max_line.geometry()
            self.gui_max_rows.move(g.x() + 1, g.y() + g.height() + 4)
            self.gui_max_rows.show()
        else:
            self.gui_max_rows.hide()

    # thread signal slot functions
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
            self.textEdit.moveCursor(QTextCursor.StartOfLine)
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
