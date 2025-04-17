from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox, QDateEdit, QTableWidget, \
    QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QDate
from database import Database
from reservation import Reservation
from service.reservation_service import ReservationService


class ReservationWindow(QWidget):
    def __init__(self, user):
        super().__init__()
        self.setWindowTitle("Rezervasyon Yap")
        self.setGeometry(400, 150, 800, 700)
        self.db = Database()
        self.user = user
        self.service = ReservationService()
        self.init_ui()

    def init_ui(self):
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/hotel_image.jpg")
        self.background_label.setPixmap(pixmap.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        layout.setSpacing(10)

        self.title = QLabel("Rezervasyon Yap")
        self.title.setFont(QFont("Arial", 20, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white;")
        layout.addWidget(self.title)

        input_style = """
            QLineEdit, QComboBox, QDateEdit {
                font-size: 14px;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid gray;
                background-color: white;
                width: 400px;
                height: 40px;
            }
        """

        self.checkin_date = QDateEdit(self)
        self.checkin_date.setCalendarPopup(True)
        self.checkin_date.setDate(QDate.currentDate())
        self.checkin_date.setStyleSheet(input_style)
        layout.addWidget(self.checkin_date, alignment=Qt.AlignCenter)

        self.checkout_date = QDateEdit(self)
        self.checkout_date.setCalendarPopup(True)
        self.checkout_date.setDate(QDate.currentDate())
        self.checkout_date.setStyleSheet(input_style)
        layout.addWidget(self.checkout_date, alignment=Qt.AlignCenter)

        self.people_count = QComboBox(self)
        self.people_count.addItems([str(i) for i in range(1, 11)])
        self.people_count.setStyleSheet(input_style)
        layout.addWidget(self.people_count, alignment=Qt.AlignCenter)

        self.room_type = QComboBox(self)
        self.room_type.addItems(["Standard", "Deluxe", "Suite"])
        self.room_type.setStyleSheet(input_style)
        layout.addWidget(self.room_type, alignment=Qt.AlignCenter)

        # Oda ID’leri ComboBox içinde gösterilecek
        self.room_selector = QComboBox(self)
        self.room_selector.setStyleSheet(input_style)
        layout.addWidget(self.room_selector, alignment=Qt.AlignCenter)

        self.check_rooms_button = QPushButton("Müsait Odaları Göster", self)
        self.check_rooms_button.clicked.connect(self.check_available_rooms)
        self.check_rooms_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.check_rooms_button.setStyleSheet("background-color: #17a2b8; color: white; padding: 10px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.check_rooms_button, alignment=Qt.AlignCenter)

        self.reserve_button = QPushButton("Rezervasyonu Tamamla", self)
        self.reserve_button.clicked.connect(self.complete_reservation)
        self.reserve_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.reserve_button.setStyleSheet("background-color: #28a745; color: white; padding: 10px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.reserve_button, alignment=Qt.AlignCenter)

        self.back_button = QPushButton("Ana Ekrana Dön", self)
        self.back_button.clicked.connect(self.go_back_to_main)
        self.back_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.back_button.setStyleSheet("background-color: #dc3545; color: white; padding: 10px; border-radius: 5px; width: 400px;")
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def check_available_rooms(self):
        """Odanın tarih aralıklarına göre müsaitliğini kontrol et"""
        self.room_selector.clear()
        selected_room_type = self.room_type.currentText()
        checkin_date = self.checkin_date.date().toString("yyyy-MM-dd")
        checkout_date = self.checkout_date.date().toString("yyyy-MM-dd")

        rooms = self.service.fetch_available_rooms(selected_room_type, checkin_date, checkout_date)

        for room_id, _, _ in rooms:
            self.room_selector.addItem(f"Oda {room_id}", room_id)

    def complete_reservation(self):
        checkin = self.checkin_date.date().toString("yyyy-MM-dd")
        checkout = self.checkout_date.date().toString("yyyy-MM-dd")
        people_count = int(self.people_count.currentText())

        if self.room_selector.currentIndex() == -1:
            print("⚠️ Lütfen bir oda seçin.")
            QMessageBox.warning(self, "Uyarı", "Lütfen bir oda seçin!")
            return

        room_id = self.room_selector.currentData()
        reservation, error = self.service.make_reservation(self.user, room_id, checkin, checkout, people_count)

        if error:
            print(f"❌ {error}")
            QMessageBox.warning(self, "Başarısız", f"Rezervasyon tamamlanamadı: {error}")
        else:
            print(f"✅ Rezervasyon tamamlandı! ID: {reservation.reservation_id} | Ücret: {reservation.price:.2f}₺")
            QMessageBox.information(self, "Başarılı", "Rezervasyon tamamlandı!")
            self.go_back_to_main()  # ✅ Başarılıysa ana menüye dön


    def go_back_to_main(self):
        from ui.main_window import MainWindow
        self.main_window = MainWindow(self.user)
        self.main_window.show()
        self.close()
