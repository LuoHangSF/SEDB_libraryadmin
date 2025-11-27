from typing import Any, List, Optional
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from database.connector import Connector


class BookInfoModel(QAbstractTableModel):
    """
    书籍信息模型（含是否已借出标记）。
    列顺序：
    0 book_id
    1 书名
    2 作者
    3 出版社
    4 价格
    5 是否已借出 ('是'/'否')
    6 出版日期
    7 入库日期
    """

    __instance = None

    @staticmethod
    def getInstance():
        if BookInfoModel.__instance is None:
            BookInfoModel.__instance = BookInfoModel()
        return BookInfoModel.__instance

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__header = ['书号', '书名', '作者', '出版社', '价格', '是否已借出', '出版日期', '入库日期']
        self.__data: List[List[Any]] = []

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__data)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__header)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if 0 <= section < len(self.__header):
                return self.__header[section]
        return None

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if not index.isValid():
            return None
        if role != Qt.DisplayRole:
            return None
        r, c = index.row(), index.column()
        if r < 0 or r >= len(self.__data) or c < 0 or c >= len(self.__header):
            return None
        return self.__data[r][c]

    def update(self, keyword: Optional[str] = None):
        """
        更新数据；keyword 为 None 或空则显示全部。
        搜索字段：book_id、b_name、author、publish_name。
        """
        cursor = Connector.get_cursor()

        if keyword is None or keyword.strip() == '':
            # 无搜索词：全部
            sql = """
                SELECT
                    b.book_id,
                    b.b_name,
                    b.author,
                    b.publish_name,
                    b.price,
                    CASE WHEN EXISTS (SELECT 1 FROM borrow br WHERE br.b_id = b.book_id) THEN '是' ELSE '否' END AS borrowed_flag,
                    b.publish_date,
                    b.stock_in_date
                FROM book b
                ORDER BY b.stock_in_date DESC, b.book_id ASC
            """
            cursor.execute(sql)
        else:
            kw = f"%{keyword.strip()}%"
            # 加入 book_id 搜索
            sql = """
                SELECT
                    b.book_id,
                    b.b_name,
                    b.author,
                    b.publish_name,
                    b.price,
                    CASE WHEN EXISTS (SELECT 1 FROM borrow br WHERE br.b_id = b.book_id) THEN '是' ELSE '否' END AS borrowed_flag,
                    b.publish_date,
                    b.stock_in_date
                FROM book b
                WHERE (b.book_id LIKE %s OR b.b_name LIKE %s OR b.author LIKE %s OR b.publish_name LIKE %s)
                ORDER BY b.stock_in_date DESC, b.book_id ASC
            """
            cursor.execute(sql, (kw, kw, kw, kw))

        rows = cursor.fetchall()
        self.beginResetModel()
        self.__data = [list(row) for row in rows]
        self.endResetModel()