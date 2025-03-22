from PyQt5.QtWidgets import QApplication
from ui.entry_page import EntryPage  # Yeni açılış sayfası
from database import Database  # Veritabanı sınıfı
import sys

# Uygulama başlamadan önce tabloları oluştur
db = Database()
db.create_tables()  # Tabloların oluşturulmasını sağla

# PyQt uygulamasını başlat
app = QApplication(sys.argv)

entry_page = EntryPage()

entry_page.show()
sys.exit(app.exec_())
