from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QDate
from lib.share import SI
# 使用你提供的新版 UI
from widget.ui_addbookwidget_mode import Ui_AddBookWidget
from database.connector import Connector


class AddBookWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_AddBookWidget()
        self.__ui.setupUi(self)
        self.__ui.m_returnButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(5))
        self.__ui.m_addButton.clicked.connect(self.addBook)

        # 为日期控件提供默认值（避免空值）
        today = QDate.currentDate()
        if hasattr(self.__ui, 'm_publishDateEdit') and self.__ui.m_publishDateEdit.date().isNull():
            self.__ui.m_publishDateEdit.setDate(today)
        if hasattr(self.__ui, 'm_publishDateEdit_2') and self.__ui.m_publishDateEdit_2.date().isNull():
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

        # 采购入库日期
        d_stock = self.__ui.m_publishDateEdit_2.date() if hasattr(self.__ui, 'm_publishDateEdit_2') else QDate.currentDate()
        stock_in_date = f'{d_stock.year():04d}-{d_stock.month():02d}-{d_stock.day():02d}'

        # 书号（可空 -> 自动生成）
        manual_book_id = self.__ui.m_titleLineEdit_2.text().strip() if hasattr(self.__ui, 'm_titleLineEdit_2') else ''
        if manual_book_id == '':
            # 今日已入库数量 -> 生成 DYYYYMMDDxN
            yyyymmdd = f'{d_stock.year():04d}{d_stock.month():02d}{d_stock.day():02d}'
            cursor = Connector.get_cursor()
            sql_count = "SELECT COUNT(*) FROM book WHERE stock_in_date = %s"
            cursor.execute(sql_count, (stock_in_date,))
            cnt = cursor.fetchone()[0] if cursor is not None else 0
            book_id = f'D{yyyymmdd}x{cnt + 1}'
        else:
            book_id = manual_book_id

        # 对缺失信息宽松处理：允许空值/默认值，避免报错
        if title == '':
            title = '未命名书籍'
        # author/publish_name 可为空；price 默认为 0

        # 写库
        cursor = Connector.get_cursor()
        sql = """
            INSERT INTO book (book_id, b_name, author, publish_name, price, publish_date, stock_in_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (book_id, title, author, publish_name, price, publish_date, stock_in_date))
        Connector.get_connection()

        QMessageBox.information(self, '添加成功', f'添加书籍成功，书号：{book_id}')
        # 返回管理员页并刷新
        SI.g_mainWindow.updateAdminWidget()