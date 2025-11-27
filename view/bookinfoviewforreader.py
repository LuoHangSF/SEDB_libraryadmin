from typing import Optional
from PySide6.QtWidgets import QTableView, QPushButton, QMessageBox, QHeaderView

from lib.share import SI
from database.connector import Connector
from model.bookinfomodel import BookInfoModel


class BookInfoViewForReader(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.verticalHeader().setVisible(False)
        self.__model = BookInfoModel.getInstance()
        self.setModel(self.__model)
        self.__model.update()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        for i in range(self.__model.rowCount()):
            borrow_button = QPushButton('借阅/归还')
            borrow_button.setWhatsThis(str(i))
            borrow_button.clicked.connect(self.borrow)
            self.setIndexWidget(self.__model.index(i, self.__model.columnCount() - 1), borrow_button)

    def borrow(self):
        row_index = int(self.sender().whatsThis())
        # book_id = self.__model.index(row_index, 5).data()
        book_id = int(self.__model.index(row_index, 0).data())
        
        cursor = Connector.get_cursor()

        # 根据模型当前显示判断状态（'否' 表示未借出）
        is_borrowed = (self.__model.index(row_index, 4).data() == '是')

        if not is_borrowed:
            # 借阅前检查个人借阅上限
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
            # 插入借阅记录
            sql = 'INSERT INTO borrow (b_id, u_id) VALUES (%s, %s)'
            cursor.execute(sql, (book_id, SI.g_userId))
            Connector.get_connection()
            QMessageBox.information(self, '借阅成功', '借阅成功')
        else:
            # 归还：必须是本人借的
            sql = 'SELECT 1 FROM borrow WHERE u_id = %s AND b_id = %s'
            cursor.execute(sql, (SI.g_userId, book_id))
            if cursor.fetchone() is None:
                QMessageBox.information(self, '归还失败', '这本书是别人借阅的')
                return
            sql = 'DELETE FROM borrow WHERE b_id = %s AND u_id = %s'
            cursor.execute(sql, (book_id, SI.g_userId))
            Connector.get_connection()
            QMessageBox.information(self, '归还成功', '归还成功')

        self.updateData()
        SI.g_userInfoModel.update()

    def updateData(self, keyword: Optional[str] = None):
        self.__model.update(keyword)
        # 重建操作按钮
        for i in range(self.__model.rowCount()):
            borrow_button = QPushButton('借阅/归还')
            borrow_button.setWhatsThis(str(i))
            borrow_button.clicked.connect(self.borrow)
            self.setIndexWidget(self.__model.index(i, self.__model.columnCount() - 1), borrow_button)