# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminwidget_mode.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

from view.bookinfoviewforadmin import BookInfoViewForAdmin

class Ui_AdminWidget(object):
    def setupUi(self, AdminWidget):
        if not AdminWidget.objectName():
            AdminWidget.setObjectName(u"AdminWidget")
        AdminWidget.resize(631, 464)
        self.m_bookInfoView = BookInfoViewForAdmin(AdminWidget)
        self.m_bookInfoView.setObjectName(u"m_bookInfoView")
        self.m_bookInfoView.setGeometry(QRect(9, 81, 611, 371))
        self.m_logoutButton = QPushButton(AdminWidget)
        self.m_logoutButton.setObjectName(u"m_logoutButton")
        self.m_logoutButton.setGeometry(QRect(550, 10, 75, 24))
        self.m_logoutButton.setStyleSheet(u"background-color: red")
        self.m_addBookButton = QPushButton(AdminWidget)
        self.m_addBookButton.setObjectName(u"m_addBookButton")
        self.m_addBookButton.setGeometry(QRect(460, 10, 75, 24))
        self.lineEdit = QLineEdit(AdminWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 531, 21))
        self.pushButton = QPushButton(AdminWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 50, 75, 24))
        self.label = QLabel(AdminWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 30, 151, 16))
        self.widget = QWidget(AdminWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(AdminWidget)

        QMetaObject.connectSlotsByName(AdminWidget)
    # setupUi

    def retranslateUi(self, AdminWidget):
        AdminWidget.setWindowTitle(QCoreApplication.translate("AdminWidget", u"Form", None))
        self.m_logoutButton.setText(QCoreApplication.translate("AdminWidget", u"\u9000\u51fa\u767b\u5f55", None))
        self.m_addBookButton.setText(QCoreApplication.translate("AdminWidget", u"\u6dfb\u52a0\u4e66\u7c4d", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("AdminWidget", u"\u641c\u7d22", None))
        self.label.setText(QCoreApplication.translate("AdminWidget", u"\u627e\u4e0d\u5230\u60f3\u8981\u7684\u4e66\uff1f\u5728\u6b64\u641c\u7d22", None))
    # retranslateUi

