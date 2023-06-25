# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_history.ui'
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

class Ui_History(object):
    def setupUi(self, History):
        if not History.objectName():
            History.setObjectName(u"History")
        History.resize(468, 238)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(History.sizePolicy().hasHeightForWidth())
        History.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(7)
        History.setFont(font)
        History.setWindowTitle(u"")
        self.horizontalLayout = QHBoxLayout(History)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.list_history = QListWidget(History)
        self.list_history.setObjectName(u"list_history")
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(9)
        self.list_history.setFont(font1)
        self.list_history.setFrameShape(QFrame.NoFrame)
        self.list_history.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout.addWidget(self.list_history)


        self.retranslateUi(History)

        QMetaObject.connectSlotsByName(History)
    # setupUi

    def retranslateUi(self, History):
        pass
    # retranslateUi

