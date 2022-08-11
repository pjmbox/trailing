#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/18/2022 2:56 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : gui_main_window.py
# ---------------------
import logging

import common
import signal_agent
import gui_uart_settings
import gui_max_rows
import gui_aliases
import gui_actions
import serial_tool
import ui_main_window
import config
import re
import yaml
from PySide6.QtGui import QImage, QPixmap, QIcon, QTextCursor, QMouseEvent, QCloseEvent, QSyntaxHighlighter, \
    QTextCharFormat, Qt, QFont
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer


class UartHighLighter(QSyntaxHighlighter):

    def __init__(self, parent):
        super(UartHighLighter, self).__init__(parent)
        self.config = parent.config
        self._mappings = {}
        with open(self.config.get_highlight_config_filename()) as f:
            self.config = yaml.safe_load(f)
        for item in self.config['highlight']['rcv_text']:
            fmt = QTextCharFormat()
            fmt.setFontWeight(QFont.Weight.__dict__[item['weight']])
            fmt.setForeground(Qt.GlobalColor.__dict__[item['color']])
            self._mappings[item['pattern']] = fmt
        dt, s, c = self.get_timestamp()
        self.datetime_format = dt
        self.timestamp_format = '<font size="%d" color="%s">%%s</font>' % (s, c)
        s, c = self.get_from_arrow()
        self.arrow_from_format = '<font size="%d" color="%s">%%s</font>' % (s, c)
        s, c = self.get_to_arrow()
        self.arrow_to_format = '<font size="%d" color="%s">%%s</font>' % (s, c)
        _, c = self.get_snd_text()
        self.snd_text_format = '<span style="font-color=%s; font-weight=bolder;">%%s</span>' % c

    @staticmethod
    def escape_text(text):
        return text.replace('<', '&lt;')

    def get_timestamp(self):
        tmp = self.config['highlight']['timestamp']
        return tmp['datetime_fmt_str'], tmp['size'], tmp['color']

    def get_to_arrow(self):
        tmp = self.config['highlight']['arrow']['to_uart']
        return tmp['size'], tmp['color']

    def get_from_arrow(self):
        tmp = self.config['highlight']['arrow']['from_uart']
        return tmp['size'], tmp['color']

    def get_snd_text(self):
        tmp = self.config['highlight']['snd_text']
        return tmp['size'], tmp['color']

    def highlightBlock(self, text):
        for pattern, fmt in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, fmt)

    def set_document(self, doc):
        self.setDocument(doc)

    def format_timestamp(self, dt):
        t0 = dt.strftime(self.datetime_format)
        return self.timestamp_format % t0

    def format_arrow(self, arrow):
        if arrow == common.UartDirection.FromUart:
            return self.arrow_from_format % self.escape_text(arrow.value)
        if arrow == common.UartDirection.ToUart:
            return self.arrow_to_format % self.escape_text(arrow.value)
        return ''

    def format_text(self, text, arrow):
        if arrow == common.UartDirection.ToUart:
            return self.snd_text_format % self.escape_text(text)
        else:
            return text


class MainWindow(QMainWindow, ui_main_window.Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.uart = None
        self.last_vb_max = None
        self.tgt_vb_pos = None
        self.config = config.Config()
        self.signal = signal_agent.GuiAgent()
        self.highlighter = UartHighLighter(self)
        self.uart_settings = gui_uart_settings.UartSettingsWindow(self)
        self.gui_max_rows = gui_max_rows.GuiMaxRowsWindow(self)
        self.gui_aliases = gui_aliases.GuiAliasesWindow(self)
        self.gui_actions = gui_actions.GuiActionsWindow(self)
        self.setupUi(self)

    def setupUi(self, p_wnd):
        super(MainWindow, self).setupUi(p_wnd)

        self.uart_settings.setupUi(self)
        self.gui_max_rows.setupUi(self)
        self.gui_aliases.setupUi(self)
        self.gui_actions.setupUi(self)
        self.highlighter.set_document(self.edt_received.document())
        self.signal.connect_gui(self._gui_agent)

        self.setWindowTitle('Trailing')

        self.setGeometry(self.config.get_rect())
        self.uart_settings.set_settings(*self.config.get_uart_settings())
        self.uart_settings.start_refresh()

        h, a, m = self.config.get_rcv_text()
        self.btn_hex_received.setChecked(h)
        self.btn_scroll_down.setChecked(a)
        self.edt_received.document().setMaximumBlockCount(m)

        h, c, ln = self.config.get_snd_text()
        self.btn_hex_sent.setChecked(h)
        self.btn_carrier_return.setChecked(c)
        self.btn_line_feed.setChecked(ln)

        if self.btn_hex_sent.isChecked():
            self.btn_carrier_return.setEnabled(False)
            self.btn_line_feed.setEnabled(False)

        if not self.btn_scroll_down.isChecked():
            self.last_vb_max = self.edt_received.verticalScrollBar().maximum()
            self.tgt_vb_pos = self.edt_received.verticalScrollBar().value()
            self.edt_received.verticalScrollBar().rangeChanged.connect(self.textedit_vb_range_changed)
            self.edt_received.verticalScrollBar().valueChanged.connect(self.textedit_vb_value_changed)

        self.btn_uart_settings.toggled.connect(self.switch_uart_settings)
        self.btn_uart_switch.clicked.connect(self.switch_uart)
        self.btn_scroll_down.toggled.connect(self.switch_screen_auto_scroll)
        self.btn_clear.clicked.connect(self.click_clear_uart_log)
        self.btn_max_rows.toggled.connect(self.switch_max_rows)
        self.btn_hex_received.toggled.connect(self.switch_hex_input)
        self.btn_send.clicked.connect(self.send_to_uart)
        self.edt_sent.returnPressed.connect(self.send_to_uart)
        self.btn_hex_sent.toggled.connect(self.switch_hex_output)
        self.btn_actions.clicked.connect(self.switch_actions)
        self.btn_aliases.toggled.connect(self.switch_aliases)
        self.groupbox_bottom.clicked.connect(self.un_click_all_bottom_buttons)

    # misc gui functions
    @staticmethod
    def set_icon(wgt, fn):
        wgt.setIcon(QIcon(QPixmap(QImage(fn))))

    def send(self, txt):
        if self.uart is not None:
            if not self.uart.hex_output:
                if self.btn_carrier_return.isChecked():
                    txt += '\r'
                if self.btn_line_feed.isChecked():
                    txt += '\n'
            try:
                self.uart.send(txt)
            except Exception as e:
                logging.error(e)
                self.show_alert('Error', str(e))

    def set_max_rows(self, n):
        self.edt_received.document().setMaximumBlockCount(n)

    def get_max_rows(self):
        return self.edt_received.document().maximumBlockCount()

    # windows signal handle functions
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.btn_uart_settings.setChecked(False)
        self.btn_max_rows.setChecked(False)
        self.btn_font.setChecked(False)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.config.set_uart_settings(*self.uart_settings.get_settings())
        self.config.set_rect(self.geometry())
        self.config.set_rcv_text(self.btn_hex_received.isChecked(),
                                 self.btn_scroll_down.isChecked(),
                                 self.get_max_rows())
        self.config.set_snd_text(self.btn_hex_sent.isChecked(),
                                 self.btn_carrier_return.isChecked(),
                                 self.btn_line_feed.isChecked())
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
            QTimer.singleShot(0, lambda: self.edt_received.verticalScrollBar().setValue(self.tgt_vb_pos))
        self.last_vb_max = m

    # toolbar button slot function
    def un_click_all_bottom_buttons(self):
        self.btn_aliases.setChecked(False)

    def send_to_uart(self):
        if self.btn_aliases.isChecked():
            self.btn_aliases.setChecked(False)
        self.send(self.edt_sent.text())

    def switch_uart_settings(self, v):
        if v:
            if self.btn_max_rows.isChecked():
                self.btn_max_rows.setChecked(False)
                self.gui_max_rows.hide()
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
            hr = self.btn_hex_received.isChecked()
            hs = self.btn_hex_sent.isChecked()
            self.uart = serial_tool.SerialToolEx(self.signal, p.lower(), p, b, db, pb, sb, hr, hs)
            self.uart.start()
        else:
            self.btn_uart_switch.setEnabled(False)
            self.uart.stop()

    def switch_screen_auto_scroll(self, v):
        if v:
            self.edt_received.moveCursor(QTextCursor.End)
            self.edt_received.verticalScrollBar().rangeChanged.disconnect(self.textedit_vb_range_changed)
            self.edt_received.verticalScrollBar().valueChanged.disconnect(self.textedit_vb_value_changed)
        else:
            self.last_vb_max = self.edt_received.verticalScrollBar().maximum()
            self.tgt_vb_pos = self.edt_received.verticalScrollBar().value()
            self.edt_received.verticalScrollBar().rangeChanged.connect(self.textedit_vb_range_changed)
            self.edt_received.verticalScrollBar().valueChanged.connect(self.textedit_vb_value_changed)

    def click_clear_uart_log(self):
        self.edt_received.clear()

    def switch_hex_input(self, v):
        if self.uart is not None:
            self.uart.hex_input = v

    def switch_hex_output(self, v):
        if self.uart is not None:
            self.uart.hex_output = v
        if self.btn_aliases.isChecked():
            self.btn_aliases.setChecked(False)
        self.btn_carrier_return.setEnabled(not v)
        self.btn_line_feed.setEnabled(not v)

    def switch_max_rows(self, v):
        if v:
            if self.btn_uart_settings.isChecked():
                self.btn_uart_settings.setChecked(False)
                self.uart_settings.hide()
            g = self.btn_max_rows.geometry()
            self.gui_max_rows.move(g.x() + 1, g.y() + g.height() + 4)
            self.gui_max_rows.show()
        else:
            self.gui_max_rows.hide()

    def switch_aliases(self, v):
        if v:
            if self.btn_actions.isChecked():
                self.btn_actions.setChecked(False)
                self.gui_actions.hide()
            self.gui_aliases.setup_aliases(self.btn_hex_sent.isChecked())
            g1 = self.btn_aliases.geometry()
            g2 = self.edt_received.geometry()
            self.gui_aliases.move(g1.x() - 32, g2.y() + g2.height() - self.gui_aliases.height() - 1)
            self.gui_aliases.show()
        else:
            self.gui_aliases.hide()

    def switch_actions(self, v):
        if v:
            if self.btn_aliases.isChecked():
                self.btn_aliases.setChecked(False)
                self.gui_aliases.hide()
            g1 = self.btn_actions.geometry()
            g2 = self.edt_received.geometry()
            self.gui_actions.move(g1.x() - 32, g2.y() + g2.height() - self.gui_actions.height() - 1)
            self.gui_actions.show()
        else:
            self.gui_actions.hide()

    # thread signal slot functions
    def _gui_agent(self, method, args):
        m = getattr(self, method)
        m(*args)

    def append_log(self, dt, arrow, text):
        old_pos = self.edt_received.verticalScrollBar().value()
        t0 = self.highlighter.format_timestamp(dt)
        t1 = self.highlighter.format_arrow(arrow)
        t2 = self.highlighter.format_text(text, arrow)
        self.edt_received.append('%s %s %s' % (t0, t1, t2))
        if self.btn_scroll_down.isChecked():
            self.edt_received.moveCursor(QTextCursor.End)
            self.edt_received.moveCursor(QTextCursor.StartOfLine)
        else:
            self.edt_received.verticalScrollBar().setValue(old_pos)

    def uart_is_running(self):
        self.set_icon(self.btn_uart_switch, 'resources/stop')
        self.btn_uart_switch.setEnabled(True)
        self.edt_sent.setEnabled(True)
        self.btn_hex_sent.setEnabled(True)
        self.btn_send.setEnabled(True)
        self.btn_actions.setEnabled(True)
        self.uart_settings.stop_refresh()
        if not self.btn_hex_sent.isChecked():
            self.btn_carrier_return.setEnabled(True)
            self.btn_line_feed.setEnabled(True)
            self.btn_aliases.setEnabled(True)

    def uart_is_stopped(self):
        self.uart = None
        self.set_icon(self.btn_uart_switch, 'resources/start')
        self.btn_uart_switch.setEnabled(True)
        self.btn_uart_settings.setEnabled(True)
        self.edt_sent.setEnabled(False)
        self.btn_hex_sent.setEnabled(False)
        self.btn_send.setEnabled(False)
        self.btn_carrier_return.setEnabled(False)
        self.btn_line_feed.setEnabled(False)
        self.btn_aliases.setEnabled(False)
        self.btn_actions.setEnabled(False)
        self.uart_settings.start_refresh()

    @staticmethod
    def show_alert(title, text):
        QMessageBox(QMessageBox.Critical, title, text, QMessageBox.Ok).exec_()
