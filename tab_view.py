from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TabView Example")

        # Ana widget oluşturma
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Ana layout oluşturma
        layout = QVBoxLayout(central_widget)

        # Tab widget oluşturma
        tab_widget = QTabWidget()

        # İlk sekme
        tab1 = QWidget()
        tab_widget.addTab(tab1, "Tab 1")
        label1 = QLabel("Bu Tab 1")
        tab1.layout = QVBoxLayout(tab1)
        tab1.layout.addWidget(label1)
        tab1.setLayout(tab1.layout)

        # İkinci sekme
        tab2 = QWidget()
        tab_widget.addTab(tab2, "Tab 2")
        label2 = QLabel("Bu Tab 2")
        tab2.layout = QVBoxLayout(tab2)
        tab2.layout.addWidget(label2)
        tab2.setLayout(tab2.layout)

        # Tab widget'ı ana layout'a ekleme
        layout.addWidget(tab_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
