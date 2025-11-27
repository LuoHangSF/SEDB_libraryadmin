# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerwidget_mode.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_RegisterWidget(object):
    def setupUi(self, RegisterWidget):
        if not RegisterWidget.objectName():
            RegisterWidget.setObjectName(u"RegisterWidget")
        RegisterWidget.resize(708, 429)
        self.m_mobileLineEdit_2 = QLineEdit(RegisterWidget)
        self.m_mobileLineEdit_2.setObjectName(u"m_mobileLineEdit_2")
        self.m_mobileLineEdit_2.setGeometry(QRect(310, 100, 132, 20))
        self.label_8 = QLabel(RegisterWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 100, 48, 16))
        self.m_registerButton = QPushButton(RegisterWidget)
        self.m_registerButton.setObjectName(u"m_registerButton")
        self.m_registerButton.setGeometry(QRect(216, 374, 75, 24))
        self.m_returnButton = QPushButton(RegisterWidget)
        self.m_returnButton.setObjectName(u"m_returnButton")
        self.m_returnButton.setGeometry(QRect(343, 374, 75, 24))
        self.m_nameLlineEdit = QLineEdit(RegisterWidget)
        self.m_nameLlineEdit.setObjectName(u"m_nameLlineEdit")
        self.m_nameLlineEdit.setGeometry(QRect(308, 51, 132, 20))
        self.label = QLabel(RegisterWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 51, 36, 16))
        self.m_mobileLineEdit = QLineEdit(RegisterWidget)
        self.m_mobileLineEdit.setObjectName(u"m_mobileLineEdit")
        self.m_mobileLineEdit.setGeometry(QRect(310, 149, 132, 20))
        self.label_3 = QLabel(RegisterWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 149, 48, 16))
        self.label_5 = QLabel(RegisterWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(222, 200, 36, 16))
        self.m_roleComboBox = QComboBox(RegisterWidget)
        self.m_roleComboBox.addItem("")
        self.m_roleComboBox.addItem("")
        self.m_roleComboBox.addItem("")
        self.m_roleComboBox.addItem("")
        self.m_roleComboBox.setObjectName(u"m_roleComboBox")
        self.m_roleComboBox.setGeometry(QRect(310, 200, 62, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_roleComboBox.sizePolicy().hasHeightForWidth())
        self.m_roleComboBox.setSizePolicy(sizePolicy)
        self.label_6 = QLabel(RegisterWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(222, 250, 36, 16))
        self.m_passwordLineEdit = QLineEdit(RegisterWidget)
        self.m_passwordLineEdit.setObjectName(u"m_passwordLineEdit")
        self.m_passwordLineEdit.setGeometry(QRect(310, 250, 132, 20))
        self.m_passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.label_7 = QLabel(RegisterWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(218, 300, 60, 16))
        self.m_passwordConfirmLineEdit = QLineEdit(RegisterWidget)
        self.m_passwordConfirmLineEdit.setObjectName(u"m_passwordConfirmLineEdit")
        self.m_passwordConfirmLineEdit.setGeometry(QRect(310, 300, 132, 20))
        self.m_passwordConfirmLineEdit.setEchoMode(QLineEdit.Password)

        self.retranslateUi(RegisterWidget)

        QMetaObject.connectSlotsByName(RegisterWidget)
    # setupUi

    def retranslateUi(self, RegisterWidget):
        RegisterWidget.setWindowTitle(QCoreApplication.translate("RegisterWidget", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("RegisterWidget", u"\u624b\u673a\u53f7\uff1a", None))
        self.m_registerButton.setText(QCoreApplication.translate("RegisterWidget", u"\u6ce8\u518c", None))
        self.m_returnButton.setText(QCoreApplication.translate("RegisterWidget", u"\u8fd4\u56de", None))
        self.label.setText(QCoreApplication.translate("RegisterWidget", u"\u59d3\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("RegisterWidget", u"email\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("RegisterWidget", u"\u7c7b\u522b\uff1a", None))
        self.m_roleComboBox.setItemText(0, QCoreApplication.translate("RegisterWidget", u"\u6559\u5e08", None))
        self.m_roleComboBox.setItemText(1, QCoreApplication.translate("RegisterWidget", u"\u7814\u7a76\u751f", None))
        self.m_roleComboBox.setItemText(2, QCoreApplication.translate("RegisterWidget", u"\u672c\u79d1\u751f", None))
        self.m_roleComboBox.setItemText(3, QCoreApplication.translate("RegisterWidget", u"\u5176\u4ed6", None))

        self.label_6.setText(QCoreApplication.translate("RegisterWidget", u"\u5bc6\u7801\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("RegisterWidget", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
    # retranslateUi

