from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, \
    QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from service.reservation_service import ReservationService


class CancelReservationWindow(QWidget):
    def __init__(self, user):
        super().__init__()
        self.setWindowTitle("Rezervasyon İptali")
        self.setGeometry(400, 150, 800, 700)
        self.user = user
        self.service = ReservationService()
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

        # Rezervasyonları Göster (Tabloyu)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Oda Türü", "Giriş Tarihi", "Çıkış Tarihi", "İptal Et"])
        layout.addWidget(self.table)

        # Rezervasyonları Al ve Göster
        self.load_reservations()

        # Ana Menüye Dön Butonu
        self.back_button = QPushButton("Ana Menüye Dön", self)
        self.back_button.clicked.connect(self.go_back_to_main)  # Ana menüye dön bağlantısı
        self.back_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.back_button.setStyleSheet("background-color: #007bff; color: white; padding: 12px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def load_reservations(self):
        """Kullanıcıya ait rezervasyonları al ve tabloya ekle"""
        reservations = self.get_upcoming_reservations()

        if not reservations:
            # Eğer rezervasyon yoksa kullanıcıya bilgi ver
            QMessageBox.information(self, "Rezervasyon Yok", "Bugünden sonraki rezervasyonunuz bulunmamaktadır.")
            return

        self.table.setRowCount(len(reservations))

        for row, reservation in enumerate(reservations):
            self.table.setItem(row, 0, QTableWidgetItem(reservation['room_type']))
            self.table.setItem(row, 1, QTableWidgetItem(reservation['check_in_date']))
            self.table.setItem(row, 2, QTableWidgetItem(reservation['check_out_date']))

            cancel_button = QPushButton("İptal Et")
            cancel_button.clicked.connect(lambda checked, r=reservation: self.cancel_reservation(r))
            self.table.setCellWidget(row, 3, cancel_button)

    def get_upcoming_reservations(self):
        """Kullanıcıya ait, bugünden sonraki rezervasyonları veritabanından al"""
        try:
            # user nesnesi tuple olabilir, bu durumda onu User nesnesine dönüştürün
            if isinstance(self.user, tuple):  # Eğer user bir tuple ise
                user_id = self.user[0]  # User ID'yi tuple'dan alıyoruz
            else:
                user_id = self.user.user_id  # User nesnesi ise doğrudan user_id'yi alıyoruz

            return self.service.get_upcoming_reservations(user_id)
        except Exception as e:
            print(f"Rezervasyonları alırken hata oluştu: {e}")
            return []


    def go_back_to_main(self):
        """Ana Menüye Dön"""
        from ui.main_window import MainWindow
        self.main_window = MainWindow(self.user)
        self.main_window.show()
        self.close()  # Rezervasyon iptal sayfasını kapat
