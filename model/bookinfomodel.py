from typing import Any, List, Optional
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from database.connector import Connector


class BookInfoModel(QAbstractTableModel):
    """
    书籍信息模型（含是否已借出标记）。
    列顺序与各界面视图保持一致：
    0 书号 (book_id)
    1 书名 (b_name)
    2 作者 (author)
    3 出版社 (publish_name)
    4 价格 (price_str) -> 字符串，保留两位小数
    5 是否已借出 (borrowed_flag) -> '是'/'否'
    6 出版日期 (publish_date_str) -> YYYY-MM-DD 字符串
    7 入库日期 (stock_in_date_str) -> YYYY-MM-DD 字符串
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
        注意：
        - 价格以字符串返回，保留两位小数（CAST(ROUND(price,2) AS CHAR)）。
        - 日期用 CONCAT(YEAR/MONTH/DAY) 拼接为 YYYY-MM-DD，避免使用 % 占位符引起 PyMySQL 格式化冲突。
        """
        cursor = Connector.get_cursor()

        base_select = """
            SELECT
                b.book_id,
                b.b_name,
                b.author,
                b.publish_name,
                CAST(ROUND(b.price, 2) AS CHAR) AS price_str,
                CASE WHEN EXISTS (SELECT 1 FROM borrow br WHERE br.b_id = b.book_id) THEN '是' ELSE '否' END AS borrowed_flag,
                CONCAT(
                    YEAR(b.publish_date), '-',
                    LPAD(MONTH(b.publish_date), 2, '0'), '-',
                    LPAD(DAY(b.publish_date), 2, '0')
                ) AS publish_date_str,
                CONCAT(
                    YEAR(b.stock_in_date), '-',
                    LPAD(MONTH(b.stock_in_date), 2, '0'), '-',
                    LPAD(DAY(b.stock_in_date), 2, '0')
                ) AS stock_in_date_str
            FROM book b
        """

        order_by = " ORDER BY b.stock_in_date DESC, b.book_id ASC"

        if keyword is None or keyword.strip() == '':
            sql = base_select + order_by
            cursor.execute(sql)
        else:
            kw = f"%{keyword.strip()}%"
            sql = base_select + """
                WHERE (b.book_id LIKE %s OR b.b_name LIKE %s OR b.author LIKE %s OR b.publish_name LIKE %s)
            """ + order_by
            cursor.execute(sql, (kw, kw, kw, kw))

        rows = cursor.fetchall()

        # 重置模型数据，并将 None 转为空字符串，避免界面显示 None
        self.beginResetModel()
        self.__data = []
        for row in rows:
            book_id, b_name, author, publish_name, price_str, borrowed_flag, pub_date_str, stock_date_str = row
            price_str = '' if price_str is None else price_str
            pub_date_str = '' if pub_date_str is None else pub_date_str
            stock_date_str = '' if stock_date_str is None else stock_date_str
            self.__data.append([
                book_id,
                b_name,
                author,
                publish_name,
                price_str,
                borrowed_flag,
                pub_date_str,
                stock_date_str
            ])
        self.endResetModel()