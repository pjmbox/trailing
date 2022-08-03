# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_aliases.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QListWidget, QListWidgetItem, QSizePolicy, QWidget)

class Ui_Aliases(object):
    def setupUi(self, Aliases):
        if not Aliases.objectName():
            Aliases.setObjectName(u"Aliases")
        Aliases.resize(447, 183)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Aliases.sizePolicy().hasHeightForWidth())
        Aliases.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(7)
        Aliases.setFont(font)
        Aliases.setWindowTitle(u"")
        self.horizontalLayout = QHBoxLayout(Aliases)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.list_aliases = QListWidget(Aliases)
        self.list_aliases.setObjectName(u"list_aliases")
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(9)
        self.list_aliases.setFont(font1)
        self.list_aliases.setFrameShape(QFrame.NoFrame)
        self.list_aliases.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout.addWidget(self.list_aliases)


        self.retranslateUi(Aliases)

        QMetaObject.connectSlotsByName(Aliases)
    # setupUi

    def retranslateUi(self, Aliases):
        pass
    # retranslateUi

