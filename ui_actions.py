# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_actions.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Actions(object):
    def setupUi(self, Actions):
        if not Actions.objectName():
            Actions.setObjectName(u"Actions")
        Actions.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Actions)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 1, 2, 2)
        self.groupbox_upper = QGroupBox(Actions)
        self.groupbox_upper.setObjectName(u"groupbox_upper")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_upper.sizePolicy().hasHeightForWidth())
        self.groupbox_upper.setSizePolicy(sizePolicy)
        self.groupbox_upper.setMinimumSize(QSize(0, 24))
        self.groupbox_upper.setMaximumSize(QSize(16777215, 24))
        self.groupbox_upper.setStyleSheet(u"border: none")
        self.groupbox_upper.setFlat(False)
        self.horizontalLayout = QHBoxLayout(self.groupbox_upper)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cmb_select = QComboBox(self.groupbox_upper)
        self.cmb_select.setObjectName(u"cmb_select")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cmb_select.sizePolicy().hasHeightForWidth())
        self.cmb_select.setSizePolicy(sizePolicy1)
        self.cmb_select.setMinimumSize(QSize(150, 18))
        self.cmb_select.setMaximumSize(QSize(150, 18))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        self.cmb_select.setFont(font)
        self.cmb_select.setAutoFillBackground(False)
        self.cmb_select.setStyleSheet(u"border: 1px solid grey;")
        self.cmb_select.setFrame(False)

        self.horizontalLayout.addWidget(self.cmb_select)

        self.btn_switch = QPushButton(self.groupbox_upper)
        self.btn_switch.setObjectName(u"btn_switch")
        sizePolicy1.setHeightForWidth(self.btn_switch.sizePolicy().hasHeightForWidth())
        self.btn_switch.setSizePolicy(sizePolicy1)
        self.btn_switch.setMinimumSize(QSize(24, 24))
        self.btn_switch.setMaximumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u"resources/start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_switch.setIcon(icon)
        self.btn_switch.setIconSize(QSize(18, 18))
        self.btn_switch.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_switch)

        self.btn_refresh = QPushButton(self.groupbox_upper)
        self.btn_refresh.setObjectName(u"btn_refresh")
        sizePolicy1.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy1)
        self.btn_refresh.setMinimumSize(QSize(24, 24))
        self.btn_refresh.setMaximumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u"resources/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon1)
        self.btn_refresh.setIconSize(QSize(16, 16))
        self.btn_refresh.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_refresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.groupbox_upper)

        self.groupbox_bottom = QGroupBox(Actions)
        self.groupbox_bottom.setObjectName(u"groupbox_bottom")

        self.verticalLayout.addWidget(self.groupbox_bottom)


        self.retranslateUi(Actions)

        QMetaObject.connectSlotsByName(Actions)
    # setupUi

    def retranslateUi(self, Actions):
        Actions.setWindowTitle(QCoreApplication.translate("Actions", u"Form", None))
        self.groupbox_upper.setTitle("")
        self.btn_switch.setText("")
        self.btn_refresh.setText("")
        self.groupbox_bottom.setTitle(QCoreApplication.translate("Actions", u"GroupBox", None))
    # retranslateUi

