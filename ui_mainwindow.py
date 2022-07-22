# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(615, 484)
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
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

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
        icon = QIcon()
        icon.addFile(u"resources/start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_uart_switch.setIcon(icon)
        self.btn_uart_switch.setIconSize(QSize(18, 18))
        self.btn_uart_switch.setFlat(True)

        self.gridLayout.addWidget(self.btn_uart_switch, 0, 1, 1, 1)

        self.btn_uart_settings = QPushButton(self.centralwidget)
        self.btn_uart_settings.setObjectName(u"btn_uart_settings")
        sizePolicy1.setHeightForWidth(self.btn_uart_settings.sizePolicy().hasHeightForWidth())
        self.btn_uart_settings.setSizePolicy(sizePolicy1)
        self.btn_uart_settings.setMinimumSize(QSize(55, 24))
        self.btn_uart_settings.setMaximumSize(QSize(55, 24))
        self.btn_uart_settings.setSizeIncrement(QSize(1, 1))
        self.btn_uart_settings.setBaseSize(QSize(55, 24))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(6)
        self.btn_uart_settings.setFont(font)
        self.btn_uart_settings.setStyleSheet(u"text-align: left; vertical-align: middle ;padding: 2px 2px 2px 2px; ")
        self.btn_uart_settings.setIconSize(QSize(0, 0))
        self.btn_uart_settings.setCheckable(True)
        self.btn_uart_settings.setFlat(True)

        self.gridLayout.addWidget(self.btn_uart_settings, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(10000, 10000))
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(11)
        self.textEdit.setFont(font1)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_uart_switch.setText("")
        self.btn_uart_settings.setText(QCoreApplication.translate("MainWindow", u"COM3\n"
"115200 8N1", None))
        self.textEdit.setMarkdown("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText("")
    # retranslateUi

