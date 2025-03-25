from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from ui.reservation_window import ReservationWindow
from ui.reservation_cancel_window import CancelReservationWindow

class MainWindow(QWidget):
    def __init__(self, user):  # 👈 user parametresi alındı
        super().__init__()
        self.user = user
        self.setWindowTitle("Otel Rezervasyon Sistemi")
        self.setGeometry(400, 150, 800, 700)
        self.init_ui()

    def init_ui(self):
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/hotel_image.jpg")
        self.background_label.setPixmap(pixmap.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        layout.setSpacing(20)

        full_name = f"{self.user[1]} {self.user[2]}"
        self.title = QLabel(f"Hoş geldin, {full_name} 👋")
        self.title.setFont(QFont("Arial", 16, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white;")
        layout.addWidget(self.title)

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

        self.reserve_button = QPushButton("Rezervasyon Yap", self)
        self.reserve_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.reserve_button.setStyleSheet(button_style)
        self.reserve_button.clicked.connect(self.open_reservation_window)
        layout.addWidget(self.reserve_button)

        self.cancel_button = QPushButton("Rezervasyon İptali", self)
        self.cancel_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.cancel_button.setStyleSheet(button_style)
        self.cancel_button.clicked.connect(self.open_cancel_reservation_window)
        layout.addWidget(self.cancel_button)

        self.logout_button = QPushButton("Çıkış Yap", self)
        self.logout_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.logout_button.setStyleSheet("background-color: #dc3545; color: white; padding: 10px; border-radius: 5px;")
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)
        self.background_label.lower()

    def open_reservation_window(self):
        self.reservation_window = ReservationWindow()
        self.reservation_window.show()
        self.hide()

    def open_cancel_reservation_window(self):
        self.cancel_window = CancelReservationWindow()
        self.cancel_window.show()
        self.hide()

    def logout(self):
        from ui.entry_page import EntryPage
        self.entry_page = EntryPage()
        self.entry_page.show()
        self.close()
