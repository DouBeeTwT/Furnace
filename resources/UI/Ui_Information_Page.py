# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Github\Trainer_GUI\resources\UI\Information_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from build.config import *
from resources.UI.Ui_config import Nodes_Items

class Ui_Information_Page(object):
    def setupUi(self, Information_Page):
        Information_Page.setObjectName("Information_Page")
        Information_Page.resize(800, 600)
        Information_Page.setStyleSheet("")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Information_Page)
        self.verticalLayout_4.setContentsMargins(40, 70, 40, 30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Info_head = QtWidgets.QHBoxLayout()
        self.Info_head.setObjectName("Info_head")
        self.BodyLabel = BodyLabel(Information_Page)
        self.BodyLabel.setObjectName("BodyLabel")
        self.Info_head.addWidget(self.BodyLabel)
        self.UsernameBox = LineEdit(Information_Page)
        self.UsernameBox.setObjectName("UsernameBox")
        self.Info_head.addWidget(self.UsernameBox)
        self.BodyLabel_2 = BodyLabel(Information_Page)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.Info_head.addWidget(self.BodyLabel_2)
        self.PasswordBox = PasswordLineEdit(Information_Page)
        self.PasswordBox.setObjectName("PasswordBox")
        self.Info_head.addWidget(self.PasswordBox)
        self.BodyLabel_3 = BodyLabel(Information_Page)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.Info_head.addWidget(self.BodyLabel_3)
        self.ComboBox = ComboBox(Information_Page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBox.sizePolicy().hasHeightForWidth())
        self.ComboBox.setSizePolicy(sizePolicy)
        self.ComboBox.setMinimumSize(QtCore.QSize(90, 0))
        self.ComboBox.setAutoDefault(False)
        self.ComboBox.setObjectName("ComboBox")
        self.Info_head.addWidget(self.ComboBox)
        self.PrimaryPushButton = PrimaryPushButton(Information_Page)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        self.Info_head.addWidget(self.PrimaryPushButton)
        self.verticalLayout_4.addLayout(self.Info_head)
        self.GPU_CUDA = QtWidgets.QHBoxLayout()
        self.GPU_CUDA.setObjectName("GPU_CUDA")
        self.GPU_L = QtWidgets.QVBoxLayout()
        self.GPU_L.setObjectName("GPU_L")
        self.GPU01 = QtWidgets.QGroupBox(Information_Page)
        self.GPU01.setObjectName("GPU01")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.GPU01)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cuda10 = SubtitleLabel(self.GPU01)
        self.cuda10.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda10.setObjectName("cuda10")
        self.horizontalLayout_2.addWidget(self.cuda10)
        self.cuda11 = SubtitleLabel(self.GPU01)
        self.cuda11.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda11.setObjectName("cuda11")
        self.horizontalLayout_2.addWidget(self.cuda11)
        self.GPU_L.addWidget(self.GPU01)
        self.GPU02 = QtWidgets.QGroupBox(Information_Page)
        self.GPU02.setObjectName("GPU02")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.GPU02)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cuda20 = SubtitleLabel(self.GPU02)
        self.cuda20.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda20.setObjectName("cuda20")
        self.horizontalLayout_3.addWidget(self.cuda20)
        self.cuda21 = SubtitleLabel(self.GPU02)
        self.cuda21.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda21.setObjectName("cuda21")
        self.horizontalLayout_3.addWidget(self.cuda21)
        self.GPU_L.addWidget(self.GPU02)
        self.GPU03 = QtWidgets.QGroupBox(Information_Page)
        self.GPU03.setObjectName("GPU03")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.GPU03)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cuda30 = SubtitleLabel(self.GPU03)
        self.cuda30.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda30.setObjectName("cuda30")
        self.horizontalLayout_4.addWidget(self.cuda30)
        self.cuda31 = SubtitleLabel(self.GPU03)
        self.cuda31.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda31.setObjectName("cuda31")
        self.horizontalLayout_4.addWidget(self.cuda31)
        self.GPU_L.addWidget(self.GPU03)
        self.GPU04 = QtWidgets.QGroupBox(Information_Page)
        self.GPU04.setObjectName("GPU04")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.GPU04)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cuda40 = SubtitleLabel(self.GPU04)
        self.cuda40.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda40.setObjectName("cuda40")
        self.horizontalLayout_5.addWidget(self.cuda40)
        self.cuda41 = SubtitleLabel(self.GPU04)
        self.cuda41.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda41.setObjectName("cuda41")
        self.horizontalLayout_5.addWidget(self.cuda41)
        self.GPU_L.addWidget(self.GPU04)
        self.GPU05 = QtWidgets.QGroupBox(Information_Page)
        self.GPU05.setObjectName("GPU05")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.GPU05)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cuda50 = SubtitleLabel(self.GPU05)
        self.cuda50.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda50.setObjectName("cuda50")
        self.horizontalLayout_6.addWidget(self.cuda50)
        self.cuda51 = SubtitleLabel(self.GPU05)
        self.cuda51.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda51.setObjectName("cuda51")
        self.horizontalLayout_6.addWidget(self.cuda51)
        self.GPU_L.addWidget(self.GPU05)
        self.GPU_CUDA.addLayout(self.GPU_L)
        self.GPU_R = QtWidgets.QVBoxLayout()
        self.GPU_R.setObjectName("GPU_R")
        self.GPU06 = QtWidgets.QGroupBox(Information_Page)
        self.GPU06.setObjectName("GPU06")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.GPU06)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Subgroup1 = QtWidgets.QHBoxLayout()
        self.Subgroup1.setObjectName("Subgroup1")
        self.cuda60 = SubtitleLabel(self.GPU06)
        self.cuda60.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda60.setObjectName("cuda60")
        self.Subgroup1.addWidget(self.cuda60)
        self.cuda61 = SubtitleLabel(self.GPU06)
        self.cuda61.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda61.setObjectName("cuda61")
        self.Subgroup1.addWidget(self.cuda61)
        self.verticalLayout.addLayout(self.Subgroup1)
        self.Subgroup2 = QtWidgets.QHBoxLayout()
        self.Subgroup2.setObjectName("Subgroup2")
        self.cuda62 = SubtitleLabel(self.GPU06)
        self.cuda62.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda62.setObjectName("cuda62")
        self.Subgroup2.addWidget(self.cuda62)
        self.cuda63 = SubtitleLabel(self.GPU06)
        self.cuda63.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda63.setObjectName("cuda63")
        self.Subgroup2.addWidget(self.cuda63)
        self.verticalLayout.addLayout(self.Subgroup2)
        self.Subgroup3 = QtWidgets.QHBoxLayout()
        self.Subgroup3.setObjectName("Subgroup3")
        self.cuda64 = SubtitleLabel(self.GPU06)
        self.cuda64.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda64.setObjectName("cuda64")
        self.Subgroup3.addWidget(self.cuda64)
        self.cuda65 = SubtitleLabel(self.GPU06)
        self.cuda65.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda65.setObjectName("cuda65")
        self.Subgroup3.addWidget(self.cuda65)
        self.verticalLayout.addLayout(self.Subgroup3)
        self.Subgroup4 = QtWidgets.QHBoxLayout()
        self.Subgroup4.setObjectName("Subgroup4")
        self.cuda66 = SubtitleLabel(self.GPU06)
        self.cuda66.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda66.setObjectName("cuda66")
        self.Subgroup4.addWidget(self.cuda66)
        self.cuda67 = SubtitleLabel(self.GPU06)
        self.cuda67.setAlignment(QtCore.Qt.AlignCenter)
        self.cuda67.setObjectName("cuda67")
        self.Subgroup4.addWidget(self.cuda67)
        self.verticalLayout.addLayout(self.Subgroup4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.GPU_R.addWidget(self.GPU06)
        self.GPU_R.setStretch(0, 4)
        self.GPU_CUDA.addLayout(self.GPU_R)
        self.GPU_CUDA.setStretch(0, 1)
        self.GPU_CUDA.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.GPU_CUDA)

        self.UsernameBox.setText(login["Username"])
        self.PasswordBox.setText(login["Password"])
        self.ComboBox.addItems(Nodes_Items)
        self.retranslateUi(Information_Page)
        QtCore.QMetaObject.connectSlotsByName(Information_Page)

    def retranslateUi(self, Information_Page):
        _translate = QtCore.QCoreApplication.translate
        Information_Page.setWindowTitle(_translate("Information_Page", "Form"))
        self.BodyLabel.setText(_translate("Information_Page", "User Name"))
        self.BodyLabel_2.setText(_translate("Information_Page", "Password"))
        self.BodyLabel_3.setText(_translate("Information_Page", "Node"))
        self.ComboBox.setText(_translate("Information_Page", "ALL"))
        self.PrimaryPushButton.setText(_translate("Information_Page", "TEST"))
        self.GPU01.setTitle(_translate("Information_Page", "GPU 01"))
        self.cuda10.setText(_translate("Information_Page", "cuda:0"))
        self.cuda11.setText(_translate("Information_Page", "cuda:1"))
        self.GPU02.setTitle(_translate("Information_Page", "GPU 02"))
        self.cuda20.setText(_translate("Information_Page", "cuda:0"))
        self.cuda21.setText(_translate("Information_Page", "cuda:1"))
        self.GPU03.setTitle(_translate("Information_Page", "GPU 03"))
        self.cuda30.setText(_translate("Information_Page", "cuda:0"))
        self.cuda31.setText(_translate("Information_Page", "cuda:1"))
        self.GPU04.setTitle(_translate("Information_Page", "GPU 04"))
        self.cuda40.setText(_translate("Information_Page", "cuda:0"))
        self.cuda41.setText(_translate("Information_Page", "cuda:1"))
        self.GPU05.setTitle(_translate("Information_Page", "GPU 05"))
        self.cuda50.setText(_translate("Information_Page", "cuda:0"))
        self.cuda51.setText(_translate("Information_Page", "cuda:1"))
        self.GPU06.setTitle(_translate("Information_Page", "GPU 06"))
        self.cuda60.setText(_translate("Information_Page", "cuda:0"))
        self.cuda61.setText(_translate("Information_Page", "cuda:1"))
        self.cuda62.setText(_translate("Information_Page", "cuda:2"))
        self.cuda63.setText(_translate("Information_Page", "cuda:3"))
        self.cuda64.setText(_translate("Information_Page", "cuda:4"))
        self.cuda65.setText(_translate("Information_Page", "cuda:5"))
        self.cuda66.setText(_translate("Information_Page", "cuda:6"))
        self.cuda67.setText(_translate("Information_Page", "cuda:7"))
from qfluentwidgets import BodyLabel, ComboBox, LineEdit, PasswordLineEdit, PrimaryPushButton, SubtitleLabel
import resource_rc
