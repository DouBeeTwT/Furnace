# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Github\Trainer_GUI\resources\UI\Trainer_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Trainer_Page(object):
    def setupUi(self, Trainer_Page):
        Trainer_Page.setObjectName("Trainer_Page")
        Trainer_Page.resize(800, 600)
        self.SubtitleLabel = SubtitleLabel(Trainer_Page)
        self.SubtitleLabel.setGeometry(QtCore.QRect(120, 180, 119, 27))
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.LineEdit = LineEdit(Trainer_Page)
        self.LineEdit.setGeometry(QtCore.QRect(260, 180, 128, 33))
        self.LineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LineEdit.setObjectName("LineEdit")
        self.SubtitleLabel_2 = SubtitleLabel(Trainer_Page)
        self.SubtitleLabel_2.setGeometry(QtCore.QRect(120, 230, 119, 27))
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.LineEdit_2 = LineEdit(Trainer_Page)
        self.LineEdit_2.setGeometry(QtCore.QRect(260, 230, 128, 33))
        self.LineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.SubtitleLabel_3 = SubtitleLabel(Trainer_Page)
        self.SubtitleLabel_3.setGeometry(QtCore.QRect(120, 300, 131, 27))
        self.SubtitleLabel_3.setObjectName("SubtitleLabel_3")
        self.LineEdit_3 = LineEdit(Trainer_Page)
        self.LineEdit_3.setGeometry(QtCore.QRect(260, 300, 128, 33))
        self.LineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LineEdit_3.setObjectName("LineEdit_3")
        self.SubtitleLabel_4 = SubtitleLabel(Trainer_Page)
        self.SubtitleLabel_4.setGeometry(QtCore.QRect(470, 140, 181, 27))
        self.SubtitleLabel_4.setObjectName("SubtitleLabel_4")
        self.SubtitleLabel_5 = SubtitleLabel(Trainer_Page)
        self.SubtitleLabel_5.setGeometry(QtCore.QRect(480, 200, 181, 27))
        self.SubtitleLabel_5.setObjectName("SubtitleLabel_5")
        self.SubtitleLabel_6 = SubtitleLabel(Trainer_Page)
        self.SubtitleLabel_6.setGeometry(QtCore.QRect(480, 260, 181, 27))
        self.SubtitleLabel_6.setObjectName("SubtitleLabel_6")
        self.SubtitleLabel_7 = SubtitleLabel(Trainer_Page)
        self.SubtitleLabel_7.setGeometry(QtCore.QRect(480, 330, 181, 27))
        self.SubtitleLabel_7.setObjectName("SubtitleLabel_7")
        self.PrimaryPushButton = PrimaryPushButton(Trainer_Page)
        self.PrimaryPushButton.setGeometry(QtCore.QRect(310, 500, 153, 32))
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")

        self.retranslateUi(Trainer_Page)
        QtCore.QMetaObject.connectSlotsByName(Trainer_Page)

    def retranslateUi(self, Trainer_Page):
        _translate = QtCore.QCoreApplication.translate
        Trainer_Page.setWindowTitle(_translate("Trainer_Page", "Form"))
        self.SubtitleLabel.setText(_translate("Trainer_Page", "Max Epoch"))
        self.LineEdit.setText(_translate("Trainer_Page", "2000"))
        self.SubtitleLabel_2.setText(_translate("Trainer_Page", "Early Stop"))
        self.LineEdit_2.setText(_translate("Trainer_Page", "200"))
        self.SubtitleLabel_3.setText(_translate("Trainer_Page", "Random Seed"))
        self.LineEdit_3.setText(_translate("Trainer_Page", "42"))
        self.SubtitleLabel_4.setText(_translate("Trainer_Page", "Labeled Images"))
        self.SubtitleLabel_5.setText(_translate("Trainer_Page", "Saved at"))
        self.SubtitleLabel_6.setText(_translate("Trainer_Page", "Model Saved at"))
        self.SubtitleLabel_7.setText(_translate("Trainer_Page", "Dataset"))
        self.PrimaryPushButton.setText(_translate("Trainer_Page", "SUBMIT"))
from qfluentwidgets import LineEdit, PrimaryPushButton, SubtitleLabel