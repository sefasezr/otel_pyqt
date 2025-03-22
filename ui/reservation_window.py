from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QComboBox, QDateEdit, QSpinBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
import random  # Simüle etmek için rastgele odalar oluşturuyoruz

class ReservationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rezervasyon Yap")
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
        layout.setSpacing(10)  # Kutular arasındaki mesafeyi ayarlıyoruz

        # Başlık
        self.title = QLabel("Rezervasyon Yap")
        self.title.setFont(QFont("Arial", 20, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white;")
        layout.addWidget(self.title)

        # Ortak stil
        input_style = """
            QLineEdit, QComboBox, QDateEdit, QSpinBox {
                font-size: 14px;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid gray;
                background-color: white;
                width: 400px;
                height: 40px;
            }
        """

        # Ad Soyad
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Ad Soyad")
        self.name_input.setStyleSheet(input_style)
        layout.addWidget(self.name_input, alignment=Qt.AlignCenter)

        # Telefon Numarası
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Telefon Numarası")
        self.phone_input.setStyleSheet(input_style)
        layout.addWidget(self.phone_input, alignment=Qt.AlignCenter)

        # E-Posta
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("E-posta")
        self.email_input.setStyleSheet(input_style)
        layout.addWidget(self.email_input, alignment=Qt.AlignCenter)

        # Giriş Tarihi (Güncel tarih ile başlat)
        self.checkin_date = QDateEdit(self)
        self.checkin_date.setCalendarPopup(True)
        self.checkin_date.setDate(QDate.currentDate())  # Güncel tarih
        self.checkin_date.setStyleSheet(input_style)
        layout.addWidget(self.checkin_date, alignment=Qt.AlignCenter)

        # Çıkış Tarihi (Güncel tarih ile başlat)
        self.checkout_date = QDateEdit(self)
        self.checkout_date.setCalendarPopup(True)
        self.checkout_date.setDate(QDate.currentDate())  # Güncel tarih
        self.checkout_date.setStyleSheet(input_style)
        layout.addWidget(self.checkout_date, alignment=Qt.AlignCenter)

        # Oda Listesi (Boş & Dolu Oda Kontrolü)
        self.room_table = QTableWidget(self)
        self.room_table.setColumnCount(2)
        self.room_table.setHorizontalHeaderLabels(["Oda Numarası", "Durum"])
        self.room_table.setFixedSize(400, 200)
        layout.addWidget(self.room_table, alignment=Qt.AlignCenter)

        # Oda Müsaitlik Kontrol Butonu
        self.check_rooms_button = QPushButton("Müsait Odaları Göster", self)
        self.check_rooms_button.clicked.connect(self.check_available_rooms)
        self.check_rooms_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.check_rooms_button.setStyleSheet("background-color: #17a2b8; color: white; padding: 10px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.check_rooms_button, alignment=Qt.AlignCenter)

        # Rezervasyonu Tamamla Butonu
        self.reserve_button = QPushButton("Rezervasyonu Tamamla", self)
        self.reserve_button.clicked.connect(self.complete_reservation)
        self.reserve_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.reserve_button.setStyleSheet("background-color: #28a745; color: white; padding: 10px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.reserve_button, alignment=Qt.AlignCenter)

        # Ana Ekrana Dön Butonu
        self.back_button = QPushButton("Ana Ekrana Dön", self)
        self.back_button.clicked.connect(self.go_back_to_main)
        self.back_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.back_button.setStyleSheet("background-color: #dc3545; color: white; padding: 10px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def check_available_rooms(self):
        """Müsait odaları listele"""
        self.room_table.setRowCount(0)  # Önceki verileri temizle

        # Simüle edilen odalar (Gerçekte veritabanından çekilecek)
        rooms = [(f"10{num}", random.choice(["Boş", "Dolu"])) for num in range(1, 11)]

        for row, (room_number, status) in enumerate(rooms):
            self.room_table.insertRow(row)
            self.room_table.setItem(row, 0, QTableWidgetItem(room_number))
            status_item = QTableWidgetItem(status)
            if status == "Dolu":
                status_item.setBackground(Qt.red)  # Dolu odaları kırmızı yap
            else:
                status_item.setBackground(Qt.green)  # Boş odaları yeşil yap
            self.room_table.setItem(row, 1, status_item)

    def complete_reservation(self):
        # Burada rezervasyon kaydı ile ilgili işlemler yapılabilir
        print("Rezervasyon tamamlandı!")

    def go_back_to_main(self):
        from ui.main_window import MainWindow  # Ana pencereyi çağırıyoruz
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()  # Rezervasyon penceresini kapat
