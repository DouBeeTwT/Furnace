# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Github\Trainer_GUI\resources\UI\Monitor_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Monitor_Page(object):
    def setupUi(self, Monitor_Page):
        Monitor_Page.setObjectName("Monitor_Page")
        Monitor_Page.resize(800, 600)
        self.ComboBox = ComboBox(Monitor_Page)
        self.ComboBox.setGeometry(QtCore.QRect(180, 70, 331, 32))
        self.ComboBox.setObjectName("ComboBox")
        self.SubtitleLabel = SubtitleLabel(Monitor_Page)
        self.SubtitleLabel.setGeometry(QtCore.QRect(110, 70, 119, 27))
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Monitor_Page)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 110, 651, 421))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.PrimaryPushButton = PrimaryPushButton(Monitor_Page)
        self.PrimaryPushButton.setGeometry(QtCore.QRect(550, 70, 153, 32))
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")

        self.retranslateUi(Monitor_Page)
        QtCore.QMetaObject.connectSlotsByName(Monitor_Page)

    def retranslateUi(self, Monitor_Page):
        _translate = QtCore.QCoreApplication.translate
        Monitor_Page.setWindowTitle(_translate("Monitor_Page", "Form"))
        self.SubtitleLabel.setText(_translate("Monitor_Page", "Job ID"))
        self.PrimaryPushButton.setText(_translate("Monitor_Page", "SHOW"))
from qfluentwidgets import ComboBox, PrimaryPushButton, SubtitleLabel