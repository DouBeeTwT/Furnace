# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Github\Trainer_GUI\resources\UI\Home_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home_Page(object):
    def setupUi(self, Home_Page):
        Home_Page.setObjectName("Home_Page")
        Home_Page.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home_Page.sizePolicy().hasHeightForWidth())
        Home_Page.setSizePolicy(sizePolicy)
        Home_Page.setMinimumSize(QtCore.QSize(800, 0))
        Home_Page.setMaximumSize(QtCore.QSize(800, 16777215))
        Home_Page.setStyleSheet("")

        self.retranslateUi(Home_Page)
        QtCore.QMetaObject.connectSlotsByName(Home_Page)

    def retranslateUi(self, Home_Page):
        _translate = QtCore.QCoreApplication.translate
        Home_Page.setWindowTitle(_translate("Home_Page", "Form"))
import resource_rc
