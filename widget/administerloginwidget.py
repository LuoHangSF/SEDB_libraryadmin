from PySide6.QtWidgets import QWidget, QMessageBox
from widget.ui_administerloginwidget import Ui_AdministerLoginWidget
from lib.share import SI
from database.connector import Connector


class AdministerLoginWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_AdministerLoginWidget()
        self.__ui.setupUi(self)

        # 返回首页
        self.__ui.m_returnButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(0))
        # 登录按钮
        self.__ui.m_loginButton.clicked.connect(self.login)

    def login(self):
        account = self.__ui.m_accountLineEdit.text().strip()
        password = self.__ui.m_passwordLineEdit.text().strip()

        if account == '' or password == '':
            QMessageBox.information(self, '登录失败', '请输入账号和密码')
            return

        cursor = Connector.get_cursor()
        sql = 'SELECT a_id FROM administer WHERE a_name = %s AND password = %s LIMIT 1'
        cursor.execute(sql, (account, password))
        row = cursor.fetchone()  # 关键：一定要调用 fetchone()

        if row is None:
            QMessageBox.critical(self, '登录失败', '管理员账号或密码错误，请检查')
            return

        # 登录成功，跳转到管理员界面
        admin_widget = SI.g_mainWindow.findChild(QWidget, 'm_adminWidget')
        if admin_widget is not None:
            SI.g_mainWindow.setCurrentWidget(admin_widget)
        else:
            # 回退：使用原工程的索引（若与你的工程不一致，请根据实际修改）
            SI.g_mainWindow.setCurrentIndex(5)

        # 如果有管理员界面的数据刷新方法，调用之
        if hasattr(SI.g_mainWindow, 'updateAdminWidget'):
            SI.g_mainWindow.updateAdminWidget()