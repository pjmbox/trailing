# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_gui_max_rows.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_gui_settings_max_rows(object):
    def setupUi(self, gui_settings_max_rows):
        if not gui_settings_max_rows.objectName():
            gui_settings_max_rows.setObjectName(u"gui_settings_max_rows")
        gui_settings_max_rows.resize(111, 22)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gui_settings_max_rows.sizePolicy().hasHeightForWidth())
        gui_settings_max_rows.setSizePolicy(sizePolicy)
        gui_settings_max_rows.setMinimumSize(QSize(111, 22))
        gui_settings_max_rows.setMaximumSize(QSize(111, 22))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(6)
        gui_settings_max_rows.setFont(font)
        self.formLayout = QFormLayout(gui_settings_max_rows)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(1)
        self.formLayout.setVerticalSpacing(1)
        self.formLayout.setContentsMargins(1, 1, 1, 1)
        self.label = QLabel(gui_settings_max_rows)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(45, 18))
        self.label.setMaximumSize(QSize(45, 18))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.edt_max_rows = QLineEdit(gui_settings_max_rows)
        self.edt_max_rows.setObjectName(u"edt_max_rows")
        sizePolicy.setHeightForWidth(self.edt_max_rows.sizePolicy().hasHeightForWidth())
        self.edt_max_rows.setSizePolicy(sizePolicy)
        self.edt_max_rows.setMinimumSize(QSize(60, 18))
        self.edt_max_rows.setMaximumSize(QSize(60, 18))
        self.edt_max_rows.setFont(font)
        self.edt_max_rows.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edt_max_rows)


        self.retranslateUi(gui_settings_max_rows)

        QMetaObject.connectSlotsByName(gui_settings_max_rows)
    # setupUi

    def retranslateUi(self, gui_settings_max_rows):
        gui_settings_max_rows.setWindowTitle(QCoreApplication.translate("gui_settings_max_rows", u"Form", None))
        self.label.setText(QCoreApplication.translate("gui_settings_max_rows", u"Max rows:", None))
    # retranslateUi

