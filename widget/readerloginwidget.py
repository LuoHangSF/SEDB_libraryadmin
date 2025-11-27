from PySide6.QtWidgets import QWidget, QMessageBox
from widget.ui_readerloginwidget_mode import Ui_ReaderLoginWidget  # 使用新版UI
from lib.share import SI
from database.connector import Connector


class ReaderLoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_ReaderLoginWidget()
        self.__ui.setupUi(self)

        # 返回主菜单（保留原逻辑，通常 index=0 是首页）
        self.__ui.m_returnButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(0))
        # 登录
        self.__ui.m_loginButton.clicked.connect(self.login)
        # 注册
        self.__ui.m_registerButton.clicked.connect(self.register)
        # 人脸登录按钮目前无功能，仅预留
        self.__ui.m_returnButton_2.clicked.connect(self.faceLoginPlaceholder)

    def faceLoginPlaceholder(self):
        QMessageBox.information(self, '提示', '人脸登录功能尚未实现')

    def login(self):
        phone = self.__ui.m_accountLineEdit.text().strip()
        password = self.__ui.m_passwordLineEdit.text().strip()

        if phone == '' or password == '':
            QMessageBox.information(self, '登录失败', '请输入手机号和密码')
            return

        cursor = Connector.get_cursor()
        sql = 'SELECT phone_number FROM user WHERE phone_number = %s AND password = %s LIMIT 1'
        cursor.execute(sql, (phone, password))
        result = cursor.fetchone()
        if result is None:
            QMessageBox.critical(self, '登录失败', '手机号或密码错误，请重试')
            return

        # 保存当前登录用户标识（手机号）
        SI.g_userId = result[0]

        # 跳转到借阅主界面：优先按对象名查找，避免索引错乱
        borrow_widget = SI.g_mainWindow.findChild(QWidget, 'm_borrowWidget')
        if borrow_widget is not None:
            SI.g_mainWindow.setCurrentWidget(borrow_widget)
        else:
            # 回退方案：使用原先常用索引（若不正确请改为你 UI 的实际索引）
            SI.g_mainWindow.setCurrentIndex(3)

        SI.g_mainWindow.updateBorrowWidget()

    def register(self):
        # 跳转到注册界面：避免硬编码索引
        register_widget = SI.g_mainWindow.findChild(QWidget, 'm_registerWidget')
        if register_widget is not None:
            SI.g_mainWindow.setCurrentWidget(register_widget)
        else:
            # 回退方案：如果对象名无法找到，则尝试原工程常用的注册页索引（原先是 4）
            SI.g_mainWindow.setCurrentIndex(4)