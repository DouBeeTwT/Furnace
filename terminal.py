import sys
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import SplitFluentWindow, FluentIcon, setThemeColor
from build.pages.home_page import Home_Page
from build.pages.infomation_page import Infomation_Page
from build.pages.trainer_page import Trainer_Page
from build.pages.monitor_page import Monitor_Page
from build.pages.prediction_page import Prediction_Page
from build.pages.setting_page import Setting_Page

from build.ssh import *
from build.config import *

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
        self.infomation_page.PrimaryPushButton.clicked.connect(self.cuda_available_test)
        self.infomation_page.ComboBox.currentIndexChanged.connect(self.color_clear)
        
        # trainer page
        self.trainer_page = Trainer_Page(self)
        self.addSubInterface(self.trainer_page, FluentIcon.SEND, "Trainer")
        self.trainer_page.RandomSeedButton.setStyleSheet("PrimaryPushButton{border-image: url(./resources/images/random.png)}")
        self.trainer_page.RandomSeedButton.clicked.connect(self.rollrandomseed)
        self.trainer_page.RandomSeedBox.textChanged.connect(self.autofillpathway)
        self.trainer_page.ModelBox.textChanged.connect(self.autofillpathway)
        self.trainer_page.FigureSizeBox.textChanged.connect(self.autofillpathway)
        self.trainer_page.LabeledImagesBox.textChanged.connect(self.autofillpathway)
        self.trainer_page.SubmmitButton.clicked.connect(self.submit)

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

    def cuda_available_test(self):
        if self.infomation_page.ComboBox.currentText() == "ALL":
            for index in range(1, self.infomation_page.ComboBox.count()):
                ssh = SSH_Client(ip=login["Hostname"],
                             port="2223"+self.infomation_page.ComboBox.itemText(index)[-1],
                             username=self.infomation_page.UsernameBox.text(),
                             password=self.infomation_page.PasswordBox.text())
                ssh.connect()
                cuda_available_list = ssh.cuda_available_test()
                ssh.close()
                self.color_change(cuda_available_list)
        else:
            ssh = SSH_Client(ip=login["Hostname"],
                             port="2223"+self.infomation_page.ComboBox.currentText()[-1],
                             username=self.infomation_page.UsernameBox.text(),
                             password=self.infomation_page.PasswordBox.text())
            ssh.connect()
            cuda_available_list = ssh.cuda_available_test()
            ssh.close()
            self.color_change(cuda_available_list)

    def autofillpathway(self):
        Dataset_Name = self.trainer_page.LabeledImagesBox.text().split("/")[-1]
        Figure_Size = self.trainer_page.FigureSizeBox.text()
        Model_Name = self.trainer_page.ModelBox.text()
        Random_Seed = "Trainer{:03d}".format(int(self.trainer_page.RandomSeedBox.text()))
        self.trainer_page.DataSetBox.setText("Dataset/{:s}/{:s}".format(Figure_Size, Dataset_Name))
        self.trainer_page.OutputPathwayBox.setText("Results/{:s}/{:s}/{:s}".format(Figure_Size, Model_Name, Random_Seed))

    def rollrandomseed(self):
        self.trainer_page.RandomSeedBox.setText(str(randint(1,999)))

    def submit(self):
        ssh = SSH_Client(ip=login["Hostname"], port=login["Port"],
                         username=self.infomation_page.UsernameBox.text(),
                         password=self.infomation_page.PasswordBox.text())
        self.monitor_page.MoniorBox.appendPlainText(ssh.connect())
        ssh.cmd("screen -S {:s}".format(self.trainer_page.RandomSeedBox.text()))
        ssh.close()
        

    
if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    main_window = Demo()
    main_window.show()
    app.exec()