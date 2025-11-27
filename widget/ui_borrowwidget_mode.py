# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'borrowwidget_mode.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

from view.bookinfoviewforreader import BookInfoViewForReader
from view.userinfoview import UserInfoView

class Ui_BorrowWidget(object):
    def setupUi(self, BorrowWidget):
        if not BorrowWidget.objectName():
            BorrowWidget.setObjectName(u"BorrowWidget")
        BorrowWidget.resize(629, 463)
        self.m_userInfoView = UserInfoView(BorrowWidget)
        self.m_userInfoView.setObjectName(u"m_userInfoView")
        self.m_userInfoView.setGeometry(QRect(9, 9, 613, 100))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_userInfoView.sizePolicy().hasHeightForWidth())
        self.m_userInfoView.setSizePolicy(sizePolicy)
        self.m_userInfoView.setMinimumSize(QSize(0, 100))
        self.m_userInfoView.setMaximumSize(QSize(16777215, 100))
        self.m_bookInfoView = BookInfoViewForReader(BorrowWidget)
        self.m_bookInfoView.setObjectName(u"m_bookInfoView")
        self.m_bookInfoView.setGeometry(QRect(9, 187, 611, 261))
        self.pushButton = QPushButton(BorrowWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 150, 75, 24))
        self.lineEdit = QLineEdit(BorrowWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 150, 521, 21))
        self.label = QLabel(BorrowWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 130, 151, 16))
        self.m_logoutButton = QPushButton(BorrowWidget)
        self.m_logoutButton.setObjectName(u"m_logoutButton")
        self.m_logoutButton.setGeometry(QRect(540, 120, 75, 24))
        self.m_logoutButton.setStyleSheet(u"background-color: red; color: white;")

        self.retranslateUi(BorrowWidget)

        QMetaObject.connectSlotsByName(BorrowWidget)
    # setupUi

    def retranslateUi(self, BorrowWidget):
        BorrowWidget.setWindowTitle(QCoreApplication.translate("BorrowWidget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("BorrowWidget", u"\u641c\u7d22", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("BorrowWidget", u"\u627e\u4e0d\u5230\u60f3\u8981\u7684\u4e66\uff1f\u5728\u6b64\u641c\u7d22", None))
        self.m_logoutButton.setText(QCoreApplication.translate("BorrowWidget", u"\u9000\u51fa\u767b\u5f55", None))
    # retranslateUi

