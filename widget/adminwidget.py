from PySide6.QtWidgets import QWidget
from lib.share import SI
# 使用带搜索控件的 UI 版本
from widget.ui_adminwidget_mode import Ui_AdminWidget


class AdminWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_AdminWidget()
        self.__ui.setupUi(self)
        self.__ui.m_addBookButton.clicked.connect(self.addBook)
        self.__ui.m_logoutButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(0))
        # 连接搜索按钮（pushButton 与 lineEdit 来自 adminwidget_mode.ui）
        if hasattr(self.__ui, 'pushButton') and hasattr(self.__ui, 'lineEdit'):
            self.__ui.pushButton.clicked.connect(self.search)

    def addBook(self):
        SI.g_mainWindow.setCurrentIndex(6)

    def search(self):
        keyword = self.__ui.lineEdit.text().strip()
        self.__ui.m_bookInfoView.updateData(keyword if keyword else None)

    def updateData(self):
        # 默认刷新显示全部
        self.__ui.m_bookInfoView.updateData()