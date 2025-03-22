from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from service.user_service import UserService  # Service katmanı
from ui.main_window import MainWindow  # Başarılı giriş sonrası yönlendirme

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Yap")
        self.setGeometry(400, 150, 800, 600)
        self.user_service = UserService()  # UserService örneği
        self.init_ui()

    def init_ui(self):
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/hotel_image.jpg")
        self.background_label.setPixmap(pixmap.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        layout.setSpacing(15)

        self.title = QLabel("Giriş Yap")
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

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Kullanıcı Adı")
        self.username_input.setStyleSheet(input_style)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(input_style)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        self.login_button = QPushButton("Giriş Yap", self)
        self.login_button.clicked.connect(self.login)
        self.login_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.login_button.setStyleSheet("background-color: #007bff; color: white; padding: 12px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        self.back_button = QPushButton("Giriş Ekranına Dön", self)
        self.back_button.clicked.connect(self.go_back_to_entry)
        self.back_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.back_button.setStyleSheet("background-color: #dc3545; color: white; padding: 12px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        success, result = self.user_service.login_user(username, password)

        if success:
            QMessageBox.information(self, "Başarılı", "Giriş başarılı.")
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Hata", result)

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back_to_entry(self):
        from ui.entry_page import EntryPage
        self.entry_page = EntryPage()
        self.entry_page.show()
        self.close()
