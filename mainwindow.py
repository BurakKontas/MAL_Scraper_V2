from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QDesktopWidget
from QTCreator.QTCreator import QTCreator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.creator = QTCreator()
        self.initUI()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        self.move(x, y)

    def initUI(self):
        menubar = self.menuBar()

        file_menu = self.creator.QActionCreator(menubar, 'Dosya', ['Yeni', 'Aç', 'Kaydet'], window=self)

        view_menu = self.creator.QActionCreator(menubar, 'Görünüm', ['Tam Ekran', 'Yardım'], window=self)

        layout = QVBoxLayout()

        top_row_layout = QHBoxLayout()

        self.creator.QComboBoxCreator(top_row_layout, 'Seçenek', ['Seçenek A', 'Seçenek B'])

        self.creator.QComboBoxCreator(top_row_layout, 'Seçenek', ['Seçenek A', 'Seçenek B'])

        layout.addLayout(top_row_layout)

        middle_row_layout = QHBoxLayout()

        self.creator.QButtonCreator(middle_row_layout, 'Buton', [
            'Buton 1', 'Buton 2', 'Buton 3'])

        layout.addLayout(middle_row_layout)

        bottom_row_layout = QHBoxLayout()

        # self.creator.QLabelCreator(bottom_row_layout, 'Log', 'Log Ekranı')
        self.creator.QWebEngineViewCreator(bottom_row_layout, 'Log', 'https://myanimelist.net')

        layout.addLayout(bottom_row_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.resize(1920, 1080)
        # self.showFullScreen()
        self.center()
        self.setWindowTitle('MAL Scraper GUI')
