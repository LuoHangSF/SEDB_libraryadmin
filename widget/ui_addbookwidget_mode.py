# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addbookwidget_mode.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDoubleSpinBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_AddBookWidget(object):
    def setupUi(self, AddBookWidget):
        if not AddBookWidget.objectName():
            AddBookWidget.setObjectName(u"AddBookWidget")
        AddBookWidget.resize(675, 389)
        self.label_7 = QLabel(AddBookWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(218, 240, 81, 16))
        self.m_publishDateEdit_2 = QDateEdit(AddBookWidget)
        self.m_publishDateEdit_2.setObjectName(u"m_publishDateEdit_2")
        self.m_publishDateEdit_2.setGeometry(QRect(330, 240, 88, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_publishDateEdit_2.sizePolicy().hasHeightForWidth())
        self.m_publishDateEdit_2.setSizePolicy(sizePolicy)
        self.label_6 = QLabel(AddBookWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 280, 121, 16))
        self.m_titleLineEdit_2 = QLineEdit(AddBookWidget)
        self.m_titleLineEdit_2.setObjectName(u"m_titleLineEdit_2")
        self.m_titleLineEdit_2.setGeometry(QRect(340, 280, 132, 20))
        self.label = QLabel(AddBookWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(222, 42, 36, 16))
        self.m_titleLineEdit = QLineEdit(AddBookWidget)
        self.m_titleLineEdit.setObjectName(u"m_titleLineEdit")
        self.m_titleLineEdit.setGeometry(QRect(310, 42, 132, 20))
        self.label_2 = QLabel(AddBookWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(222, 80, 36, 16))
        self.m_authorLineEdit = QLineEdit(AddBookWidget)
        self.m_authorLineEdit.setObjectName(u"m_authorLineEdit")
        self.m_authorLineEdit.setGeometry(QRect(310, 80, 132, 20))
        self.label_3 = QLabel(AddBookWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(218, 200, 60, 16))
        self.m_publishDateEdit = QDateEdit(AddBookWidget)
        self.m_publishDateEdit.setObjectName(u"m_publishDateEdit")
        self.m_publishDateEdit.setGeometry(QRect(330, 200, 88, 20))
        sizePolicy.setHeightForWidth(self.m_publishDateEdit.sizePolicy().hasHeightForWidth())
        self.m_publishDateEdit.setSizePolicy(sizePolicy)
        self.m_publishLineEdit = QLineEdit(AddBookWidget)
        self.m_publishLineEdit.setObjectName(u"m_publishLineEdit")
        self.m_publishLineEdit.setGeometry(QRect(310, 120, 132, 20))
        self.label_4 = QLabel(AddBookWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 120, 48, 16))
        self.m_priceSpinBox = QDoubleSpinBox(AddBookWidget)
        self.m_priceSpinBox.setObjectName(u"m_priceSpinBox")
        self.m_priceSpinBox.setGeometry(QRect(308, 160, 53, 20))
        sizePolicy.setHeightForWidth(self.m_priceSpinBox.sizePolicy().hasHeightForWidth())
        self.m_priceSpinBox.setSizePolicy(sizePolicy)
        self.label_5 = QLabel(AddBookWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 160, 36, 16))
        self.m_addButton = QPushButton(AddBookWidget)
        self.m_addButton.setObjectName(u"m_addButton")
        self.m_addButton.setGeometry(QRect(216, 333, 75, 24))
        self.m_returnButton = QPushButton(AddBookWidget)
        self.m_returnButton.setObjectName(u"m_returnButton")
        self.m_returnButton.setGeometry(QRect(343, 333, 75, 24))

        self.retranslateUi(AddBookWidget)

        QMetaObject.connectSlotsByName(AddBookWidget)
    # setupUi

    def retranslateUi(self, AddBookWidget):
        AddBookWidget.setWindowTitle(QCoreApplication.translate("AddBookWidget", u"\u6dfb\u52a0\u65b0\u4e66", None))
        self.label_7.setText(QCoreApplication.translate("AddBookWidget", u"\u91c7\u8d2d\u5165\u5e93\u65e5\u671f\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("AddBookWidget", u"\u4e66\u53f7-\u7559\u7a7a\u5219\u81ea\u52a8\u751f\u6210\uff1a", None))
        self.label.setText(QCoreApplication.translate("AddBookWidget", u"\u4e66\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("AddBookWidget", u"\u4f5c\u8005\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("AddBookWidget", u"\u51fa\u7248\u65e5\u671f\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("AddBookWidget", u"\u51fa\u7248\u793e\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("AddBookWidget", u"\u4ef7\u683c\uff1a", None))
        self.m_addButton.setText(QCoreApplication.translate("AddBookWidget", u"\u786e\u8ba4\u6dfb\u52a0", None))
        self.m_returnButton.setText(QCoreApplication.translate("AddBookWidget", u"\u8fd4\u56de", None))
    # retranslateUi

