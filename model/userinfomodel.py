from typing import Any
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex, Qt

import lib.share
from database.connector import Connector
from lib.share import SI


class UserInfoModel(QAbstractTableModel):
    """
    新版用户信息模型：
    列含义：
    0 手机号
    1 余额
    2 类别（与 role.r_name 对应）
    3 已借阅数量
    4 最大借阅数量 (role.max_number)
    5 最大借阅时长 (role.max_day)
    6 查看已借阅书籍（按钮占位列）
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始占位：与列数匹配
        self.__userInfo = [['', 0.00, '', 0, 0, 0, '']]
        self.__headerList = ['手机号', '余额', '类别', '已借阅数量', '最大借阅数量', '最大借阅时长', '查看已借阅书籍']
        lib.share.SI.g_userInfoModel = self

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if 0 <= section < len(self.__headerList):
                return self.__headerList[section]
        return super().headerData(section, orientation, role)

    def rowCount(self, parent: [QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__userInfo)

    def columnCount(self, parent: [QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__headerList)

    def data(self, index: [QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if 0 <= index.column() < len(self.__headerList) and 0 <= index.row() < len(self.__userInfo):
            return self.__userInfo[index.row()][index.column()]
        return None

    def update(self):
        if SI.g_userId is None:
            # 未登录时重置
            self.__userInfo = [['', 0.00, '', 0, 0, 0, '']]
            self.dataChanged.emit(self.index(0, 0), self.index(0, len(self.__headerList) - 1))
            return

        cursor = Connector.get_cursor()
        # 修改：使用 phone_number / category 与新结构匹配，借阅计数 LEFT JOIN borrow
        sql = """
            SELECT
                u.phone_number,
                u.balance,
                u.category,
                COUNT(br.b_id) AS borrowed_count,
                r.max_number,
                r.max_day,
                '' AS placeholder
            FROM user u
            JOIN role r ON r.r_name = u.category
            LEFT JOIN borrow br ON br.phone_number = u.phone_number
            WHERE u.phone_number = %s
            GROUP BY u.phone_number, u.balance, u.category, r.max_number, r.max_day
            LIMIT 1
        """
        cursor.execute(sql, (SI.g_userId,))
        result = cursor.fetchone()
        if result is None:
            # 登录后若用户不存在（理论上不应出现），给一个占位
            self.__userInfo = [[SI.g_userId, 0.00, '未知', 0, 0, 0, '']]
        else:
            self.__userInfo = [list(result)]
        self.dataChanged.emit(self.index(0, 0), self.index(0, len(self.__headerList) - 1))