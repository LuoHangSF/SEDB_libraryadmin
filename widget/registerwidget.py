from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt
from widget.ui_registerwidget_mode import Ui_RegisterWidget  # 使用新版UI
from lib.share import SI
from database.connector import Connector


class RegisterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_RegisterWidget()
        self.__ui.setupUi(self)

        self.__ui.m_returnButton.clicked.connect(self.returnLogin)
        self.__ui.m_registerButton.clicked.connect(self.register)

    def returnLogin(self):
        # 优先按对象名跳转，避免硬编码索引错误
        reader_login_widget = SI.g_mainWindow.findChild(QWidget, 'm_readerLoginWidget')
        if reader_login_widget is not None:
            SI.g_mainWindow.setCurrentWidget(reader_login_widget)
        else:
            # 回退到首页（原工程 index=0 通常是首页）
            SI.g_mainWindow.setCurrentIndex(0)

    def register(self):
        name = self.__ui.m_nameLlineEdit.text().strip()
        phone = self.__ui.m_mobileLineEdit_2.text().strip()   # 手机号（主键）
        email = self.__ui.m_mobileLineEdit.text().strip()      # email（UI命名如此）
        category = self.__ui.m_roleComboBox.currentText().strip()
        password = self.__ui.m_passwordLineEdit.text().strip()
        password_confirm = self.__ui.m_passwordConfirmLineEdit.text().strip()

        if name == '' or phone == '' or password == '':
            QMessageBox.information(self, '注册失败', '姓名、手机号、密码不能为空')
            return

        if password != password_confirm:
            QMessageBox.information(self, '注册失败', '两次输入的密码不一致')
            return

        cursor = Connector.get_cursor()

        # 检查手机号是否已存在
        sql_check = 'SELECT 1 FROM user WHERE phone_number = %s LIMIT 1'
        cursor.execute(sql_check, (phone,))
        if cursor.fetchone() is not None:
            QMessageBox.information(self, '注册失败', '该手机号已注册')
            return

        # 插入用户：face_id 为空；sex/unit 暂时占位
        sql_insert = '''
            INSERT INTO user (phone_number, u_name, email, category, password, face_id, balance, sex, unit)
            VALUES (%s, %s, %s, %s, %s, %s, 0.00, %s, %s)
        '''
        cursor.execute(sql_insert, (phone, name, email, category, password, None, '未知', ''))
        Connector.get_connection()

        QMessageBox.information(self, '注册成功', '注册成功，请登录')

        # 跳回“读者登录”页（按对象名查找，避免索引错乱）
        reader_login_widget = SI.g_mainWindow.findChild(QWidget, 'm_readerLoginWidget')
        if reader_login_widget is not None:
            SI.g_mainWindow.setCurrentWidget(reader_login_widget)
        else:
            # 回退方案：若未找到对象名，退回首页或你原先约定的读者登录索引
            SI.g_mainWindow.setCurrentIndex(0)