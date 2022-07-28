# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_uart_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLayout, QSizePolicy, QSpacerItem, QWidget)

class Ui_UartSettingsWindow(object):
    def setupUi(self, UartSettingsWindow):
        if not UartSettingsWindow.objectName():
            UartSettingsWindow.setObjectName(u"UartSettingsWindow")
        UartSettingsWindow.setEnabled(True)
        UartSettingsWindow.resize(156, 83)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UartSettingsWindow.sizePolicy().hasHeightForWidth())
        UartSettingsWindow.setSizePolicy(sizePolicy)
        UartSettingsWindow.setMinimumSize(QSize(152, 77))
        UartSettingsWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(6)
        UartSettingsWindow.setFont(font)
        UartSettingsWindow.setWindowTitle(u"")
        self.gridLayout = QGridLayout(UartSettingsWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.label_uart_baud = QLabel(UartSettingsWindow)
        self.label_uart_baud.setObjectName(u"label_uart_baud")
        self.label_uart_baud.setFont(font)
        self.label_uart_baud.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_uart_baud, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(10, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.label_uart_oddbit = QLabel(UartSettingsWindow)
        self.label_uart_oddbit.setObjectName(u"label_uart_oddbit")
        self.label_uart_oddbit.setFont(font)
        self.label_uart_oddbit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_uart_oddbit, 5, 0, 1, 1)

        self.label_uart_name = QLabel(UartSettingsWindow)
        self.label_uart_name.setObjectName(u"label_uart_name")
        self.label_uart_name.setFont(font)
        self.label_uart_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_uart_name, 1, 0, 1, 1)

        self.comboBox_uart_name = QComboBox(UartSettingsWindow)
        self.comboBox_uart_name.setObjectName(u"comboBox_uart_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_uart_name.sizePolicy().hasHeightForWidth())
        self.comboBox_uart_name.setSizePolicy(sizePolicy1)
        self.comboBox_uart_name.setMinimumSize(QSize(120, 14))
        self.comboBox_uart_name.setMaximumSize(QSize(120, 14))
        self.comboBox_uart_name.setBaseSize(QSize(120, 14))
        self.comboBox_uart_name.setFont(font)
        self.comboBox_uart_name.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_uart_name, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.comboBox_uart_baud = QComboBox(UartSettingsWindow)
        self.comboBox_uart_baud.setObjectName(u"comboBox_uart_baud")
        sizePolicy1.setHeightForWidth(self.comboBox_uart_baud.sizePolicy().hasHeightForWidth())
        self.comboBox_uart_baud.setSizePolicy(sizePolicy1)
        self.comboBox_uart_baud.setMinimumSize(QSize(100, 14))
        self.comboBox_uart_baud.setMaximumSize(QSize(100, 14))
        self.comboBox_uart_baud.setBaseSize(QSize(100, 21))
        self.comboBox_uart_baud.setFont(font)
        self.comboBox_uart_baud.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_uart_baud, 2, 1, 1, 1)

        self.label_uart_databit = QLabel(UartSettingsWindow)
        self.label_uart_databit.setObjectName(u"label_uart_databit")
        self.label_uart_databit.setFont(font)
        self.label_uart_databit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_uart_databit, 3, 0, 1, 1)

        self.label_uart_stopbit = QLabel(UartSettingsWindow)
        self.label_uart_stopbit.setObjectName(u"label_uart_stopbit")
        self.label_uart_stopbit.setFont(font)
        self.label_uart_stopbit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_uart_stopbit, 6, 0, 1, 1)

        self.comboBox_uart_databit = QComboBox(UartSettingsWindow)
        self.comboBox_uart_databit.setObjectName(u"comboBox_uart_databit")
        sizePolicy1.setHeightForWidth(self.comboBox_uart_databit.sizePolicy().hasHeightForWidth())
        self.comboBox_uart_databit.setSizePolicy(sizePolicy1)
        self.comboBox_uart_databit.setMinimumSize(QSize(50, 14))
        self.comboBox_uart_databit.setMaximumSize(QSize(50, 14))
        self.comboBox_uart_databit.setFont(font)
        self.comboBox_uart_databit.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_uart_databit, 3, 1, 1, 1)

        self.comboBox_uart_oddbit = QComboBox(UartSettingsWindow)
        self.comboBox_uart_oddbit.setObjectName(u"comboBox_uart_oddbit")
        sizePolicy1.setHeightForWidth(self.comboBox_uart_oddbit.sizePolicy().hasHeightForWidth())
        self.comboBox_uart_oddbit.setSizePolicy(sizePolicy1)
        self.comboBox_uart_oddbit.setMinimumSize(QSize(50, 14))
        self.comboBox_uart_oddbit.setMaximumSize(QSize(50, 14))
        self.comboBox_uart_oddbit.setFont(font)

        self.gridLayout.addWidget(self.comboBox_uart_oddbit, 5, 1, 1, 1)

        self.comboBox_uart_stopbit = QComboBox(UartSettingsWindow)
        self.comboBox_uart_stopbit.setObjectName(u"comboBox_uart_stopbit")
        sizePolicy1.setHeightForWidth(self.comboBox_uart_stopbit.sizePolicy().hasHeightForWidth())
        self.comboBox_uart_stopbit.setSizePolicy(sizePolicy1)
        self.comboBox_uart_stopbit.setMinimumSize(QSize(50, 14))
        self.comboBox_uart_stopbit.setMaximumSize(QSize(50, 14))
        self.comboBox_uart_stopbit.setFont(font)
        self.comboBox_uart_stopbit.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_uart_stopbit, 6, 1, 1, 1)


        self.retranslateUi(UartSettingsWindow)

        self.comboBox_uart_name.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(UartSettingsWindow)
    # setupUi

    def retranslateUi(self, UartSettingsWindow):
        self.label_uart_baud.setText(QCoreApplication.translate("UartSettingsWindow", u"Baud:", None))
        self.label_uart_oddbit.setText(QCoreApplication.translate("UartSettingsWindow", u"Parity:", None))
        self.label_uart_name.setText(QCoreApplication.translate("UartSettingsWindow", u"Name:", None))
        self.comboBox_uart_name.setCurrentText("")
        self.label_uart_databit.setText(QCoreApplication.translate("UartSettingsWindow", u"Data:", None))
        self.label_uart_stopbit.setText(QCoreApplication.translate("UartSettingsWindow", u"Stop:", None))
        pass
    # retranslateUi

