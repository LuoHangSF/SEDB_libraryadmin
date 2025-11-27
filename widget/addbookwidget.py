from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QDate
from lib.share import SI
# 使用你提供的新版 UI
from widget.ui_addbookwidget_mode import Ui_AddBookWidget
from database.connector import Connector
from pymysql.err import IntegrityError


class AddBookWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_AddBookWidget()
        self.__ui.setupUi(self)
        # 返回管理员页（保持原逻辑索引，如需避免索引问题可改为按对象名查找）
        self.__ui.m_returnButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(5))
        self.__ui.m_addButton.clicked.connect(self.addBook)

        # 设置价格控件最大值为 9999.99，避免 UI 限制在 100 以内
        if hasattr(self.__ui, 'm_priceSpinBox'):
            try:
                # QDoubleSpinBox 支持 setMaximum，最多 2 位小数
                self.__ui.m_priceSpinBox.setMaximum(9999.99)
            except Exception:
                pass

        # 为日期控件提供默认值（避免空值）
        today = QDate.currentDate()
        if hasattr(self.__ui, 'm_publishDateEdit') and (not self.__ui.m_publishDateEdit.date().isValid()):
            self.__ui.m_publishDateEdit.setDate(today)
        if hasattr(self.__ui, 'm_publishDateEdit_2') and (not self.__ui.m_publishDateEdit_2.date().isValid()):
            self.__ui.m_publishDateEdit_2.setDate(today)

    def addBook(self):
        # 新 UI 字段读取
        title = self.__ui.m_titleLineEdit.text().strip() if hasattr(self.__ui, 'm_titleLineEdit') else ''
        author = self.__ui.m_authorLineEdit.text().strip() if hasattr(self.__ui, 'm_authorLineEdit') else ''
        publish_name = self.__ui.m_publishLineEdit.text().strip() if hasattr(self.__ui, 'm_publishLineEdit') else ''
        price = float(self.__ui.m_priceSpinBox.value()) if hasattr(self.__ui, 'm_priceSpinBox') else 0.0

        # 出版日期
        d_pub = self.__ui.m_publishDateEdit.date() if hasattr(self.__ui, 'm_publishDateEdit') else QDate.currentDate()
        publish_date = f'{d_pub.year():04d}-{d_pub.month():02d}-{d_pub.day():02d}'

        # 采购入库日期（用于“当天序号”）
        d_stock = self.__ui.m_publishDateEdit_2.date() if hasattr(self.__ui, 'm_publishDateEdit_2') else QDate.currentDate()
        stock_in_date = f'{d_stock.year():04d}-{d_stock.month():02d}-{d_stock.day():02d}'

        # 书号（手动优先；为空则自动生成）
        manual_book_id = self.__ui.m_titleLineEdit_2.text().strip() if hasattr(self.__ui, 'm_titleLineEdit_2') else ''

        # 对缺失信息宽松处理：允许空值/默认值，避免报错
        if title == '':
            title = '未命名书籍'
        # author/publish_name 可为空；price 默认为 0

        insert_sql = """
            INSERT INTO book (book_id, b_name, author, publish_name, price, publish_date, stock_in_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        def next_book_id_for_today() -> str:
            # 规则：'D' + 入库日期YYYYMMDD + 'x' + 当日最大后缀 + 1（更稳健，避免删除导致计数回退）
            yyyymmdd = f'{d_stock.year():04d}{d_stock.month():02d}{d_stock.day():02d}'
            prefix = f'D{yyyymmdd}x'
            cur = Connector.get_cursor()
            cur.execute(
                """
                SELECT COALESCE(MAX(CAST(SUBSTRING_INDEX(book_id, 'x', -1) AS UNSIGNED)), 0)
                FROM book
                WHERE book_id LIKE %s
                """,
                (prefix + '%',)
            )
            row = cur.fetchone()
            max_seq = row[0] if row and row[0] is not None else 0
            return f'{prefix}{max_seq + 1}'

        if manual_book_id:
            # 手工指定：直接尝试插入
            book_id = manual_book_id
            cursor = Connector.get_cursor()
            cursor.execute(insert_sql, (book_id, title, author, publish_name, price, publish_date, stock_in_date))
            Connector.get_connection()
        else:
            # 自动生成：并发兜底，主键冲突则重新生成
            while True:
                try:
                    book_id = next_book_id_for_today()
                    cursor = Connector.get_cursor()
                    cursor.execute(insert_sql, (book_id, title, author, publish_name, price, publish_date, stock_in_date))
                    Connector.get_connection()
                    break
                except IntegrityError:
                    # 极端并发下可能撞主键，重新生成重试
                    continue

        QMessageBox.information(self, '添加成功', f'添加书籍成功，书号：{book_id}')
        # 返回管理员页并刷新（如果你希望返回页面，也可以在此处 setCurrentIndex 或 setCurrentWidget）
        if hasattr(SI.g_mainWindow, 'updateAdminWidget'):
            SI.g_mainWindow.updateAdminWidget()