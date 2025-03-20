from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class CancelReservationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rezervasyon İptali")
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
        layout.setSpacing(15)

        # Başlık
        self.title = QLabel("Rezervasyon İptali")
        self.title.setFont(QFont("Arial", 20, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white;")
        layout.addWidget(self.title)

        # Ortak stil
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

        # Rezervasyon ID Girişi
        self.reservation_id_input = QLineEdit(self)
        self.reservation_id_input.setPlaceholderText("Rezervasyon Numarası")
        self.reservation_id_input.setStyleSheet(input_style)
        layout.addWidget(self.reservation_id_input, alignment=Qt.AlignCenter)

        # Rezervasyonu İptal Et Butonu
        self.cancel_button = QPushButton("Rezervasyonu İptal Et", self)
        self.cancel_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.cancel_button.setStyleSheet("background-color: #dc3545; color: white; padding: 12px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.cancel_button, alignment=Qt.AlignCenter)

        # Ana Ekrana Dön Butonu
        self.back_button = QPushButton("Ana Menüye Dön", self)
        self.back_button.clicked.connect(self.go_back_to_main)  # Ana menüye dön bağlantısı
        self.back_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.back_button.setStyleSheet("background-color: #007bff; color: white; padding: 12px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def go_back_to_main(self):
        """Ana Menüye Dön"""
        from ui.main_window import MainWindow  # Ana pencereyi çağırıyoruz
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()  # Rezervasyon iptal sayfasını kapat
