from PySide6.QtWidgets import QTableView, QPushButton, QHeaderView, QListWidget, QMessageBox
from lib.share import SI
from database.connector import Connector
from model.userinfomodel import UserInfoModel


class UserInfoView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__showBorrowWidget = None
        self.verticalHeader().setVisible(False)
        self.__model = UserInfoModel()
        self.setModel(self.__model)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        # 在“查看已借阅书籍”那一列放按钮（列索引 6）
        show_button = QPushButton('查看已借阅书籍')
        self.setIndexWidget(self.__model.index(0, 6), show_button)
        show_button.setStyleSheet('min-width: 100px; max-width: 100px;')
        show_button.clicked.connect(self.showBorrow)

    def showBorrow(self):
        if SI.g_userId is None:
            QMessageBox.information(self, '提示', '尚未登录')
            return

        cursor = Connector.get_cursor()
        # 修改：使用 phone_number 关联 borrow 表
        sql = """
            SELECT b.b_name
            FROM borrow br
            JOIN book b ON b.book_id = br.b_id
            WHERE br.phone_number = %s
        """
        cursor.execute(sql, (SI.g_userId,))
        result = cursor.fetchall()

        self.__showBorrowWidget = QListWidget()
        self.__showBorrowWidget.setWindowTitle('借阅书籍目录')
        for item in result:
            self.__showBorrowWidget.addItem(item[0])
        self.__showBorrowWidget.show()

    def updateData(self):
        self.__model.update()
        # 重新挂按钮（防止模型刷新导致按钮丢失）
        show_button = QPushButton('查看已借阅书籍')
        show_button.setStyleSheet('min-width: 100px; max-width: 100px;')
        show_button.clicked.connect(self.showBorrow)
        self.setIndexWidget(self.__model.index(0, 6), show_button)