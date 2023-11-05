from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from StartingWindow import StartingWindow
from ImageConversionWindow import ImageConversionWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.StartingWindow = StartingWindow()
        self.ImageConversionWindow = ImageConversionWindow()
        self.show_starting_window()

    def show_starting_window(self):
        self.StartingWindow.image_convert_btn.clicked.connect(self.show_image_conversion_window)
        self.StartingWindow.image_convert_btn.clicked.connect(self.StartingWindow.close)
        self.StartingWindow.show()

    def show_image_conversion_window(self):
        self.ImageConversionWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
