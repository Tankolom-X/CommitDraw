from PyQt5.QtWidgets import QMainWindow, QLineEdit, QCalendarWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import datetime as dt
from ImageConverter import ImageConverter


class ImageConversionWindow(QMainWindow):
    def __init__(self):
        super(ImageConversionWindow, self).__init__()

        # Load the ui file
        uic.loadUi('../ui/image_conversion_window.ui', self)

        # Define the widgets
        self.image_label = self.findChild(QLabel, 'image_label')
        self.image_result_label = self.findChild(QLabel, 'image_result_label')

        self.directory_label = self.findChild(QLabel, 'directory_label')
        self.author_lineEdit = self.findChild(QLineEdit, 'author_lineEdit')
        self.email_lineEdit = self.findChild(QLineEdit, 'email_lineEdit')
        self.calendarWidget = self.findChild(QCalendarWidget, 'calendarWidget')

        self.previous_settings_btn = self.findChild(QPushButton, 'previous_settings_btn')
        self.start_btn = self.findChild(QPushButton, 'start_btn')

        self.image_label.mouseReleaseEvent = self.image_select

        self.calendarWidget.clicked['QDate'].connect(self.date_select)

        self.date = None
        self.image_path = None

    def image_select(self, event):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Images (*.png *.jpg *jpeg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            image_path = dialog.selectedFiles()[0]
            if image_path:
                self.set_image(image_path, 'image_label')
                self.image_path = image_path
                if self.make_image_result() == 'White image':
                    self.error_white_image()

    def set_image(self, filename, label_name):
        pixmap = QPixmap(filename).scaled(459, 63)
        a = self.findChild(QLabel, label_name)
        a.setPixmap(pixmap)

    def error_white_image(self):
        error = QMessageBox()
        error.setWindowTitle('Warning')
        error.setText('Cannot transform white image')
        error.setIcon(QMessageBox.Warning)
        error.exec_()

    def date_select(self):
        selected_date = self.calendarWidget.selectedDate().toString('dd-MM-yyyy').split('-')
        date = dt.datetime(year=int(selected_date[2]), month=int(selected_date[1]), day=int(selected_date[0]), hour=12)

        self.date = date
        if self.make_image_result() == 'White image':
            self.error_white_image()

    def make_image_result(self):
        if self.image_path and self.date:
            image_converter = ImageConverter()
            image = image_converter.make_a_result_image(self.date, self.image_path)
            if image == 'White image':
                return 'White image'
            result_image_path = image_converter.save_result_image(image)
            self.set_image(result_image_path, 'image_result_label')
