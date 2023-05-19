from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ana Pencere")
        self.setGeometry(300, 300, 400, 300)

        # İkinci ekranı açmak için bir buton
        self.openSecondScreenButton = QPushButton("İkinci Ekranı Aç", self)
        self.openSecondScreenButton.setGeometry(150, 100, 150, 30)
        self.openSecondScreenButton.clicked.connect(self.openSecondScreen)

        # İkinci ekranı temsil edecek pencere
        self.secondScreen = SecondScreen(self)

    def openSecondScreen(self):
        self.hide()  # Ana ekranı gizle
        self.secondScreen.show()  # İkinci ekranı göster

    def closeEvent(self, event):
        # Ana ekranda X tuşuna basıldığında uygulamayı kapat
        if event.spontaneous() and self.isVisible():
            event.accept()
        else:
            event.ignore()

class SecondScreen(QMainWindow):
    def __init__(self, mainWin):
        super().__init__()
        self.mainWin = mainWin
        self.initUI()

    def initUI(self):
        self.setWindowTitle("İkinci Ekran")
        self.setGeometry(300, 300, 400, 300)

    def closeEvent(self, event):
        # İkinci ekranda X tuşuna basıldığında sadece ikinci ekranı kapat
        if event.spontaneous():
            self.mainWin.show()  # Ana ekranı göster
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()
