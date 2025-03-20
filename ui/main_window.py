from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from ui.register_window import RegisterWindow  # Kayıt ekranını içe aktarıyoruz
from ui.login_window import LoginWindow  # Giriş ekranını içe aktarıyoruz
from ui.reservation_window import ReservationWindow  # Rezervasyon ekranını içe aktarıyoruz
from ui.reservation_cancel_window import CancelReservationWindow  # Rezervasyon iptal ekranı

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Otel Rezervasyon Sistemi")
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
        self.title.setFont(QFont("Arial", 14, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white;")
        layout.addWidget(self.title)

        # Butonları oluştur ve stillendir
        button_style = """
            QPushButton {
                background-color: rgba(0, 123, 255, 0.8);
                color: white;
                font-size: 14px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(0, 86, 179, 0.8);
            }
        """

        self.login_button = QPushButton("Giriş Yap", self)
        self.login_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.login_button.setStyleSheet(button_style)
        self.login_button.clicked.connect(self.open_login_window)  # Giriş yap ekranına yönlendirme
        layout.addWidget(self.login_button)

        self.register_button = QPushButton("Üye Ol", self)
        self.register_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.register_button.setStyleSheet(button_style)
        self.register_button.clicked.connect(self.open_register_window)  # Kayıt ol ekranına yönlendirme
        layout.addWidget(self.register_button)

        self.reserve_button = QPushButton("Rezervasyon Yap", self)
        self.reserve_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.reserve_button.setStyleSheet(button_style)
        self.reserve_button.clicked.connect(self.open_reservation_window)  # Rezervasyon ekranına yönlendirme
        layout.addWidget(self.reserve_button)

        self.cancel_button = QPushButton("Rezervasyon İptali", self)
        self.cancel_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.cancel_button.setStyleSheet(button_style)
        self.cancel_button.clicked.connect(self.open_cancel_reservation_window)  # Rezervasyon iptal ekranına yönlendirme
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        # Arka planı en arkaya gönder
        self.background_label.lower()

    def open_register_window(self):
        """Kayıt ol sayfasını aç ve ana ekranı gizle"""
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.hide()

    def open_login_window(self):
        """Giriş yap sayfasını aç ve ana ekranı gizle"""
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def open_reservation_window(self):
        """Rezervasyon yap sayfasını aç ve ana ekranı gizle"""
        self.reservation_window = ReservationWindow()
        self.reservation_window.show()
        self.hide()

    def open_cancel_reservation_window(self):
        """Rezervasyon iptal sayfasını aç ve ana ekranı gizle"""
        self.cancel_window = CancelReservationWindow()
        self.cancel_window.show()
        self.hide()
