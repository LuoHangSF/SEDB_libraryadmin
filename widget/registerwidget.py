from PySide6.QtWidgets import QWidget, QMessageBox

from lib.share import SI
from widget.ui_registerwidget import Ui_RegisterWidget
from database.connector import Connector


class RegisterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_RegisterWidget()
        self.__ui.setupUi(self)
        self.__ui.m_returnButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(1))
        self.__ui.m_registerButton.clicked.connect(self.register)

    def register(self):
        name = self.__ui.m_nameLlineEdit.text()
        password = self.__ui.m_passwordLineEdit.text()
        password_confirm = self.__ui.m_passwordConfirmLineEdit.text()
        gender = self.__ui.m_genderComboBox.currentText()
        balance = 0
        mobile = self.__ui.m_mobileLineEdit.text()
        unit = self.__ui.m_unitLineEdit.text()

        # 数据库 role.r_id 从 1 开始，QComboBox 索引从 0 开始，需要 +1 修正
        role_id = self.__ui.m_roleComboBox.currentIndex() + 1

        if name == '' or password == '' or mobile == '' or unit == '':
            QMessageBox.information(self, '注册失败', '请将信息填写完整再注册')
            return
        if password != password_confirm:
            QMessageBox.information(self, '注册失败', '密码和确认密码输入不一致')
            return

        cursor = Connector.get_cursor()
        sql = """
            INSERT INTO user (u_name, password, sex, balance, phone_number, r_id, unit) 
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        try:
            cursor.execute(sql, (name, password, gender, balance, mobile, role_id, unit))
            # 显式提交事务，确保数据持久化
            conn = Connector.get_connection()
            if hasattr(conn, "commit"):
                conn.commit()
        except Exception as e:
            QMessageBox.information(self, '注册失败', f'注册过程中出现错误：{e}')
            return

        QMessageBox.information(self, '注册成功', '注册成功')