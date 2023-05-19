from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from Screens.action_process_screen import ProcessScreen


class SelectScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ana Pencere")
        self.setGeometry(300, 300, 400, 300)

        # İkinci ekranı açmak için bir buton
        self.openprocess_screenButton = QPushButton("İkinci Ekranı Aç", self)
        self.openprocess_screenButton.setGeometry(150, 100, 150, 30)
        self.openprocess_screenButton.clicked.connect(self.open_process_screen)

        # İkinci ekranı temsil edecek pencere
    def open_process_screen(self):
        self.process_screen = ProcessScreen(self)
        self.hide()  # Ana ekranı gizle
        self.process_screen.show()  # İkinci ekranı göster

    def closeEvent(self, event):
        # Ana ekranda X tuşuna basıldığında uygulamayı kapat
        if event.spontaneous() and self.isVisible():
            event.accept()
        else:
            event.ignore()
