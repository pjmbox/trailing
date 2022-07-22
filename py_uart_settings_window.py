#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/21/2022 5:58 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : win_uart_settings
# ---------------------
import ui_uart_settings_window
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QPoint, QSize


class UartSettingsWindow(ui_uart_settings_window.Ui_UartSettingsWindow):

    def __init__(self):
        super(UartSettingsWindow, self).__init__()
        self.widget = QWidget()
        self.widget.setFixedSize(QSize(236, 84))
        self.widget.setAutoFillBackground(True)
        self.setupUi(self.widget)
        self.comboBox_uart_name.addItems(['COM1', 'COM2', 'COM3'])
        self.comboBox_uart_baud.addItems(['4800', '9600', '19200', '38400', '115200'])
        self.comboBox_uart_stopbit.addItems(['1', '1.5', '2'])
        self.comboBox_uart_databit.addItems(['5', '7', '8'])
        self.comboBox_uart_oddbit.addItems(['N', 'E', 'O'])
        self.comboBox_uart_baud.setCurrentText('115200')
        self.comboBox_uart_name.setCurrentText('COM3')
        self.comboBox_uart_stopbit.setCurrentText('1')
        self.comboBox_uart_databit.setCurrentText('8')
        self.comboBox_uart_oddbit.setCurrentText('N')


    def show(self):
        self.widget.show()

    def hide(self):
        self.widget.hide()

    def set_position(self, x, y):
        self.widget.pos = QPoint(x, y)
