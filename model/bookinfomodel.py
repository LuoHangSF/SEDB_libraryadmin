from typing import Any, Optional
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex, Qt
from database.connector import Connector
from lib.share import SI


class BookInfoModel(QAbstractTableModel):
    s_instance = None

    @staticmethod
    def getInstance():
        if BookInfoModel.s_instance is None:
            BookInfoModel.s_instance = BookInfoModel()
        return BookInfoModel.s_instance

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__bookInfoList = []
        # 最后一列作为操作列（按钮），内部持有 BookID 用于操作
        self.__headerList = ['标题', '作者', '出版日期', '出版社', '是否已借出', '借阅/归还']
        SI.g_bookInfoModel = self
        self.update()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if 0 <= section < len(self.__headerList):
                return self.__headerList[section]
        return super().headerData(section, orientation, role)

    def rowCount(self, parent: [QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__bookInfoList)

    def columnCount(self, parent: [QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__headerList)

    def data(self, index: [QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if 0 <= index.column() < len(self.__headerList) and 0 <= index.row() < len(self.__bookInfoList):
            return self.__bookInfoList[index.row()][index.column()]
        return None

    def sort(self, column: int, order: Qt.SortOrder = ...) -> None:
        self.__bookInfoList.sort(key=lambda row: row[column], reverse=order == Qt.SortOrder.DescendingOrder)
        if self.__bookInfoList:
            self.dataChanged.emit(self.index(0, 0), self.index(len(self.__bookInfoList) - 1, len(self.__headerList) - 1))

    def update(self, keyword: Optional[str] = None):
        """
        更新数据。
        keyword: 若提供，则在 书名(b_name)、作者(author)、出版社(publish_name) 三个字段上做 LIKE 匹配。
        借出状态不再依赖 book.borrowed 字段，而是通过 borrow 表动态判断（是否存在记录）。
        """
        self.beginResetModel()
        cursor = Connector.get_cursor()
        if keyword is not None and keyword.strip() != '':
            like = f"%{keyword.strip()}%"
            sql = """
                SELECT
                    b.b_name,
                    b.author,
                    b.publish_date,
                    b.publish_name,
                    CASE WHEN EXISTS (SELECT 1 FROM borrow br WHERE br.b_id = b.book_id) THEN 1 ELSE 0 END AS borrowed,
                    b.book_id
                FROM book b
                WHERE b.b_name LIKE %s OR b.author LIKE %s OR b.publish_name LIKE %s
            """
            cursor.execute(sql, (like, like, like))
        else:
            sql = """
                SELECT
                    b.b_name,
                    b.author,
                    b.publish_date,
                    b.publish_name,
                    CASE WHEN EXISTS (SELECT 1 FROM borrow br WHERE br.b_id = b.book_id) THEN 1 ELSE 0 END AS borrowed,
                    b.book_id
                FROM book b
            """
            cursor.execute(sql)
        result = cursor.fetchall()
        self.__bookInfoList = []
        for row in result:
            # row: (b_name, author, publish_date(date or None), publish_name, borrowed(int), book_id)
            publish_date = row[2].strftime('%Y-%m-%d') if row[2] else ''
            self.__bookInfoList.append([
                row[0],                          # 标题
                row[1],                          # 作者
                publish_date,                    # 出版日期
                row[3],                          # 出版社
                '否' if row[4] == 0 else '是',   # 是否已借出
                row[5],                          # BookID（操作使用）
            ])
        self.endResetModel()