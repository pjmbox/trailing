# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_max_rows.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_MaxRows(object):
    def setupUi(self, MaxRows):
        if not MaxRows.objectName():
            MaxRows.setObjectName(u"MaxRows")
        MaxRows.resize(111, 26)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MaxRows.sizePolicy().hasHeightForWidth())
        MaxRows.setSizePolicy(sizePolicy)
        MaxRows.setMinimumSize(QSize(111, 26))
        MaxRows.setMaximumSize(QSize(111, 26))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(6)
        MaxRows.setFont(font)
        self.horizontalLayout = QHBoxLayout(MaxRows)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.label = QLabel(MaxRows)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(45, 18))
        self.label.setMaximumSize(QSize(45, 18))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.edt_max_rows = QLineEdit(MaxRows)
        self.edt_max_rows.setObjectName(u"edt_max_rows")
        sizePolicy.setHeightForWidth(self.edt_max_rows.sizePolicy().hasHeightForWidth())
        self.edt_max_rows.setSizePolicy(sizePolicy)
        self.edt_max_rows.setMinimumSize(QSize(36, 18))
        self.edt_max_rows.setMaximumSize(QSize(36, 18))
        self.edt_max_rows.setFont(font)
        self.edt_max_rows.setMaxLength(6)
        self.edt_max_rows.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.edt_max_rows)

        self.btn_ok = QPushButton(MaxRows)
        self.btn_ok.setObjectName(u"btn_ok")
        sizePolicy.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy)
        self.btn_ok.setMinimumSize(QSize(20, 20))
        self.btn_ok.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u"resources/tick.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ok.setIcon(icon)
        self.btn_ok.setIconSize(QSize(18, 18))
        self.btn_ok.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_ok)


        self.retranslateUi(MaxRows)

        QMetaObject.connectSlotsByName(MaxRows)
    # setupUi

    def retranslateUi(self, MaxRows):
        MaxRows.setWindowTitle(QCoreApplication.translate("MaxRows", u"Form", None))
        self.label.setText(QCoreApplication.translate("MaxRows", u"Max rows:", None))
        self.edt_max_rows.setPlaceholderText(QCoreApplication.translate("MaxRows", u"press return to confirm", None))
        self.btn_ok.setText("")
    # retranslateUi

