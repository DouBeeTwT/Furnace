import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import SplitFluentWindow, FluentIcon, setThemeColor
from build.pages.home_page import Home_Page
from build.pages.infomation_page import Infomation_Page
from build.pages.trainer_page import Trainer_Page
from build.pages.monitor_page import Monitor_Page
from build.pages.prediction_page import Prediction_Page
from build.pages.setting_page import Setting_Page

from build.ssh import return_gpu_info

class Demo(SplitFluentWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ML Trainer Terminal")
        self.setWindowIcon(QIcon("./resources/images/icon.png"))

        # Show in the center of the screen
        self.resize(800, 600)
        rect = QApplication.desktop().availableGeometry()
        w, h = rect.width(), rect.height()
        self.move(w//2-self.width()//2, h//2-self.height()//2)

        # Change Theme Color
        setThemeColor("#148CD3")

        ### Add Sub Page
        # home page
        self.home_page = Home_Page(self)
        self.addSubInterface(self.home_page, FluentIcon.HOME, "Home")

        # infomation page
        self.infomation_page = Infomation_Page(self)
        self.addSubInterface(self.infomation_page, FluentIcon.GLOBE, "Connection")
        self.SubtitleLabels = [self.infomation_page.cuda10, self.infomation_page.cuda11,
                               self.infomation_page.cuda20, self.infomation_page.cuda21,
                               self.infomation_page.cuda30, self.infomation_page.cuda31,
                               self.infomation_page.cuda40, self.infomation_page.cuda41,
                               self.infomation_page.cuda50, self.infomation_page.cuda51,
                               self.infomation_page.cuda60, self.infomation_page.cuda61,
                               self.infomation_page.cuda62, self.infomation_page.cuda63,
                               self.infomation_page.cuda64, self.infomation_page.cuda65,
                               self.infomation_page.cuda66, self.infomation_page.cuda67]
        self.infomation_page.PrimaryPushButton.clicked.connect(self.ssh)
        self.infomation_page.ComboBox.currentIndexChanged.connect(self.color_clear)

        # trainer page
        self.trainer_page = Trainer_Page(self)
        self.addSubInterface(self.trainer_page, FluentIcon.SEND, "Trainer")
        self.trainer_page.SmoothScrollArea.setStyleSheet("""
             SmoothScrollArea{
                background: transparent;
                border: 0px solid #f9f9f9;
             }
        """)
        self.trainer_page.SmoothScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Monitor_Page
        self.monitor_page = Monitor_Page(self)
        self.addSubInterface(self.monitor_page, FluentIcon.VIEW, "Monitor")

        # Prediction Page
        self.prediction_page = Prediction_Page(self)
        self.addSubInterface(self.prediction_page, FluentIcon.PHOTO, "Prediction")

        # Setting Page
        self.setting_page = Setting_Page(self)
        self.addSubInterface(self.setting_page, FluentIcon.SETTING, "Setting", position="Buttom")
        

    def color_change(self, available_list):
        for i in range(len(self.SubtitleLabels)):
            if available_list[i]:
                self.SubtitleLabels[i].setStyleSheet("color:#148CD3")

    def color_clear(self):
        for i in range(len(self.SubtitleLabels)):
            self.SubtitleLabels[i].setStyleSheet("color:black")

    def ssh(self):
        Node_List = ["GPU01", "GPU02", "GPU03", "GPU04", "GPU05", "GPU06"]
        if self.infomation_page.ComboBox.currentText() == "ALL":
            for Node in Node_List:
                lines = return_gpu_info(Node, self.infomation_page.LineEdit.text(),
                                    self.infomation_page.PasswordLineEdit.text())
                self.color_change(lines)
        else:
            lines = return_gpu_info(self.infomation_page.ComboBox.currentText(),
                                    self.infomation_page.LineEdit.text(),
                                    self.infomation_page.PasswordLineEdit.text())
            self.color_change(lines)

    






if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    main_window = Demo()
    main_window.show()
    app.exec()