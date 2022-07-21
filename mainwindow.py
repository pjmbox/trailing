import logging

import gui_agent
import serial_tool_ex
import ui_mainwindow
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QImage, QPixmap, Qt, QIcon


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.uart = None
        self.signal = gui_agent.GuiAgent()
        self.signal.connect_gui(self._gui_agent)
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_uart_switch.clicked.connect(self.switch_uart)
        self.set_max_lines(1000)
        self.uart_running = False

    # misc gui functions
    @staticmethod
    def set_icon(wgt, fn):
        wgt.setIcon(QIcon(QPixmap(QImage(fn))))

    def set_max_lines(self, n):
        self.ui.textEdit.document().setMaximumBlockCount(n)

    # windows signal handle functions
    def switch_uart(self):
        if self.uart is None:
            self.ui.btn_uart_switch.setEnabled(False)
            self.ui.btn_uart_settings.setEnabled(False)
            self.uart = serial_tool_ex.SerialToolEx(self.signal, 'TextCom', 'COM3', 115200)
            self.uart.start()
        else:
            self.ui.btn_uart_switch.setEnabled(False)
            self.uart.stop()

    # thread signal handle functions
    def _gui_agent(self, method, args):
        m = getattr(self, method)
        m(*args)

    def append_log(self, dt, dirs, text):
        tmp = dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        tmp = '%s %s %s' % (tmp, dirs.value, text)
        self.ui.textEdit.append(tmp)

    def uart_is_running(self):
        self.set_icon(self.ui.btn_uart_switch, 'resources/stop')
        self.ui.btn_uart_switch.setEnabled(True)

    def uart_is_stopped(self):
        self.uart = None
        self.set_icon(self.ui.btn_uart_switch, 'resources/start')
        self.ui.btn_uart_switch.setEnabled(True)
        self.ui.btn_uart_settings.setEnabled(True)

    # entrypoint function
    @staticmethod
    def run():
        app = QApplication([])
        widget = MainWindow()
        widget.resize(800, 600)
        widget.show()
        try:
            sys.exit(app.exec())
        except Exception as e:
            logging.error(e)
