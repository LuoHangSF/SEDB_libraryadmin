# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'readerloginwidget_mode.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_ReaderLoginWidget(object):
    def setupUi(self, ReaderLoginWidget):
        if not ReaderLoginWidget.objectName():
            ReaderLoginWidget.setObjectName(u"ReaderLoginWidget")
        ReaderLoginWidget.resize(591, 456)
        self.label_3 = QLabel(ReaderLoginWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 70, 84, 26))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.m_returnButton_2 = QPushButton(ReaderLoginWidget)
        self.m_returnButton_2.setObjectName(u"m_returnButton_2")
        self.m_returnButton_2.setGeometry(QRect(60, 360, 75, 24))
        self.m_accountLineEdit = QLineEdit(ReaderLoginWidget)
        self.m_accountLineEdit.setObjectName(u"m_accountLineEdit")
        self.m_accountLineEdit.setGeometry(QRect(240, 158, 132, 20))
        self.label = QLabel(ReaderLoginWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(193, 158, 41, 20))
        self.label_2 = QLabel(ReaderLoginWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(198, 250, 36, 16))
        self.m_passwordLineEdit = QLineEdit(ReaderLoginWidget)
        self.m_passwordLineEdit.setObjectName(u"m_passwordLineEdit")
        self.m_passwordLineEdit.setGeometry(QRect(240, 250, 132, 20))
        self.m_passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.m_loginButton = QPushButton(ReaderLoginWidget)
        self.m_loginButton.setObjectName(u"m_loginButton")
        self.m_loginButton.setGeometry(QRect(186, 360, 75, 24))
        self.m_registerButton = QPushButton(ReaderLoginWidget)
        self.m_registerButton.setObjectName(u"m_registerButton")
        self.m_registerButton.setGeometry(QRect(313, 360, 75, 24))
        self.m_returnButton = QPushButton(ReaderLoginWidget)
        self.m_returnButton.setObjectName(u"m_returnButton")
        self.m_returnButton.setGeometry(QRect(440, 360, 75, 24))

        self.retranslateUi(ReaderLoginWidget)

        QMetaObject.connectSlotsByName(ReaderLoginWidget)
    # setupUi

    def retranslateUi(self, ReaderLoginWidget):
        ReaderLoginWidget.setWindowTitle(QCoreApplication.translate("ReaderLoginWidget", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u8bfb\u8005\u767b\u5f55", None))
        self.m_returnButton_2.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u4eba\u8138\u767b\u5f55", None))
        self.m_accountLineEdit.setText("")
        self.label.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u624b\u673a\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u5bc6\u7801\uff1a", None))
        self.m_passwordLineEdit.setText("")
        self.m_loginButton.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u767b\u5f55", None))
        self.m_registerButton.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u6ce8\u518c", None))
        self.m_returnButton.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u8fd4\u56de", None))
    # retranslateUi

