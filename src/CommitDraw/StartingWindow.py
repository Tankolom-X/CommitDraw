from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class StartingWindow(QMainWindow):
    def __init__(self):
        super(StartingWindow, self).__init__()

        # Load the ui file
        uic.loadUi('../ui/starting_window.ui', self)

        # Define the widgets
        self.image_convert_btn = self.findChild(QPushButton, 'image_convert_btn')
        self.image_label = self.findChild(QLabel, 'image_label')

        pixmap = QPixmap('../../media/preview.png')
        self.image_label.setPixmap(pixmap)
