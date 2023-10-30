from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget

from qfluentwidgets import FluentIcon
from resources.UI.Ui_Information_Page import Ui_Information_Page

class Infomation_Page(QWidget, Ui_Information_Page):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = self.setupUi(self)