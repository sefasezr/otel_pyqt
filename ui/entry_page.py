from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from ui.register_window import RegisterWindow  # Kayıt ekranını içe aktarıyoruz
from ui.login_window import LoginWindow  # Giriş ekranını içe aktarıyoruz
from ui.main_window import MainWindow  # Ana ekranı içe aktarıyoruz
from ui.contact_us_window import ContactUsWindow  # Bize ulaşın ekranını içe aktarıyoruz

class EntryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hoş Geldiniz")
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
        layout.setSpacing(20)

        # Başlık
        self.title = QLabel("Otel Rezervasyon Sistemimize Hoş Geldiniz!")
        self.title.setFont(QFont("Arial", 16, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white;")
        layout.addWidget(self.title)

        # Buton Stili
        button_style = """
            QPushButton {
                background-color: rgba(0, 123, 255, 0.8);
                color: white;
                font-size: 14px;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
            }
            QPushButton:hover {
                background-color: rgba(0, 86, 179, 0.8);
            }
        """

        self.login_button = QPushButton("Giriş Yap", self)
        self.login_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.login_button.setStyleSheet(button_style)
        self.login_button.clicked.connect(self.open_login_window)  # Giriş yap ekranına yönlendirme
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        self.register_button = QPushButton("Üye Ol", self)
        self.register_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.register_button.setStyleSheet(button_style)
        self.register_button.clicked.connect(self.open_register_window)  # Kayıt ol ekranına yönlendirme
        layout.addWidget(self.register_button, alignment=Qt.AlignCenter)

        # Bize Ulaşın Butonu
        self.contact_button = QPushButton("Bize Ulaşın", self)
        self.contact_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.contact_button.setStyleSheet(button_style)
        self.contact_button.clicked.connect(self.open_contact_us_window)  # Bize ulaşın ekranına yönlendirme
        layout.addWidget(self.contact_button, alignment=Qt.AlignCenter)

        # Çıkış Butonu
        self.exit_button = QPushButton("Çıkış", self)
        self.exit_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.exit_button.setStyleSheet(button_style)
        self.exit_button.clicked.connect(self.close_application)  # Uygulamayı kapatma
        layout.addWidget(self.exit_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.background_label.lower()

    def open_login_window(self):
        """Giriş yap ekranını aç ve giriş başarılıysa MainWindow'a yönlendir"""
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def open_register_window(self):
        """Üye ol ekranını aç ve üye olunursa MainWindow'a yönlendir"""
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.hide()

    def open_contact_us_window(self):
        """Bize Ulaşın penceresini aç"""
        self.contact_window = ContactUsWindow()
        self.contact_window.show()
        self.hide()

    def close_application(self):
        """Uygulamayı kapat"""
        reply = QMessageBox.question(self, 'Çıkış', 'Uygulamayı kapatmak istediğinizden emin misiniz?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()  # Uygulamayı kapat
