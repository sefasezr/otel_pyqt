# ui/contact_us_window.py

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from service.contact_us_service import ContactUsService  # ContactUsService'yi içe aktar

class ContactUsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bize Ulaşın")
        self.setGeometry(400, 150, 800, 700)
        self.init_ui()

    def init_ui(self):
        # Layout ayarları
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Başlık
        self.title = QLabel("Bize Ulaşın")
        self.title.setFont(QFont("Arial", 20, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        # İsim ve Soyisim
        name_layout = QHBoxLayout()
        self.name_label = QLabel("İsim:")
        self.name_input = QLineEdit(self)
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)

        # Telefon Numarası
        phone_layout = QHBoxLayout()
        self.phone_label = QLabel("Telefon Numarası:")
        self.phone_input = QLineEdit(self)
        phone_layout.addWidget(self.phone_label)
        phone_layout.addWidget(self.phone_input)
        layout.addLayout(phone_layout)

        # Mesaj Başlığı
        subject_layout = QHBoxLayout()
        self.subject_label = QLabel("Mesaj Başlığı:")
        self.subject_input = QLineEdit(self)
        subject_layout.addWidget(self.subject_label)
        subject_layout.addWidget(self.subject_input)
        layout.addLayout(subject_layout)

        # Mesaj Kutucuğu (Daha büyük)
        self.message_label = QLabel("Mesajınız:")
        self.message_input = QTextEdit(self)
        self.message_input.setPlaceholderText("Mesajınızı buraya yazınız...")
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)

        # Gönder Butonu
        self.send_button = QPushButton("Gönder", self)
        self.send_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button, alignment=Qt.AlignCenter)

        # Pencereyi oluştur
        self.setLayout(layout)

    def send_message(self):
        """Mesaj gönderildiğinde kullanıcıya başarı mesajı göster."""
        name = self.name_input.text()
        phone = self.phone_input.text()
        subject = self.subject_input.text()
        message = self.message_input.toPlainText()

        if not name or not phone or not subject or not message:
            QMessageBox.warning(self, "Eksik Bilgi", "Lütfen tüm alanları doldurun.")
            return

        # Mesajı service aracılığıyla gönder
        contact_service = ContactUsService()
        result_message = contact_service.send_message(name, phone, subject, message)

        QMessageBox.information(self, "Mesaj Gönderildi", result_message)

        # İletişim sonrası EntryPage'e yönlendir
        from ui.entry_page import EntryPage  # Burada EntryPage'i import ediyoruz
        self.entry_page = EntryPage()  # EntryPage'i başlatıyoruz
        self.entry_page.show()  # EntryPage'i gösteriyoruz
        self.close()  # Bu pencereyi kapat
