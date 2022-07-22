import gui_agent
import py_uart_settings_window
import serial_tool_ex
import ui_mainwindow
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox


class MainWindow(ui_mainwindow.Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.uart = None
        self.signal = None
        self.w_settings = py_uart_settings_window.UartSettingsWindow()
        self.widget = QMainWindow()
        self.setupUi(self.widget)
        self.widget.resize(800, 600)

    def setupUi(self, main_window):
        super(MainWindow, self).setupUi(main_window)
        self.btn_uart_switch.clicked.connect(self.switch_uart)
        self.btn_uart_settings.toggled.connect(self.uart_settings)
        self.textEdit.document().setMaximumBlockCount(1000)
        self.signal = gui_agent.GuiAgent()
        self.signal.connect_gui(self._gui_agent)
        self.w_settings.widget.setParent(main_window)
        self.w_settings.hide()

    # misc gui functions
    def show(self):
        self.widget.show()

    @staticmethod
    def set_icon(wgt, fn):
        wgt.setIcon(QIcon(QPixmap(QImage(fn))))

    def set_max_lines(self, n):
        self.textEdit.document().setMaximumBlockCount(n)

    # windows signal handle functions
    def uart_settings(self, v):
        if v:
            x = self.btn_uart_settings.x()
            y = self.btn_uart_settings.y()
            self.w_settings.set_position(x, y + 300)
            self.w_settings.show()
        else:
            self.w_settings.hide()

    def switch_uart(self):
        if self.uart is None:
            self.btn_uart_switch.setEnabled(False)
            self.btn_uart_settings.setEnabled(False)
            self.uart = serial_tool_ex.SerialToolEx(self.signal, 'TextCom', 'COM3', 115200)
            self.uart.start()
        else:
            self.btn_uart_switch.setEnabled(False)
            self.uart.stop()

    # thread signal handle functions
    def _gui_agent(self, method, args):
        m = getattr(self, method)
        m(*args)

    def append_log(self, dt, dirs, text):
        tmp = dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        tmp = '%s %s %s' % (tmp, dirs.value, text)
        self.textEdit.append(tmp)

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
