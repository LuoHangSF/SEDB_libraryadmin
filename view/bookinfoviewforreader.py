from typing import Optional
from PySide6.QtWidgets import QTableView, QPushButton, QMessageBox, QHeaderView

from lib.share import SI
from database.connector import Connector
from model.bookinfomodel import BookInfoModel

# 列索引常量，保持与原模型一致
BOOK_ID_COL = 0         # 书号在第 1 列
BORROWED_FLAG_COL = 5   # “是否已借出”列（内容为 '是' / '否'）


class BookInfoViewForReader(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.verticalHeader().setVisible(False)
        self.__model = BookInfoModel.getInstance()
        self.setModel(self.__model)
        self.__model.update()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # 在最后一列放“借阅/归还”按钮
        for i in range(self.__model.rowCount()):
            borrow_button = QPushButton('借阅/归还')
            borrow_button.setWhatsThis(str(i))
            borrow_button.clicked.connect(self.borrow)
            self.setIndexWidget(self.__model.index(i, self.__model.columnCount() - 1), borrow_button)

    def borrow(self):
        if SI.g_userId is None:
            QMessageBox.information(self, '提示', '请先登录')
            return

        row_index = int(self.sender().whatsThis())
        book_id = str(self.__model.index(row_index, BOOK_ID_COL).data()).strip()

        cursor = Connector.get_cursor()

        # 判断“是否已借出”
        is_borrowed = (str(self.__model.index(row_index, BORROWED_FLAG_COL).data()) == '是')

        if not is_borrowed:
            # 借阅前检查个人借阅上限（借阅数量 / 最大借阅数量）
            if int(SI.g_userInfoModel.index(0, 3).data()) >= int(SI.g_userInfoModel.index(0, 4).data()):
                QMessageBox.information(self, '借阅失败', '已达到最大借阅数量')
                return
            # 再次确认此书当前无人借阅（避免竞态）
            sql = 'SELECT 1 FROM borrow WHERE b_id = %s LIMIT 1'
            cursor.execute(sql, (book_id,))
            if cursor.fetchone() is not None:
                QMessageBox.information(self, '借阅失败', '该书已被借阅')
                self.updateData()
                return
            # 修改：插入借阅记录使用 phone_number
            sql = 'INSERT INTO borrow (b_id, phone_number) VALUES (%s, %s)'
            cursor.execute(sql, (book_id, SI.g_userId))
            Connector.get_connection()
            QMessageBox.information(self, '借阅成功', '借阅成功')
        else:
            # 归还：必须是本人借的
            sql = 'SELECT 1 FROM borrow WHERE phone_number = %s AND b_id = %s'
            cursor.execute(sql, (SI.g_userId, book_id))
            if cursor.fetchone() is None:
                QMessageBox.information(self, '归还失败', '这本书是别人借阅的')
                return
            sql = 'DELETE FROM borrow WHERE b_id = %s AND phone_number = %s'
            cursor.execute(sql, (book_id, SI.g_userId))
            Connector.get_connection()
            QMessageBox.information(self, '归还成功', '归还成功')

        self.updateData()
        SI.g_userInfoModel.update()

    def updateData(self, keyword: Optional[str] = None):
        self.__model.update(keyword)
        # 重建操作按钮（避免模型刷新后索引失效）
        for i in range(self.__model.rowCount()):
            borrow_button = QPushButton('借阅/归还')
            borrow_button.setWhatsThis(str(i))
            borrow_button.clicked.connect(self.borrow)
            self.setIndexWidget(self.__model.index(i, self.__model.columnCount() - 1), borrow_button)