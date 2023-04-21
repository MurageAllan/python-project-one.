import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyBrowser")
        self.setWindowIcon(QIcon("icons/python.png"))
        self.setGeometry(200, 200, 900, 600)


        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon('icons/back.png'))
        self.backButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon('icons/reload.png'))
        self.reloadButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.reloadButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon('icons/forward.png'))
        self.forwardButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.forwardButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon('icons/forward.png'))
        self.homeButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.homeButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("sanserif", 18))
        toolbar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon('icons/search.png'))
        self.searchButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.searchButton)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

