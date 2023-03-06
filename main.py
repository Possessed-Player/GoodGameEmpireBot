import pyautogui as pag
import cv2 as cv
import numpy as np
import configparser
import threading
from time import sleep
from random import choice
from os.path import isfile
from pynput.keyboard import Key, Listener
from PyQt5 import QtCore, QtGui, QtWidgets

SCALE = 2
S_SCALE = 1

PREF_PATH = "pref.ini"
if not isfile(PREF_PATH):
    BC = {
    "C1_x" : "0",
    "C1_y" : "0",
    "C2_x" : "0",
    "C2_y" : "0",
    "C3_x" : "0",
    "C3_y" : "0",
    "C4_x" : "0",
    "C4_y" : "0",
    "C5_x" : "0",
    "C5_y" : "0",
    "C6_x" : "0",
    "C6_y" : "0",
    "C7_x" : "0",
    "C7_y" : "0",
    "C8_x" : "0",
    "C8_y" : "0",
    "C9_x" : "0",
    "C9_y" : "0",
    "C10_x" : "0",
    "C10_y" : "0",
    "Slot" : "1"
    }
    FI = {
    "C1_x" : "0",
    "C1_y" : "0",
    "C2_x" : "0",
    "C2_y" : "0",
    "C3_x" : "0",
    "C3_y" : "0",
    "C4_x" : "0",
    "C4_y" : "0",
    "C5_x" : "0",
    "C5_y" : "0",
    "C6_x" : "0",
    "C6_y" : "0",
    "C7_x" : "0",
    "C7_y" : "0",
    "C8_x" : "0",
    "C8_y" : "0",
    "C9_x" : "0",
    "C9_y" : "0",
    "C10_x" : "0",
    "C10_y" : "0",
    "Slot" : "2"    
    }
    NM = {
    "C1_x" : "0",
    "C1_y" : "0",
    "C2_x" : "0",
    "C2_y" : "0",
    "C3_x" : "0",
    "C3_y" : "0",
    "C4_x" : "0",
    "C4_y" : "0",
    "Slot" : "3"
    }
    SI = {
    "C1_x" : "0",
    "C1_y" : "0",
    "C2_x" : "0",
    "C2_y" : "0",
    "C3_x" : "0",
    "C3_y" : "0",
    "C4_x" : "0",
    "C4_y" : "0",
    "Slot" : "4"
    }
else:
    config = configparser.ConfigParser()
    config.read(PREF_PATH)
    BC = config['BC']
    FI = config['FI']
    NM = config['NM']
    SI = config['SI']
 
ALL = {
    0 : BC,
    1 : FI,
    2 : NM,
    3 : SI
}


def save_changes():
    config = configparser.ConfigParser()
            
    config['BC'] = BC
    config['FI'] = FI
    config['NM'] = NM
    config['SI'] = SI
    
    with open(PREF_PATH, 'w') as configfile:
        config.write(configfile)
        

class Ui_cordDialog(object):
    def setupUi(self, cordDialog, i, cn):
        cordDialog.setObjectName("cordDialog")
        cordDialog.resize(int(378 * SCALE), int(154 * SCALE))
        cordDialog.setMaximumSize(QtCore.QSize(int(378 * SCALE), int(154 * SCALE)))
        cordDialog.setMinimumSize(QtCore.QSize(int(378 * SCALE), int(154 * SCALE)))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cordDialog.setWindowIcon(icon)
        self.spinBox = QtWidgets.QSpinBox(cordDialog)
        self.spinBox.setGeometry(QtCore.QRect(int(80 * SCALE), int(30 * SCALE), int(111 * SCALE), int(41 * SCALE)))
        self.spinBox.setMaximum(1000000)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setFocus(True)
        font = QtGui.QFont()
        font.setPointSize(int(8 * SCALE))
        self.spinBox.setFont(font)
        self.spinBox_2 = QtWidgets.QSpinBox(cordDialog)
        self.spinBox_2.setGeometry(QtCore.QRect(int(250 * SCALE), int(30 * SCALE), int(111 * SCALE), int(41 * SCALE)))
        self.spinBox_2.setMaximum(1000000)
        self.spinBox_2.setObjectName("spinBox_2")
        font = QtGui.QFont()
        font.setPointSize(int(8 * SCALE))
        self.spinBox_2.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(cordDialog)
        self.buttonBox.setGeometry(QtCore.QRect(int(20 * SCALE), int(110 * SCALE), int(341 * SCALE), int(32 * SCALE)))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(cordDialog)
        self.label.setGeometry(QtCore.QRect(int(30 * SCALE), int(30 * SCALE), int(111 * SCALE), int(41 * SCALE)))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * SCALE))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(cordDialog)
        self.label_2.setGeometry(QtCore.QRect(int(210 * SCALE), int(30 * SCALE), int(111 * SCALE), int(41 * SCALE)))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * SCALE))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        

        self.retranslateUi(cordDialog)
        self.buttonBox.accepted.connect(lambda : self.save(cordDialog.accept, i, cn))
        self.buttonBox.rejected.connect(cordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(cordDialog)

    def retranslateUi(self, cordDialog):
        _translate = QtCore.QCoreApplication.translate
        cordDialog.setWindowTitle(_translate("cordDialog", "Type new coordinates"))
        self.label.setText(_translate("cordDialog", "X :"))
        self.label_2.setText(_translate("cordDialog", "Y :"))
		
    def save(self, func, i, cn):        
        ALL[i]['C' + str(cn) + '_x'] = str(self.spinBox.value())
        ALL[i]['C' + str(cn) + '_y'] = str(self.spinBox_2.value())
        
        save_changes()
        func()

class Ui_prefDialog(object):
    def setupUi(self, prefDialog, i):
        prefDialog.setObjectName("prefDialog")
        prefDialog.resize(int(442 * S_SCALE), int(742 * S_SCALE))
        prefDialog.setMaximumSize(QtCore.QSize(int(442 * S_SCALE), int(742 * S_SCALE)))
        prefDialog.setMinimumSize(QtCore.QSize(int(442 * S_SCALE), int(742 * S_SCALE)))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prefDialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(prefDialog)
        self.buttonBox.setGeometry(QtCore.QRect(int(70 * S_SCALE), int(700 * S_SCALE), int(341 * S_SCALE), int(32 * S_SCALE)))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(prefDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(int(9 * S_SCALE), int(9 * S_SCALE), int(421 * S_SCALE), int(681 * S_SCALE)))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, int(5 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, int(1 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, int(9 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda : self.showNewCordsDialog(i, 9))
        self.gridLayout.addWidget(self.pushButton_9, int(8 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, int(2 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, int(7 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, int(5 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, int(4 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, int(3 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, int(9 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, int(3 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, int(8 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda : self.showNewCordsDialog(i, 6))
        self.gridLayout.addWidget(self.pushButton_6, int(5 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda : self.showNewCordsDialog(i, 3))
        self.gridLayout.addWidget(self.pushButton_3, int(2 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda : self.showNewCordsDialog(i, 5))
        self.gridLayout.addWidget(self.pushButton_5, int(4 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, int(6 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda : self.showNewCordsDialog(i, 2))
        self.gridLayout.addWidget(self.pushButton_2, int(1 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda : self.showNewCordsDialog(i, 4))
        self.gridLayout.addWidget(self.pushButton_4, int(3 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda : self.showNewCordsDialog(i, 8))
        self.gridLayout.addWidget(self.pushButton_8, int(7 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.showNewCordsDialog(i, 1))
        self.gridLayout.addWidget(self.pushButton, 0, int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, int(7 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, int(6 * S_SCALE), 0, int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, int(8 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, int(4 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda : self.showNewCordsDialog(i, 7))
        self.gridLayout.addWidget(self.pushButton_7, int(6 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(int(16 * S_SCALE))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda : self.showNewCordsDialog(i, 10))
        self.gridLayout.addWidget(self.pushButton_10, int(9 * S_SCALE), int(2 * S_SCALE), int(1 * S_SCALE), int(1 * S_SCALE))
        self.spinBox = QtWidgets.QSpinBox(prefDialog)
        self.spinBox.setGeometry(QtCore.QRect(int(150 * S_SCALE), int(700 * S_SCALE), int(51 * S_SCALE), int(31 * S_SCALE)))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setValue(int(ALL[i]['Slot']))
        self.spinBox.setObjectName("spinBox")
        font = QtGui.QFont()
        font.setPointSize(int(8 * S_SCALE))
        self.spinBox.setFont(font)
        self.label_21 = QtWidgets.QLabel(prefDialog)
        self.label_21.setGeometry(QtCore.QRect(int(10 * S_SCALE), int(700 * S_SCALE), int(111 * S_SCALE), int(31 * S_SCALE)))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(int(16 * S_SCALE))
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        
        if i > 1:
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.pushButton_9.setEnabled(False)
            self.pushButton_10.setEnabled(False)

        self.retranslateUi(prefDialog, i)
        self.buttonBox.rejected.connect(prefDialog.reject)
        self.buttonBox.accepted.connect(lambda : self.accept(prefDialog.accept, i))
        QtCore.QMetaObject.connectSlotsByName(prefDialog)

    def retranslateUi(self, prefDialog, i):
        _translate = QtCore.QCoreApplication.translate
        prefDialog.setWindowTitle(_translate("prefDialog", "Settings"))
        self.label_6.setText(_translate("prefDialog", "Castle 6"))
        self.label_2.setText(_translate("prefDialog", "Castle 2"))
        self.label.setText(_translate("prefDialog", "Castle 1"))
        self.label_20.setText(_translate("prefDialog", (str(ALL[i]["C10_x"]) + ", " + str(ALL[i]["C10_y"]) if i < 2 else "0, 0")))
        self.pushButton_9.setText(_translate("prefDialog", "Change"))
        self.label_3.setText(_translate("prefDialog", "Castle 3"))
        self.label_8.setText(_translate("prefDialog", "Castle 8"))
        self.label_16.setText(_translate("prefDialog", (str(ALL[i]["C6_x"]) + ", " + str(ALL[i]["C6_y"]) if i < 2 else "0, 0")))
        self.label_5.setText(_translate("prefDialog", "Castle 5"))
        self.label_14.setText(_translate("prefDialog", str(ALL[i]["C4_x"]) + ", " + str(ALL[i]["C4_y"])))
        self.label_10.setText(_translate("prefDialog", "Castle 10"))
        self.label_11.setText(_translate("prefDialog", str(ALL[i]["C1_x"]) + ", " + str(ALL[i]["C1_y"])))
        self.label_4.setText(_translate("prefDialog", "Castle 4"))
        self.label_9.setText(_translate("prefDialog", "Castle 9"))
        self.pushButton_6.setText(_translate("prefDialog", "Change"))
        self.pushButton_3.setText(_translate("prefDialog", "Change"))
        self.pushButton_5.setText(_translate("prefDialog", "Change"))
        self.label_17.setText(_translate("prefDialog", (str(ALL[i]["C7_x"]) + ", " + str(ALL[i]["C7_y"]) if i < 2 else "0, 0")))
        self.pushButton_2.setText(_translate("prefDialog", "Change"))
        self.pushButton_4.setText(_translate("prefDialog", "Change"))
        self.label_13.setText(_translate("prefDialog", str(ALL[i]["C3_x"]) + ", " + str(ALL[i]["C3_y"])))
        self.label_12.setText(_translate("prefDialog", str(ALL[i]["C2_x"]) + ", " + str(ALL[i]["C2_y"])))
        self.pushButton_8.setText(_translate("prefDialog", "Change"))
        self.pushButton.setText(_translate("prefDialog", "Change"))
        self.label_18.setText(_translate("prefDialog", (str(ALL[i]["C8_x"]) + ", " + str(ALL[i]["C8_y"]) if i < 2 else "0, 0")))
        self.label_7.setText(_translate("prefDialog", "Castle 7"))
        self.label_19.setText(_translate("prefDialog", (str(ALL[i]["C9_x"]) + ", " + str(ALL[i]["C9_y"]) if i < 2 else "0, 0")))
        self.label_15.setText(_translate("prefDialog", (str(ALL[i]["C5_x"]) + ", " + str(ALL[i]["C5_y"]) if i < 2 else "0, 0")))
        self.pushButton_7.setText(_translate("prefDialog", "Change"))
        self.pushButton_10.setText(_translate("prefDialog", "Change"))
        self.label_21.setText(_translate("prefDialog", "Preset Slot :"))
		
    def accept(self, func, i):
        new_slot = self.spinBox.value()
        
        ALL[i]['Slot'] = str(new_slot)
        
        save_changes()
        func()
        
        
    def showNewCordsDialog(self, i, cn):
        dialog = QtWidgets.QDialog()
        ui = Ui_cordDialog()
        ui.setupUi(dialog, i, cn)
        res = dialog.exec_()
        
        if res == 1:
            eval("self.label_" + ("1" + str(cn) if cn < 10 else "20") + ".setText('" + str(ALL[i]["C" + str(cn) + "_x"]) + ", " + str(ALL[i]["C" + str(cn) + "_y"]) + "')")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(int(264 * SCALE), int(150 * SCALE))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(int(264 * SCALE), int(150 * SCALE)))
        MainWindow.setMinimumSize(QtCore.QSize(int(264 * SCALE), int(150 * SCALE)))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(int(10 * SCALE), int(10 * SCALE), int(201 * SCALE), int(31 * SCALE)))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Bloodcrow", "Foreign Invasion", "Nomad", "Samurai Invasion"])
        font = QtGui.QFont()
        font.setPointSize(int(8 * SCALE))
        self.comboBox.setFont(font)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(int(220 * SCALE), int(10 * SCALE), int(31 * SCALE), int(31 * SCALE)))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("media/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.openSettingsDialog)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(int(10 * SCALE), int(60 * SCALE), int(241 * SCALE), int(41 * SCALE)))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.prerun)
        font = QtGui.QFont()
        font.setPointSize(int(8 * SCALE))
        self.pushButton.setFont(font)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(int(10 * SCALE), int(107 * SCALE), int(241 * SCALE), int(21 * SCALE)))
        font = QtGui.QFont()
        font.setPointSize(int(8 * SCALE))
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, int(264 * SCALE), int(21 * SCALE)))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        font = QtGui.QFont()
        font.setPointSize(int(8 * SCALE))
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)
        
        
        tod = ("Ready!", "Welcome!", "All set!", "Greetings!",
               "Tip: Press 'esc' to stop the bot", 
               "Tip: Click on the game window after running",
               "Tip: Bot takes longer to stop if sleeping",
               "Tip: You can set same preset for all events", 
               "Tip: make sure all castles are Visible",
               "Tip: make sure all castles are Extinguished",
               "Tip: Run for 6-8 hrs maximum to reduce ban %")
        
        if not isfile(PREF_PATH):
            self.statusbar.showMessage("Please setup castles coords before running!")
            self.pushButton.setEnabled(False)
        else:
            self.statusbar.showMessage(choice(tod))
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hisham GGE Bot"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.checkBox.setText(_translate("MainWindow", "Big Monitor"))
		
    def openSettingsDialog(self):
        prefDialog = QtWidgets.QDialog()
        ui = Ui_prefDialog()
        ui.setupUi(prefDialog, self.comboBox.currentIndex())
        prefDialog.exec_()
            
        
        if not self.pushButton.isEnabled():
            if isfile(PREF_PATH):
                self.pushButton.setEnabled(True)
                self.statusbar.showMessage("Ready!")
                
    def run(self):
        def find_object(file):
            img = pag.screenshot()
            img = img.convert('RGB')
            img = np.array(img)
            img_rgb = img[:, :, ::-1].copy()
            img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
            template = cv.imread("objects/" + file,0)
            w, h = template.shape[::-1]
            
            res = cv.matchTemplate(img_gray,template,cv.TM_SQDIFF_NORMED)
            mn,_,mnLoc,_ = cv.minMaxLoc(res)
            
            print(file, "->", mn)

            if mn < 0.007:
                return mnLoc
            else:
                return False
                
        def press(key):
            pag.keyDown(key)
            pag.keyUp(key)
            
        def click(x, y):
            if self.checkBox.isChecked():
                x = int(x * 1.25)
                y = int(y * 1.25)
                
            pag.moveTo(x, y, 0.25, pag.easeOutQuad)
            pag.mouseDown()
            pag.mouseUp()
            
        def repeat(func, rslt):
            for i in range(0, 10):
                if (func() != False) != (not rslt):
                    return True
                elif i > 2:
                    boxCheck()
                
                sleep(0.5)
                
            return False
            
        def enter_target_info(x, y):
            press("tab")
            pag.write(x)
            press("tab")
            pag.write(y)
            press("enter")
            sleep(0.5)
            press("tab")
            pag.write(x)
            press("tab")
            pag.write(y)
            press("enter")
            sleep(1)
            
            if findClick_object("target.bmp") == False: return False
            
            return repeat(lambda: find_object("success_targselect.bmp"), True)
            
        def findClick_object(o, x=0, y=0):
            cords = find_object(o)
            
            if cords == False: return False
            
            click(cords[0] + x, cords[1] + y)
            
            
        def select_preset(i):
            cords = find_object("drop_preset.bmp")
            
            if cords == False: return False
            
            click(cords[0] - 50, cords[1] + 60)
            sleep(1)
            if self.checkBox.isChecked():
                pag.move(0, -(int(22 * 1.25) * i))
            else:
                pag.move(0, -(22 * i))
            sleep(0.25)
            pag.click()
            
            self.preset_ready = True
            
            
        
        def boxCheck():
            x = 0
            y = 0
            confirmBox = find_object("reward.bmp")
            
            if confirmBox == False:
                confirmBox = find_object("reward2.bmp")
                if confirmBox == False:
                    confirmBox = find_object("confirm2.bmp")
                    if confirmBox == False:
                        confirmBox = find_object("reward3.bmp")
                    else:
                        x = 30
                        y = 60
                else:
                    x = 50
                    y = 50
            else:
                x = 170
                y = 20
            
            while confirmBox != False:
                click(confirmBox[0] + x, confirmBox[1] + y)
                sleep(3)
                confirmBox = find_object("reward.bmp")

                if confirmBox == False:
                    confirmBox = find_object("reward2.bmp")
                    if confirmBox == False:
                        confirmBox = find_object("confirm2.bmp")
                        if confirmBox != False:
                            x = 50
                            y = 10
                        else:
                            confirmBox = find_object("reward3.bmp")
                            if confirmBox != False:
                                x = 30
                                y = 60
                    else:
                        x = 50
                        y = 50
                else:
                    x = 170
                    y = 20
                    
            
        def extinguish(x, y):
            def extingush_on():
                return find_object("skipper_btn.bmp") != False
                
            def timer_done():
                return find_object("success_targselect.bmp") != False
                
            def skip_time():
                findClick_object("skipper_btn.bmp", 10, 5)
                sleep(1)
                while find_object("skipper_leftarrow.bmp") == False:
                    boxCheck()
                    findClick_object("skipper_btn.bmp", 10, 5)
                    
                findClick_object("skipper_leftarrow.bmp", 15, 25)
                sleep(1)
                while find_object("30min_skipper.bmp") == False:
                    boxCheck()
                    findClick_object("skipper_leftarrow.bmp", 15, 25)
                    
                boxCheck()
                findClick_object("1hr_skipper.bmp", 75, 15)
                sleep(2)
                while not timer_done():
                    boxCheck()
                    findClick_object("30min_skipper.bmp", 75, 15)
                    sleep(2)
            
            extinguished = False
            
            while not extinguished:
                if not self.on: return False
                boxCheck()
                
                press("tab")
                pag.write(x)
                press("tab")
                pag.write(y)
                press("enter")
                sleep(0.5)
                press("tab")
                pag.write(x)
                press("tab")
                pag.write(y)
                press("enter")
                sleep(1)
                findClick_object("target.bmp")
                sleep(2)
                
                if repeat(extingush_on, True):
                    skip_time()
                    extinguished = True
                else:
                    boxCheck()
                    cord = find_object("close2.bmp")
                    while cord != False:
                        click(cord[0], cord[1])
                        sleep(1)
                        boxCheck()
                        cord = find_object("close2.bmp")
                        

                        
                    sleep(15)
            
            
            return True
        
        
        def waitFor_reappear(x, y):
            disappeared = False
            
            self.statusbar.showMessage("Attack didn't land yet, sleeping...")
            while not disappeared and not self.attack_landed:
                if not self.on: return False
                boxCheck()
                
                press("tab")
                pag.write(x)
                press("tab")
                pag.write(y)
                press("enter")
                sleep(0.5)
                press("tab")
                pag.write(x)
                press("tab")
                pag.write(y)
                press("enter")
                sleep(1)
                
                boxCheck()
                
                if find_object("target.bmp") != False:
                    sleep(60)
                else:
                    disappeared = True
                    
            
            self.statusbar.showMessage("Castle didn't appear yet, sleeping...")            
            while disappeared:
                if not self.on: return False
                boxCheck()
                
                press("tab")
                pag.write(x)
                press("tab")
                pag.write(y)
                press("enter")
                sleep(0.5)
                press("tab")
                pag.write(x)
                press("tab")
                pag.write(y)
                press("enter")
                sleep(1)
                
                boxCheck()
                
                if find_object("target.bmp") == False:
                    sleep(300)
                else:
                    disappeared = False
            
            self.attack_landed = True
            
            return True
            
        def select_speedup(i):
            cords = find_object("confirm3.bmp")
            
            if cords == False: return False
            
            if i > 1:
                click(cords[0] - 300, cords[1] - 200)
            else:
                click(cords[0] + 100, cords[1] - 200)
                
            sleep(0.5)
            
            click(cords[0], cords[1])
            
            sleep(1)
            
            return repeat(lambda: find_object("success_attack.bmp"), False)

        
        def selector(i):
            if i > 1 and not self.firstRotation:
                return extinguish(ALL[i]["C" + str(castle) + "_x"], ALL[i]["C" + str(castle) + "_y"])
            elif i <= 1 and not self.firstRotation:
                return waitFor_reappear(ALL[i]["C" + str(castle) + "_x"], ALL[i]["C" + str(castle) + "_y"])
            else:
                sleep(5)
                return True
        
        def open_attackWin():
            if findClick_object("confirm.bmp") == False: return False
            
            sleep(2)
            
            return repeat(lambda: find_object("use_preset.bmp"), True)
            
        
        def apply_preset():
            if findClick_object("use_preset.bmp", x=10, y=5) == False: return False
            
            sleep(1)
            
            return repeat(lambda: find_object("failed_preset_use.bmp"), False)
        
        def attack():
            if findClick_object("start_attack.bmp", x=50, y=10) == False: return False
            
            sleep(1)
            
            return repeat(lambda: find_object("success_attack.bmp"), True)
        
        i = self.comboBox.currentIndex()        
        self.preset_ready = False
        self.attack_landed = False
        self.firstRotation = True
        #fcounter = 0
        castle = 1
        max = (4 if i > 1 else 10)
        cur_task = 0
        tasks = {
            0 : lambda : selector(i),
            1 : lambda : enter_target_info(ALL[i]["C" + str(castle) + "_x"], ALL[i]["C" + str(castle) + "_y"]),
            2 : lambda : open_attackWin(),
            3 : lambda : select_preset(int(ALL[i]['Slot'])),
            4 : lambda : apply_preset(),
            5 : lambda : attack(),
            6 : lambda : select_speedup(i)
        }
        
        def next_task():
            if cur_task == 3 and self.preset_ready: return True
            if cur_task == 1 and i > 1 and not self.firstRotation: return True
            print(cur_task)
            return tasks[cur_task]() != False
        
        
        #def reset():
        #    close = True
        #    while close != False:
        #        for i in range(1, 6):
        #            close = find_object("sqr_close_" + str(i) +".bmp")
        #            if close != False:
        #                break
        #        click(close[0], close[1])
        #        sleep(1)
        #    
        #    cur_task = 0

        while self.on:
            if next_task() != False:
                #fcounter = 0
                if cur_task == (len(tasks) - 1):
                    cur_task = 0
                    
                    if castle == max:
                        self.firstRotation = False
                        castle = 1
                    else:
                        castle += 1
                        
                else:
                    cur_task += 1
            else:
                boxCheck()
            #else:
            #    if fcounter > 2:
            #        fcounter = 0
            #        reset()
            #    else:
            #        fcounter += 1
                    
            
            
            
        self.toolButton.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.checkBox.setEnabled(True)
        self.statusbar.showMessage("Ready!")

    def kb_listener(self):
        def on_release(key):
            if key == Key.esc:
                self.on = False
                self.statusbar.showMessage("Stopping...")
                return False


        with Listener(on_release=on_release) as listener:
            listener.join()
    
    def prerun(self):
        self.on = True
       
        kbd_thrd = threading.Thread(target=self.kb_listener, args=())
        run_thrd = threading.Thread(target=self.run, args=())
        run_thrd.start()
        kbd_thrd.start()
        
        self.toolButton.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.checkBox.setEnabled(False)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
