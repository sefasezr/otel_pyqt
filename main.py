from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys

app = QApplication(sys.argv)

main_window = MainWindow()

main_window.show()
sys.exit(app.exec_())