# ui/cancel_reservation_window.py

from PyQt5.QtWidgets import QWidget, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from service.reservation_service import ReservationService
from repository.room_repository import RoomRepository


class CancelReservationWindow(QWidget):
    def __init__(self, user):
        super().__init__()
        self.setWindowTitle("Rezervasyon İptali")
        self.setGeometry(400, 150, 800, 700)
        self.user = user
        self.service = ReservationService()
        self.room_repo = RoomRepository()
        self.init_ui()

    def init_ui(self):
        # Arka plan
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/hotel_image.jpg")
        self.background_label.setPixmap(
            pixmap.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        )
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

        # Tablo
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Oda Türü", "Giriş Tarihi", "Çıkış Tarihi", "İptal Et"])
        layout.addWidget(self.table)

        # İlk yükleme
        self.load_reservations()

        # Ana Menüye Dön
        self.back_button = QPushButton("Ana Menüye Dön", self)
        self.back_button.clicked.connect(self.go_back_to_main)
        self.back_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.back_button.setStyleSheet(
            "background-color: #007bff; color: white; padding: 12px; border-radius: 5px; width: 400px;"
        )
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def load_reservations(self):
        """Kullanıcıya ait rezervasyonları yeniden çek ve tabloyu güncelle."""
        self.table.setRowCount(0)               # önceki satırları temizle
        reservations = self.get_upcoming_reservations()

        if not reservations:
            QMessageBox.information(self, "Rezervasyon Yok",
                                    "Güncel Rezervasonunuz Bulunmamakta.")
            return

        self.table.setRowCount(len(reservations))
        for row, reservation in enumerate(reservations):
            room_id = reservation[2]
            room_type = self.room_repo.get_room_type_by_id(room_id) or "–"
            check_in = reservation[3]
            check_out = reservation[4]

            self.table.setItem(row, 0, QTableWidgetItem(room_type))
            self.table.setItem(row, 1, QTableWidgetItem(str(check_in)))
            self.table.setItem(row, 2, QTableWidgetItem(str(check_out)))

            cancel_btn = QPushButton("İptal Et")
            cancel_btn.clicked.connect(lambda _, r=reservation: self.cancel_reservation(r))
            self.table.setCellWidget(row, 3, cancel_btn)

    def get_upcoming_reservations(self):
        """Bugünden sonraki rezervasyonları al."""
        try:
            if isinstance(self.user, tuple):
                user_id = self.user[0]
            else:
                user_id = self.user.user_id
            return self.service.get_upcoming_reservations(user_id)
        except Exception as e:
            print(f"Rezervasyonları alırken hata oluştu: {e}")
            return []

    def cancel_reservation(self, reservation):
        """Seçilen rezervasyonu iptal et, DB’yi güncelle ve tabloyu yenile."""
        reservation_id = reservation[0]

        try:
            success = self.service.cancel_reservation(self.user, reservation_id)
            if success:
                QMessageBox.information(self, "Başarılı",
                                        f"Rezervasyon {reservation_id} iptal edildi.")
                self.load_reservations()   # tabloyu tekrar doldur
            else:
                QMessageBox.warning(self, "Hata", "Rezervasyon iptal edilemedi.")
        except Exception as e:
            print("❌ İptal sırasında hata:", e)
            QMessageBox.critical(self, "Hata", str(e))

    def go_back_to_main(self):
        from ui.main_window import MainWindow
        self.hide()
        self.main_window = MainWindow(self.user)
        self.main_window.show()
        self.deleteLater()
