import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import SplitFluentWindow, FluentIcon, setThemeColor
from infomation_page import Infomation_Page

from build.ssh import return_gpu_info

class Demo(SplitFluentWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ML Trainer Terminal")
        self.setWindowIcon(QIcon("./resources/images/icon.png"))

        # Show in the center of the screen
        self.resize(800, 600)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        rect = QApplication.desktop().availableGeometry()
        w, h = rect.width(), rect.height()
        self.move(w//2-self.width()//2, h//2-self.height()//2)

        # Change Theme Color
        setThemeColor("#148CD3")

        # Add Sub Page
        self.infomation_page = Infomation_Page(self)
        self.addSubInterface(self.infomation_page, FluentIcon.GLOBE, "Connect Info")
        self.infomation_page.PrimaryPushButton.clicked.connect(self.ssh)
        self.infomation_page.ComboBox.currentIndexChanged.connect(self.clear)


    def ssh(self):
        Node_List = ["GPU01", "GPU02", "GPU03", "GPU04", "GPU05", "GPU06"]
        if self.infomation_page.ComboBox.currentText() == "ALL":
            for Node in Node_List:
                lines = return_gpu_info(Node, self.infomation_page.LineEdit.text(),
                                    self.infomation_page.PasswordLineEdit.text())
                for line in lines:
                    self.infomation_page.results_info.appendPlainText(line)
        else:
            lines = return_gpu_info(self.infomation_page.ComboBox.currentText(),
                                    self.infomation_page.LineEdit.text(),
                                    self.infomation_page.PasswordLineEdit.text())
            for line in lines:
                self.infomation_page.results_info.appendPlainText(line)
    
    def clear(self):
        self.infomation_page.results_info.clear()





if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    main_window = Demo()
    main_window.show()
    app.exec()