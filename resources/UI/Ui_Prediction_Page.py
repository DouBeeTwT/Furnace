# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Github\Trainer_GUI\resources\UI\Prediction_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Prediction_Page(object):
    def setupUi(self, Prediction_Page):
        Prediction_Page.setObjectName("Prediction_Page")
        Prediction_Page.resize(800, 600)
        self.SubtitleLabel = SubtitleLabel(Prediction_Page)
        self.SubtitleLabel.setGeometry(QtCore.QRect(70, 110, 119, 27))
        self.SubtitleLabel.setObjectName("SubtitleLabel")

        self.retranslateUi(Prediction_Page)
        QtCore.QMetaObject.connectSlotsByName(Prediction_Page)

    def retranslateUi(self, Prediction_Page):
        _translate = QtCore.QCoreApplication.translate
        Prediction_Page.setWindowTitle(_translate("Prediction_Page", "Form"))
        self.SubtitleLabel.setText(_translate("Prediction_Page", "Subtitle label"))
from qfluentwidgets import SubtitleLabel
