from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from service.user_service import UserService
from ui.main_window import MainWindow

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kayıt Ol")
        self.setGeometry(400, 150, 800, 700)
        self.user_service = UserService()
        self.init_ui()

    def init_ui(self):
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/hotel_image.jpg")
        self.background_label.setPixmap(pixmap.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        layout.setSpacing(12)

        self.title = QLabel("Kayıt Ol")
        self.title.setFont(QFont("Arial", 20, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white;")
        layout.addWidget(self.title)

        input_style = """
            QLineEdit {
                font-size: 14px;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid gray;
                background-color: white;
                width: 400px;
                height: 40px;
            }
        """

        self.first_name_input = QLineEdit(self)
        self.first_name_input.setPlaceholderText("İsim")
        self.first_name_input.setStyleSheet(input_style)
        layout.addWidget(self.first_name_input, alignment=Qt.AlignCenter)

        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Soyisim")
        self.last_name_input.setStyleSheet(input_style)
        layout.addWidget(self.last_name_input, alignment=Qt.AlignCenter)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Kullanıcı Adı")
        self.username_input.setStyleSheet(input_style)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Telefon Numarası")
        self.phone_input.setStyleSheet(input_style)
        layout.addWidget(self.phone_input, alignment=Qt.AlignCenter)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("E-posta")
        self.email_input.setStyleSheet(input_style)
        layout.addWidget(self.email_input, alignment=Qt.AlignCenter)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(input_style)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        self.password_confirm_input = QLineEdit(self)
        self.password_confirm_input.setPlaceholderText("Şifre Tekrar")
        self.password_confirm_input.setEchoMode(QLineEdit.Password)
        self.password_confirm_input.setStyleSheet(input_style)
        layout.addWidget(self.password_confirm_input, alignment=Qt.AlignCenter)

        self.register_button = QPushButton("Kayıt Ol", self)
        self.register_button.clicked.connect(self.register_user)
        self.register_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.register_button.setStyleSheet("background-color: #28a745; color: white; padding: 12px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.register_button, alignment=Qt.AlignCenter)

        self.back_button = QPushButton("Giriş Ekranına Dön", self)
        self.back_button.clicked.connect(self.go_back_to_entry)
        self.back_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.back_button.setStyleSheet("background-color: #dc3545; color: white; padding: 12px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def register_user(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        username = self.username_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        password_confirm = self.password_confirm_input.text()

        if password != password_confirm:
            QMessageBox.warning(self, "Hata", "Şifreler uyuşmuyor!")
            return

        success, message = self.user_service.register_user(
            first_name, last_name, username, phone, email, password
        )

        if success:
            user = self.user_service.repo.get_user_by_username(username)  # 👈 yeni kullanıcıyı al
            QMessageBox.information(self, "Başarılı", message)
            self.open_main_window(user)
        else:
            QMessageBox.warning(self, "Kayıt Başarısız", message)

    def open_main_window(self, user):
        self.main_window = MainWindow(user)
        self.main_window.show()
        self.close()

    def go_back_to_entry(self):
        from ui.entry_page import EntryPage
        self.entry_page = EntryPage()
        self.entry_page.show()
        self.close()
