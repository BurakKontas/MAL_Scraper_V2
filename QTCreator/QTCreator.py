import os

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QComboBox, QWidget, QAction, QMenuBar, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl
from typing import TypeVar

T = TypeVar('T')
Column = TypeVar('Column', list[str], list[int])


class QTCreator:
    def QActionCreator(self, widget: QMenuBar, name: str, buttons: list, window: QMainWindow, css: str = "") -> QMenuBar:
        menu = widget.addMenu(name)
        self.__apply_css(menu, css)
        for button in buttons:
            action = QAction(button, window)
            menu.addAction(action)
        return menu

    def QButtonCreator(self, name: str, buttons: list, settings: dict = {}, css: str = "") -> list[QPushButton]:
        qbuttons = []
        for button in buttons:
            qButton = QPushButton(button)
            self.__apply_settings(qButton, settings)
            self.__apply_css(qButton, css)
            qbuttons.append(qButton)
        return qbuttons

    def QComboBoxCreator(self, name: str, buttons: list, settings: dict = {}, css: str = "") -> QComboBox:
        qComboBox = QComboBox()
        for button in buttons:
            qComboBox.addItem(button)
            self.__apply_settings(qComboBox, settings)
            self.__apply_css(qComboBox, css)
        return qComboBox

    def QLabelCreator(self, name: str, text: str, settings: dict = {}, css: str = "") -> QLabel:
        qLabel = QLabel(text)
        self.__apply_settings(qLabel, settings)
        self.__apply_css(qLabel, css)
        return qLabel

    def QTextEditCreator(self, name: str, text: str, settings: dict = {}, css: str = "") -> QTextEdit:
        qTextEdit = QTextEdit(text)
        self.__apply_settings(qTextEdit, settings)
        self.__apply_css(qTextEdit, css)
        return qTextEdit

    def QTableWidgetCreator(self, name: str, columns: Column, rows: list[Column], settings: dict = {}, css: str = "") -> QTableWidget:
        table = QTableWidget()
        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)
        for row in rows:
            table.insertRow(0)
            for i in range(len(row)):
                table.setItem(0, i, QTableWidgetItem(str(row[i])))
        self.__apply_settings(table, settings)
        self.__apply_css(table, css)
        return table

    def QWebEngineViewCreator(self, name: str, url: str, settings: dict = {}, css: str = "") -> QWebEngineView:
        os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-logging"
        webview = QWebEngineView()
        url = QUrl(url)
        webview.load(url)
        return webview
    

    def __apply_settings(self, widget: QWidget, settings: dict = {}) -> None:
        try:
            if 'readonly' in settings:
                if settings['readonly'] == True:
                    widget.setReadOnly(True)
            if 'enabled' in settings:
                if settings['enabled'] == False:
                    widget.setEnabled(False)
        except:
            print(widget.objectName, 'için ayarlar uygulanamadı.')

    def __apply_css(self, widget: QWidget, css: str) -> None:
        try:
            widget.setStyleSheet(css)
        except:
            print(widget.objectName, 'için CSS uygulanamadı.')
