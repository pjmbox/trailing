#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/21/2022 5:58 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : win_uart_settings
# ---------------------
import ui_uart_settings
import serial.tools.list_ports
from PySide6.QtWidgets import QGroupBox
from PySide6.QtCore import QTimer


class UartSettingsWindow(QGroupBox, ui_uart_settings.Ui_UartSettings):

    def __init__(self, parent):
        super(UartSettingsWindow, self).__init__()
        self.parent = parent
        self.timer = QTimer()
        self.com_list = None

    def setupUi(self, p_wnd):
        super(UartSettingsWindow, self).setupUi(self)
        self.setParent(p_wnd)
        self.setAutoFillBackground(True)
        self.hide()
        self.com_list = self.get_port_list()
        self.comboBox_uart_name.addItems(self.com_list)
        self.comboBox_uart_name.setCurrentText('')
        self.comboBox_uart_baud.addItems(['50', '75', '110', '134', '150', '200', '300', '600', '1200', '1800',
                                          '2400', '4800', '9600', '19200', '38400', '57600', '115200', '230400',
                                          '460800', '500000', '576000', '921600', '1000000', '1152000', '1500000',
                                          '2000000', '2500000', '3000000', '3500000', '4000000'])
        self.comboBox_uart_baud.setCurrentText('115200')
        self.comboBox_uart_stopbit.addItems(['1', '1.5', '2'])
        self.comboBox_uart_stopbit.setCurrentText('1')
        self.comboBox_uart_databit.addItems(['5', '6', '7', '8'])
        self.comboBox_uart_databit.setCurrentText('8')
        self.comboBox_uart_oddbit.addItems(['N', 'E', 'O', 'M', 'S'])
        self.comboBox_uart_oddbit.setCurrentText('N')
        self.comboBox_uart_name.currentIndexChanged.connect(self.slot_update_settings)
        self.comboBox_uart_baud.currentIndexChanged.connect(self.slot_update_settings)
        self.comboBox_uart_databit.currentIndexChanged.connect(self.slot_update_settings)
        self.comboBox_uart_oddbit.currentIndexChanged.connect(self.slot_update_settings)
        self.comboBox_uart_stopbit.currentIndexChanged.connect(self.slot_update_settings)
        self.timer.timeout.connect(self.slot_update_com_list)
        self.slot_update_settings()

    # util functions
    @staticmethod
    def get_port_list():
        tmp = ['']
        for port in list(serial.tools.list_ports.comports()):
            tmp.append(port.device)
        return tmp

    def get_settings(self):
        name = self.comboBox_uart_name.currentText()
        baud = self.comboBox_uart_baud.currentText()
        dbit = self.comboBox_uart_databit.currentText()
        obit = self.comboBox_uart_oddbit.currentText()
        sbit = self.comboBox_uart_stopbit.currentText()
        return name, int(baud), int(dbit), obit, float(sbit)

    def set_settings(self, name, baud, data, parity, stop):
        if name in self.com_list:
            self.comboBox_uart_name.setCurrentText(name)
        self.comboBox_uart_baud.setCurrentText(str(baud))
        self.comboBox_uart_databit.setCurrentText(str(data))
        self.comboBox_uart_oddbit.setCurrentText(parity)
        self.comboBox_uart_stopbit.setCurrentText(str(stop))

    # gui functions
    def show(self):
        self.timer.start(1000)
        super(UartSettingsWindow, self).show()

    def hide(self):
        self.timer.stop()
        super(UartSettingsWindow, self).hide()

    # slot functions
    def slot_update_com_list(self):
        tmp = self.get_port_list()
        if tmp != self.com_list:
            text = self.comboBox_uart_name.currentText()
            self.comboBox_uart_name.clear()
            self.comboBox_uart_name.addItems(tmp)
            self.comboBox_uart_name.setCurrentText('' if text not in tmp else text)
            self.com_list = tmp

    def slot_update_settings(self):
        name = self.comboBox_uart_name.currentText()
        baud = self.comboBox_uart_baud.currentText()
        dbit = self.comboBox_uart_databit.currentText()
        obit = self.comboBox_uart_oddbit.currentText()
        sbit = self.comboBox_uart_stopbit.currentText()
        if name is None or name == '' or name == 'none':
            name = 'none'
            self.parent.btn_uart_switch.setEnabled(False)
        else:
            self.parent.btn_uart_switch.setEnabled(True)
        tmp = '%s\n%s%s%s %s' % (name, dbit, obit, sbit, baud)
        self.parent.btn_uart_settings.setText(tmp)
