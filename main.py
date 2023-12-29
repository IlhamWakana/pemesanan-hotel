import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(300, 300, 300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        email_label = QLabel('Email:')
        self.email_line_edit = QLineEdit()
        password_label = QLabel('Password:')
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        layout.addWidget(email_label)
        layout.addWidget(self.email_line_edit)
        layout.addWidget(password_label)
        layout.addWidget(self.password_line_edit)

        button_box = QWidget()
        button_box_layout = QVBoxLayout()
        button_box.setLayout(button_box_layout)

        login_button = QPushButton('Masuk')
        login_button.clicked.connect(self.on_login_clicked)
        cancel_button = QPushButton('Batal')
        cancel_button.clicked.connect(self.on_cancel_clicked)

        button_box_layout.addWidget(login_button)
        button_box_layout.addWidget(cancel_button)

        layout.addWidget(button_box)

        self.setLayout(layout)
        self.setFixedSize(self.size())

    def on_login_clicked(self):
        email = self.email_line_edit.text()
        password = self.password_line_edit.text()
        print('Login with:', email, password)

    def on_cancel_clicked(self):
        self.close()

app = QApplication(sys.argv)
login_form = LoginForm()
login_form.show()
sys.exit(app.exec_())