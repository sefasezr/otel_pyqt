from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Yap")
        self.setGeometry(400, 150, 800, 700)
        self.init_ui()

    def init_ui(self):
        # Arka plan resmi
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/hotel_image.jpg")  # Resmin yolu
        self.background_label.setPixmap(pixmap.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        layout.setSpacing(8)  # Daha dar aralıklar

        # Başlık
        self.title = QLabel("Giriş Yap")
        self.title.setFont(QFont("Arial", 20, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white;")
        layout.addWidget(self.title)

        # Ortak stil (kutucuk boyutları ve tasarımı)
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

        # Kullanıcı adı giriş kutusu
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Kullanıcı Adı")
        self.username_input.setStyleSheet(input_style)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)

        # Şifre giriş kutusu
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(input_style)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        # Spacer ekleyerek aralıkları düzenliyoruz
        layout.addSpacing(5)

        # Giriş Yap Butonu
        self.login_button = QPushButton("Giriş Yap", self)
        self.login_button.clicked.connect(self.login_user)
        self.login_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.login_button.setStyleSheet("background-color: #007bff; color: white; padding: 10px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        # Spacer ekleyerek butonların arasını daraltıyoruz
        layout.addSpacing(5)

        # Ana Ekrana Dön Butonu
        self.back_button = QPushButton("Ana Ekrana Dön", self)
        self.back_button.clicked.connect(self.go_back_to_main)
        self.back_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.back_button.setStyleSheet("background-color: #dc3545; color: white; padding: 10px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def login_user(self):
        # Burada giriş doğrulama işlemleri yapılabilir
        print("Giriş yapılıyor...")

    def go_back_to_main(self):
        from ui.main_window import MainWindow  # Ana pencereyi çağırıyoruz
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()  # Giriş penceresini kapat
