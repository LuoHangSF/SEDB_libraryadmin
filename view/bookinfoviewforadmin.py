from typing import Optional
from PySide6.QtWidgets import QTableView, QPushButton, QMessageBox, QHeaderView, QWidget
from PySide6.QtCore import Qt

from lib.share import SI
from database.connector import Connector
from model.bookinfomodel import BookInfoModel


class BookInfoViewForAdmin(QTableView):

    def __init__(self, parent=None):
        """
        兼容 UI 构造处传入“类而非实例”的错误：
        - 如果 parent 是 QWidget 的实例，则使用它作为父对象（正常显示到布局中）
        - 否则（例如传的是 AdminWidget 类），则降级为无父对象，避免 TypeError
        """
        real_parent = parent if isinstance(parent, QWidget) else None
        super().__init__(real_parent)

        # 视图基础设置
        self.verticalHeader().setVisible(False)

        # 绑定模型并刷新
        self.__model = BookInfoModel.getInstance()
        self.setModel(self.__model)
        self.__model.update()

        # 列宽策略
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setStretchLastSection(False)

        # 书号现在就是第 1 列（索引 0），这里的移动等价于“不动”
        self._move_book_id_column_to_front(book_id_col=0)

        # 构建“淘汰”按钮列
        self._build_eliminate_buttons()

    def _move_book_id_column_to_front(self, book_id_col: int):
        try:
            if 0 <= book_id_col < self.__model.columnCount() and book_id_col != 0:
                self.horizontalHeader().moveSection(book_id_col, 0)
        except Exception:
            # 某些模型/视图不支持移动，忽略即可
            pass

    def _build_eliminate_buttons(self):
        last_col = self.__model.columnCount() - 1
        for i in range(self.__model.rowCount()):
            btn = QPushButton('淘汰')
            btn.setStyleSheet('background-color: red; color: white; border-radius: 6px; padding: 4px 10px;')
            btn.setCursor(Qt.PointingHandCursor)
            btn.setWhatsThis(str(i))
            btn.clicked.connect(self.deleteBook)
            self.setIndexWidget(self.__model.index(i, last_col), btn)
        # 给按钮列一个固定宽度，减少叠压
        try:
            self.setColumnWidth(last_col, 100)
        except Exception:
            pass

    def deleteBook(self):
        ret = QMessageBox.question(self, '确认淘汰', '确认淘汰这本书吗？')
        if ret != QMessageBox.StandardButton.Yes:
            return

        row_index = int(self.sender().whatsThis())
        # 书号现为索引 0，且为字符串
        book_id = str(self.__model.index(row_index, 0).data()).strip()

        # 先清借阅，再淘汰（删除）书籍
        cursor = Connector.get_cursor()
        sql = 'DELETE FROM borrow WHERE b_id = %s'
        cursor.execute(sql, (book_id,))
        sql = 'DELETE FROM book WHERE book_id = %s'
        cursor.execute(sql, (book_id,))
        Connector.get_connection()

        QMessageBox.information(self, '淘汰成功', '淘汰成功')
        self.updateData()

    def updateData(self, keyword: Optional[str] = None):
        self.__model.update(keyword)
        # 数据刷新后重建按钮列（防止索引失效）
        self._build_eliminate_buttons()