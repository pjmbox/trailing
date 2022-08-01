# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(615, 484)
        icon = QIcon()
        icon.addFile(u"resources/trailing.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_wnd = QGridLayout(self.centralwidget)
        self.gridLayout_wnd.setSpacing(0)
        self.gridLayout_wnd.setObjectName(u"gridLayout_wnd")
        self.gridLayout_wnd.setContentsMargins(0, 0, 0, 0)
        self.groupbox_top = QGroupBox(self.centralwidget)
        self.groupbox_top.setObjectName(u"groupbox_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupbox_top.sizePolicy().hasHeightForWidth())
        self.groupbox_top.setSizePolicy(sizePolicy1)
        self.groupbox_top.setMinimumSize(QSize(0, 24))
        self.groupbox_top.setMaximumSize(QSize(16777215, 24))
        self.gridLayout_top = QGridLayout(self.groupbox_top)
        self.gridLayout_top.setSpacing(0)
        self.gridLayout_top.setObjectName(u"gridLayout_top")
        self.gridLayout_top.setContentsMargins(0, 0, 0, 0)
        self.btn_max_rows = QPushButton(self.groupbox_top)
        self.btn_max_rows.setObjectName(u"btn_max_rows")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_max_rows.sizePolicy().hasHeightForWidth())
        self.btn_max_rows.setSizePolicy(sizePolicy2)
        self.btn_max_rows.setMinimumSize(QSize(24, 24))
        self.btn_max_rows.setMaximumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u"resources/max_line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_max_rows.setIcon(icon1)
        self.btn_max_rows.setIconSize(QSize(18, 18))
        self.btn_max_rows.setCheckable(True)
        self.btn_max_rows.setFlat(True)

        self.gridLayout_top.addWidget(self.btn_max_rows, 0, 7, 1, 1)

        self.btn_uart_settings = QPushButton(self.groupbox_top)
        self.btn_uart_settings.setObjectName(u"btn_uart_settings")
        sizePolicy2.setHeightForWidth(self.btn_uart_settings.sizePolicy().hasHeightForWidth())
        self.btn_uart_settings.setSizePolicy(sizePolicy2)
        self.btn_uart_settings.setMinimumSize(QSize(70, 24))
        self.btn_uart_settings.setMaximumSize(QSize(70, 24))
        self.btn_uart_settings.setSizeIncrement(QSize(0, 0))
        self.btn_uart_settings.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(6)
        self.btn_uart_settings.setFont(font)
        self.btn_uart_settings.setStyleSheet(u"text-align: left; vertical-align: middle ;padding: 2px 2px 2px 2px; ")
        self.btn_uart_settings.setIconSize(QSize(0, 0))
        self.btn_uart_settings.setCheckable(True)
        self.btn_uart_settings.setFlat(True)

        self.gridLayout_top.addWidget(self.btn_uart_settings, 0, 0, 1, 1)

        self.horizontalspacer_top = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_top.addItem(self.horizontalspacer_top, 0, 9, 1, 1)

        self.line_1 = QFrame(self.groupbox_top)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShadow(QFrame.Raised)
        self.line_1.setFrameShape(QFrame.VLine)

        self.gridLayout_top.addWidget(self.line_1, 0, 2, 1, 1)

        self.btn_scroll_down = QPushButton(self.groupbox_top)
        self.btn_scroll_down.setObjectName(u"btn_scroll_down")
        sizePolicy2.setHeightForWidth(self.btn_scroll_down.sizePolicy().hasHeightForWidth())
        self.btn_scroll_down.setSizePolicy(sizePolicy2)
        self.btn_scroll_down.setMinimumSize(QSize(24, 24))
        self.btn_scroll_down.setMaximumSize(QSize(24, 24))
        icon2 = QIcon()
        icon2.addFile(u"resources/down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_scroll_down.setIcon(icon2)
        self.btn_scroll_down.setIconSize(QSize(18, 18))
        self.btn_scroll_down.setCheckable(True)
        self.btn_scroll_down.setChecked(True)
        self.btn_scroll_down.setFlat(True)

        self.gridLayout_top.addWidget(self.btn_scroll_down, 0, 3, 1, 1)

        self.line_2 = QFrame(self.groupbox_top)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Raised)
        self.line_2.setFrameShape(QFrame.VLine)

        self.gridLayout_top.addWidget(self.line_2, 0, 6, 1, 1)

        self.btn_hex_received = QPushButton(self.groupbox_top)
        self.btn_hex_received.setObjectName(u"btn_hex_received")
        sizePolicy2.setHeightForWidth(self.btn_hex_received.sizePolicy().hasHeightForWidth())
        self.btn_hex_received.setSizePolicy(sizePolicy2)
        self.btn_hex_received.setMinimumSize(QSize(24, 24))
        self.btn_hex_received.setMaximumSize(QSize(24, 24))
        icon3 = QIcon()
        icon3.addFile(u"resources/hex.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_hex_received.setIcon(icon3)
        self.btn_hex_received.setIconSize(QSize(18, 18))
        self.btn_hex_received.setCheckable(True)
        self.btn_hex_received.setFlat(True)

        self.gridLayout_top.addWidget(self.btn_hex_received, 0, 5, 1, 1)

        self.btn_clear = QPushButton(self.groupbox_top)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy2.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy2)
        self.btn_clear.setMinimumSize(QSize(24, 24))
        self.btn_clear.setMaximumSize(QSize(24, 24))
        icon4 = QIcon()
        icon4.addFile(u"resources/clear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear.setIcon(icon4)
        self.btn_clear.setIconSize(QSize(18, 18))
        self.btn_clear.setFlat(True)

        self.gridLayout_top.addWidget(self.btn_clear, 0, 4, 1, 1)

        self.btn_uart_switch = QPushButton(self.groupbox_top)
        self.btn_uart_switch.setObjectName(u"btn_uart_switch")
        sizePolicy2.setHeightForWidth(self.btn_uart_switch.sizePolicy().hasHeightForWidth())
        self.btn_uart_switch.setSizePolicy(sizePolicy2)
        self.btn_uart_switch.setMinimumSize(QSize(24, 24))
        self.btn_uart_switch.setMaximumSize(QSize(24, 24))
        self.btn_uart_switch.setBaseSize(QSize(24, 24))
        self.btn_uart_switch.setStyleSheet(u"padding: 2px;")
        icon5 = QIcon()
        icon5.addFile(u"resources/start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_uart_switch.setIcon(icon5)
        self.btn_uart_switch.setIconSize(QSize(18, 18))
        self.btn_uart_switch.setFlat(True)

        self.gridLayout_top.addWidget(self.btn_uart_switch, 0, 1, 1, 1)

        self.btn_font = QPushButton(self.groupbox_top)
        self.btn_font.setObjectName(u"btn_font")
        sizePolicy2.setHeightForWidth(self.btn_font.sizePolicy().hasHeightForWidth())
        self.btn_font.setSizePolicy(sizePolicy2)
        self.btn_font.setMinimumSize(QSize(24, 24))
        self.btn_font.setMaximumSize(QSize(24, 24))
        icon6 = QIcon()
        icon6.addFile(u"resources/font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_font.setIcon(icon6)
        self.btn_font.setIconSize(QSize(18, 18))
        self.btn_font.setCheckable(True)
        self.btn_font.setFlat(True)

        self.gridLayout_top.addWidget(self.btn_font, 0, 8, 1, 1)


        self.gridLayout_wnd.addWidget(self.groupbox_top, 0, 0, 1, 1)

        self.groupbox_bottom = QGroupBox(self.centralwidget)
        self.groupbox_bottom.setObjectName(u"groupbox_bottom")
        sizePolicy1.setHeightForWidth(self.groupbox_bottom.sizePolicy().hasHeightForWidth())
        self.groupbox_bottom.setSizePolicy(sizePolicy1)
        self.groupbox_bottom.setMinimumSize(QSize(0, 25))
        self.groupbox_bottom.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout = QHBoxLayout(self.groupbox_bottom)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 1)
        self.edt_sent = QLineEdit(self.groupbox_bottom)
        self.edt_sent.setObjectName(u"edt_sent")
        self.edt_sent.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(100)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.edt_sent.sizePolicy().hasHeightForWidth())
        self.edt_sent.setSizePolicy(sizePolicy3)
        self.edt_sent.setMinimumSize(QSize(0, 22))
        self.edt_sent.setMaximumSize(QSize(400, 22))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(7)
        self.edt_sent.setFont(font1)
        self.edt_sent.setMaxLength(512)
        self.edt_sent.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.edt_sent)

        self.btn_carrier_return = QPushButton(self.groupbox_bottom)
        self.btn_carrier_return.setObjectName(u"btn_carrier_return")
        self.btn_carrier_return.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btn_carrier_return.sizePolicy().hasHeightForWidth())
        self.btn_carrier_return.setSizePolicy(sizePolicy2)
        self.btn_carrier_return.setMinimumSize(QSize(24, 24))
        self.btn_carrier_return.setMaximumSize(QSize(24, 24))
        icon7 = QIcon()
        icon7.addFile(u"resources/cr.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carrier_return.setIcon(icon7)
        self.btn_carrier_return.setIconSize(QSize(18, 18))
        self.btn_carrier_return.setCheckable(True)
        self.btn_carrier_return.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_carrier_return)

        self.btn_line_feed = QPushButton(self.groupbox_bottom)
        self.btn_line_feed.setObjectName(u"btn_line_feed")
        self.btn_line_feed.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btn_line_feed.sizePolicy().hasHeightForWidth())
        self.btn_line_feed.setSizePolicy(sizePolicy2)
        self.btn_line_feed.setMinimumSize(QSize(24, 24))
        self.btn_line_feed.setMaximumSize(QSize(24, 24))
        icon8 = QIcon()
        icon8.addFile(u"resources/lf.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_line_feed.setIcon(icon8)
        self.btn_line_feed.setIconSize(QSize(18, 18))
        self.btn_line_feed.setCheckable(True)
        self.btn_line_feed.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_line_feed)

        self.btn_hex_sent = QPushButton(self.groupbox_bottom)
        self.btn_hex_sent.setObjectName(u"btn_hex_sent")
        self.btn_hex_sent.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btn_hex_sent.sizePolicy().hasHeightForWidth())
        self.btn_hex_sent.setSizePolicy(sizePolicy2)
        self.btn_hex_sent.setMinimumSize(QSize(24, 24))
        self.btn_hex_sent.setMaximumSize(QSize(24, 24))
        self.btn_hex_sent.setIcon(icon3)
        self.btn_hex_sent.setIconSize(QSize(18, 18))
        self.btn_hex_sent.setCheckable(True)
        self.btn_hex_sent.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_hex_sent)

        self.horizontalspacer_bottom = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalspacer_bottom)


        self.gridLayout_wnd.addWidget(self.groupbox_bottom, 3, 0, 1, 1)

        self.edt_received = QTextEdit(self.centralwidget)
        self.edt_received.setObjectName(u"edt_received")
        sizePolicy.setHeightForWidth(self.edt_received.sizePolicy().hasHeightForWidth())
        self.edt_received.setSizePolicy(sizePolicy)
        self.edt_received.setMaximumSize(QSize(10000, 10000))
        font2 = QFont()
        font2.setFamilies([u"Courier New"])
        font2.setPointSize(11)
        self.edt_received.setFont(font2)
        self.edt_received.setAutoFillBackground(False)
        self.edt_received.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.edt_received.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.edt_received.setLineWrapMode(QTextEdit.NoWrap)
        self.edt_received.setReadOnly(True)

        self.gridLayout_wnd.addWidget(self.edt_received, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupbox_top.setTitle("")
        self.btn_max_rows.setText("")
        self.btn_uart_settings.setText(QCoreApplication.translate("MainWindow", u"COM3\n"
"115200 8N1", None))
        self.btn_scroll_down.setText("")
        self.btn_hex_received.setText("")
        self.btn_clear.setText("")
        self.btn_uart_switch.setText("")
        self.btn_font.setText("")
        self.groupbox_bottom.setTitle("")
        self.btn_carrier_return.setText("")
        self.btn_line_feed.setText("")
        self.btn_hex_sent.setText("")
        self.edt_received.setMarkdown("")
        self.edt_received.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.edt_received.setPlaceholderText("")
    # retranslateUi
