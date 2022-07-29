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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)

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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.btn_uart_switch = QPushButton(self.centralwidget)
        self.btn_uart_switch.setObjectName(u"btn_uart_switch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_uart_switch.sizePolicy().hasHeightForWidth())
        self.btn_uart_switch.setSizePolicy(sizePolicy1)
        self.btn_uart_switch.setMinimumSize(QSize(24, 24))
        self.btn_uart_switch.setMaximumSize(QSize(24, 24))
        self.btn_uart_switch.setBaseSize(QSize(24, 24))
        self.btn_uart_switch.setStyleSheet(u"padding: 2px;")
        icon1 = QIcon()
        icon1.addFile(u"resources/start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_uart_switch.setIcon(icon1)
        self.btn_uart_switch.setIconSize(QSize(18, 18))
        self.btn_uart_switch.setFlat(True)

        self.gridLayout.addWidget(self.btn_uart_switch, 0, 1, 1, 1)

        self.btn_font = QPushButton(self.centralwidget)
        self.btn_font.setObjectName(u"btn_font")
        sizePolicy1.setHeightForWidth(self.btn_font.sizePolicy().hasHeightForWidth())
        self.btn_font.setSizePolicy(sizePolicy1)
        self.btn_font.setMinimumSize(QSize(24, 24))
        self.btn_font.setMaximumSize(QSize(24, 24))
        icon2 = QIcon()
        icon2.addFile(u"resources/font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_font.setIcon(icon2)
        self.btn_font.setIconSize(QSize(18, 18))
        self.btn_font.setCheckable(True)
        self.btn_font.setFlat(True)

        self.gridLayout.addWidget(self.btn_font, 0, 8, 1, 1)

        self.btn_uart_clear = QPushButton(self.centralwidget)
        self.btn_uart_clear.setObjectName(u"btn_uart_clear")
        sizePolicy1.setHeightForWidth(self.btn_uart_clear.sizePolicy().hasHeightForWidth())
        self.btn_uart_clear.setSizePolicy(sizePolicy1)
        self.btn_uart_clear.setMinimumSize(QSize(24, 24))
        self.btn_uart_clear.setMaximumSize(QSize(24, 24))
        icon3 = QIcon()
        icon3.addFile(u"resources/clear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_uart_clear.setIcon(icon3)
        self.btn_uart_clear.setIconSize(QSize(18, 18))
        self.btn_uart_clear.setFlat(True)

        self.gridLayout.addWidget(self.btn_uart_clear, 0, 4, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Raised)
        self.line_2.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_2, 0, 6, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line, 0, 2, 1, 1)

        self.btn_max_line = QPushButton(self.centralwidget)
        self.btn_max_line.setObjectName(u"btn_max_line")
        sizePolicy1.setHeightForWidth(self.btn_max_line.sizePolicy().hasHeightForWidth())
        self.btn_max_line.setSizePolicy(sizePolicy1)
        self.btn_max_line.setMinimumSize(QSize(24, 24))
        self.btn_max_line.setMaximumSize(QSize(24, 24))
        icon4 = QIcon()
        icon4.addFile(u"resources/max_line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_max_line.setIcon(icon4)
        self.btn_max_line.setIconSize(QSize(18, 18))
        self.btn_max_line.setCheckable(True)
        self.btn_max_line.setFlat(True)

        self.gridLayout.addWidget(self.btn_max_line, 0, 7, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(10000, 10000))
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 10)

        self.btn_screen_down = QPushButton(self.centralwidget)
        self.btn_screen_down.setObjectName(u"btn_screen_down")
        sizePolicy1.setHeightForWidth(self.btn_screen_down.sizePolicy().hasHeightForWidth())
        self.btn_screen_down.setSizePolicy(sizePolicy1)
        self.btn_screen_down.setMinimumSize(QSize(24, 24))
        self.btn_screen_down.setMaximumSize(QSize(24, 24))
        icon5 = QIcon()
        icon5.addFile(u"resources/down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_screen_down.setIcon(icon5)
        self.btn_screen_down.setIconSize(QSize(18, 18))
        self.btn_screen_down.setCheckable(True)
        self.btn_screen_down.setChecked(True)
        self.btn_screen_down.setFlat(True)

        self.gridLayout.addWidget(self.btn_screen_down, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 9, 1, 1)

        self.btn_uart_settings = QPushButton(self.centralwidget)
        self.btn_uart_settings.setObjectName(u"btn_uart_settings")
        sizePolicy1.setHeightForWidth(self.btn_uart_settings.sizePolicy().hasHeightForWidth())
        self.btn_uart_settings.setSizePolicy(sizePolicy1)
        self.btn_uart_settings.setMinimumSize(QSize(70, 24))
        self.btn_uart_settings.setMaximumSize(QSize(70, 24))
        self.btn_uart_settings.setSizeIncrement(QSize(0, 0))
        self.btn_uart_settings.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(6)
        self.btn_uart_settings.setFont(font1)
        self.btn_uart_settings.setStyleSheet(u"text-align: left; vertical-align: middle ;padding: 2px 2px 2px 2px; ")
        self.btn_uart_settings.setIconSize(QSize(0, 0))
        self.btn_uart_settings.setCheckable(True)
        self.btn_uart_settings.setFlat(True)

        self.gridLayout.addWidget(self.btn_uart_settings, 0, 0, 1, 1)

        self.btn_hex = QPushButton(self.centralwidget)
        self.btn_hex.setObjectName(u"btn_hex")
        sizePolicy1.setHeightForWidth(self.btn_hex.sizePolicy().hasHeightForWidth())
        self.btn_hex.setSizePolicy(sizePolicy1)
        self.btn_hex.setMinimumSize(QSize(24, 24))
        self.btn_hex.setMaximumSize(QSize(24, 24))
        icon6 = QIcon()
        icon6.addFile(u"resources/hex.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_hex.setIcon(icon6)
        self.btn_hex.setIconSize(QSize(18, 18))
        self.btn_hex.setCheckable(True)
        self.btn_hex.setFlat(True)

        self.gridLayout.addWidget(self.btn_hex, 0, 5, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_uart_switch.setText("")
        self.btn_font.setText("")
        self.btn_uart_clear.setText("")
        self.btn_max_line.setText("")
        self.textEdit.setMarkdown("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText("")
        self.btn_screen_down.setText("")
        self.btn_uart_settings.setText(QCoreApplication.translate("MainWindow", u"COM3\n"
"115200 8N1", None))
        self.btn_hex.setText("")
    # retranslateUi

