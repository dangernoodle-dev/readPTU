# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyse_ptu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 540)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 00);\n"
"background-color: rgb(255, 246, 249);")
        # Dialog.setSizeGripEnabled(False)
        self.istimetrace = QtWidgets.QCheckBox(Dialog)
        self.istimetrace.setGeometry(QtCore.QRect(20, 110, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.istimetrace.setFont(font)
        self.istimetrace.setStyleSheet("")
        self.istimetrace.setObjectName("istimetrace")
        self.istimetrace.setChecked(True)
        self.isG2 = QtWidgets.QCheckBox(Dialog)
        self.isG2.setGeometry(QtCore.QRect(170, 110, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.isG2.setFont(font)
        self.isG2.setObjectName("isG2")
        self.isG2.setChecked(True)
        self.filepath = QtWidgets.QLineEdit(Dialog)
        self.filepath.setGeometry(QtCore.QRect(110, 60, 301, 25))
        self.filepath.setObjectName("filepath")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 81, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 90, 461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 40, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, -10, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.openfile = QtWidgets.QToolButton(Dialog)
        self.openfile.setGeometry(QtCore.QRect(420, 60, 32, 25))
        self.openfile.setObjectName("openfile")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 451, 291))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.postselect0 = QtWidgets.QLineEdit(self.groupBox)
        self.postselect0.setGeometry(QtCore.QRect(240, 260, 71, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.postselect0.setFont(font)
        self.postselect0.setObjectName("postselect0")
        self.postselect1 = QtWidgets.QLineEdit(self.groupBox)
        self.postselect1.setGeometry(QtCore.QRect(360, 260, 71, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.postselect1.setFont(font)
        self.postselect1.setAutoFillBackground(False)
        self.postselect1.setInputMask("")
        self.postselect1.setFrame(True)
        self.postselect1.setReadOnly(False)
        self.postselect1.setClearButtonEnabled(False)
        self.postselect1.setObjectName("postselect1")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 30, 214, 220))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(241, 30, 195, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.timetraceres = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.timetraceres.setFont(font)
        self.timetraceres.setObjectName("timetraceres")
        self.verticalLayout_2.addWidget(self.timetraceres)
        self.g2timeres = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.g2timeres.setFont(font)
        self.g2timeres.setMinimum(4)
        self.g2timeres.setMaximum(512)
        self.g2timeres.setSingleStep(4)
        self.g2timeres.setProperty("value", 32)
        self.g2timeres.setObjectName("g2timeres")
        self.verticalLayout_2.addWidget(self.g2timeres)
        self.g2timewindow = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.g2timewindow.setFont(font)
        self.g2timewindow.setObjectName("g2timewindow")
        self.verticalLayout_2.addWidget(self.g2timewindow)
        self.zerodelaypos = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.zerodelaypos.setFont(font)
        self.zerodelaypos.setObjectName("zerodelaypos")
        self.verticalLayout_2.addWidget(self.zerodelaypos)
        self.g2algo = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.g2algo.setFont(font)
        self.g2algo.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"background-color: rgb(255, 246, 249);")
        self.g2algo.setObjectName("g2algo")
        self.g2algo.addItem("")
        self.g2algo.addItem("")
        self.verticalLayout_2.addWidget(self.g2algo)
        self.g2postselectionopts = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.g2postselectionopts.setFont(font)
        self.g2postselectionopts.setStyleSheet("background-color: rgb(255, 246, 249);")
        self.g2postselectionopts.setObjectName("g2postselectionopts")
        self.g2postselectionopts.addItem("")
        self.g2postselectionopts.addItem("")
        self.g2postselectionopts.addItem("")
        self.g2postselectionopts.addItem("")
        self.verticalLayout_2.addWidget(self.g2postselectionopts)
        self.isSavedData = QtWidgets.QCheckBox(Dialog)
        self.isSavedData.setGeometry(QtCore.QRect(20, 470, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.isSavedData.setFont(font)
        self.isSavedData.setStyleSheet("")
        self.isSavedData.setObjectName("isSavedData")
        self.isSaveFigure = QtWidgets.QCheckBox(Dialog)
        self.isSaveFigure.setGeometry(QtCore.QRect(20, 500, 201, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.isSaveFigure.setFont(font)
        self.isSaveFigure.setStyleSheet("")
        self.isSaveFigure.setObjectName("isSaveFigure")
        self.CalculateG2 = QtWidgets.QPushButton(Dialog)
        self.CalculateG2.setGeometry(QtCore.QRect(330, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.CalculateG2.setFont(font)
        self.CalculateG2.setStyleSheet("background-color: rgba(255, 201, 238, 155);")
        self.CalculateG2.setObjectName("CalculateG2")
        self.savebutton = QtWidgets.QPushButton(Dialog)
        self.savebutton.setGeometry(QtCore.QRect(170, 460, 112, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.savebutton.setFont(font)
        self.savebutton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(223, 215, 255);")
        self.savebutton.setObjectName("savebutton")
        self.calculatebar = QtWidgets.QProgressBar(Dialog)
        self.calculatebar.setGeometry(QtCore.QRect(330, 510, 131, 23))
        self.calculatebar.setProperty("value", 0)
        self.calculatebar.setObjectName("calculatebar")
        self.saveprogress = QtWidgets.QProgressBar(Dialog)
        self.saveprogress.setGeometry(QtCore.QRect(170, 510, 120, 23))
        self.saveprogress.setProperty("value", 0)
        self.saveprogress.setObjectName("saveprogress")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.filepath, self.openfile)
        Dialog.setTabOrder(self.openfile, self.istimetrace)
        Dialog.setTabOrder(self.istimetrace, self.isG2)
        Dialog.setTabOrder(self.isG2, self.timetraceres)
        Dialog.setTabOrder(self.timetraceres, self.g2timeres)
        Dialog.setTabOrder(self.g2timeres, self.g2timewindow)
        Dialog.setTabOrder(self.g2timewindow, self.zerodelaypos)
        Dialog.setTabOrder(self.zerodelaypos, self.g2algo)
        Dialog.setTabOrder(self.g2algo, self.g2postselectionopts)
        Dialog.setTabOrder(self.g2postselectionopts, self.postselect0)
        Dialog.setTabOrder(self.postselect0, self.postselect1)
        Dialog.setTabOrder(self.postselect1, self.isSavedData)
        Dialog.setTabOrder(self.isSavedData, self.isSaveFigure)
        Dialog.setTabOrder(self.isSaveFigure, self.savebutton)
        Dialog.setTabOrder(self.savebutton, self.CalculateG2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.istimetrace.setText(_translate("Dialog", "Time trace"))
        self.isG2.setText(_translate("Dialog", "G2"))
        self.label.setText(_translate("Dialog", "Filename"))
        self.label_2.setText(_translate("Dialog", "Analyse PTU"))
        self.openfile.setText(_translate("Dialog", "..."))
        self.groupBox.setTitle(_translate("Dialog", "Parameters"))
        self.postselect0.setText(_translate("Dialog", "0"))
        self.postselect1.setText(_translate("Dialog", "0"))
        self.label_4.setText(_translate("Dialog", "Time trace res (s)"))
        self.label_5.setText(_translate("Dialog", "G2 time res (ps)"))
        self.label_7.setText(_translate("Dialog", "G2 time window (ns)"))
        self.label_6.setText(_translate("Dialog", "Zero Delay Position (ns)"))
        self.label_9.setText(_translate("Dialog", "G2 Algorithm"))
        self.label_8.setText(_translate("Dialog", "G2 Post Selection"))
        self.timetraceres.setText(_translate("Dialog", "0.1"))
        self.g2timewindow.setText(_translate("Dialog", "1000"))
        self.zerodelaypos.setText(_translate("Dialog", "0"))
        self.g2algo.setItemText(0, _translate("Dialog", "symmetric"))
        self.g2algo.setItemText(1, _translate("Dialog", "ring"))
        self.g2postselectionopts.setItemText(0, _translate("Dialog", "None"))
        self.g2postselectionopts.setItemText(1, _translate("Dialog", "above"))
        self.g2postselectionopts.setItemText(2, _translate("Dialog", "below"))
        self.g2postselectionopts.setItemText(3, _translate("Dialog", "between"))
        self.isSavedData.setText(_translate("Dialog", "Saved Data"))
        self.isSaveFigure.setText(_translate("Dialog", "Save Figure"))
        self.CalculateG2.setText(_translate("Dialog", "Calculate"))
        self.savebutton.setText(_translate("Dialog", "Save"))
