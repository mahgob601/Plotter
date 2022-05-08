# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np


class Ui_MainWindow(object):
    def __init__(self):
        self.noSamples = 20
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.InputLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.InputLayout.setContentsMargins(0, 0, 0, 0)
        self.InputLayout.setObjectName("InputLayout")
        self.containerWidget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.containerWidget.setStyleSheet("QWidget#containerWidget{ background-color: rgb(227, 213, 255);}")
        self.containerWidget.setObjectName("containerWidget")
        self.FuncLabel = QtWidgets.QLabel(self.containerWidget)
        self.FuncLabel.setEnabled(True)
        self.FuncLabel.setGeometry(QtCore.QRect(12, 10, 111, 51))
        self.FuncLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FuncLabel.setFont(font)
        self.FuncLabel.setAutoFillBackground(False)
        self.FuncLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(28, 12, 255)")
        self.FuncLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.FuncLabel.setObjectName("FuncLabel")
        self.MinLabel = QtWidgets.QLabel(self.containerWidget)
        self.MinLabel.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.MinLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(28, 12, 255)")
        self.MinLabel.setObjectName("MinLabel")
        self.FuncTB = QtWidgets.QTextEdit(self.containerWidget)
        self.FuncTB.setGeometry(QtCore.QRect(10, 70, 291, 41))
        self.FuncTB.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.FuncTB.setObjectName("FuncTB")

        self.MinTB = QtWidgets.QTextEdit(self.containerWidget)
        self.MinTB.setGeometry(QtCore.QRect(10, 190, 71, 41))
        self.MinTB.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.MinTB.setObjectName("MinTB")

        self.MaxTB = QtWidgets.QTextEdit(self.containerWidget)
        self.MaxTB.setGeometry(QtCore.QRect(170, 190, 71, 41))
        self.MaxTB.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.MaxTB.setObjectName("MaxTB")

        self.MaxLabel = QtWidgets.QLabel(self.containerWidget)
        self.MaxLabel.setGeometry(QtCore.QRect(180, 150, 71, 21))
        self.MaxLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(28, 12, 255)")
        self.MaxLabel.setObjectName("MaxLabel")
        self.plotButton = QtWidgets.QPushButton(self.containerWidget)
        self.plotButton.setGeometry(QtCore.QRect(80, 300, 101, 51))
        self.plotButton.setStyleSheet("""
        QPushButton::hover
         {
         background-color : lightgreen;
         }
        
        """)
        self.plotButton.setObjectName("plotButton")
        self.FuncLabel.raise_()
        self.MinLabel.raise_()
        self.MinTB.raise_()
        self.MaxTB.raise_()
        self.MaxLabel.raise_()
        self.FuncTB.raise_()
        self.plotButton.raise_()
        self.InputLayout.addWidget(self.containerWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(370, 10, 481, 471))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.GraphLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.GraphLayout.setContentsMargins(0, 0, 0, 0)
        self.GraphLayout.setObjectName("GraphLayout")
        self.graphWidget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.graphWidget.setObjectName("graphWidget")
        self.GraphLayout.addWidget(self.graphWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.plotButton.clicked.connect(lambda x: self.on_click_plot())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FuncLabel.setText(_translate("MainWindow", "Function"))
        self.MinLabel.setText(_translate("MainWindow", "Min"))
        self.FuncTB.setPlaceholderText(_translate("MainWindow", "Enter Your Function Here e.g. 2^x"))
        self.MinTB.setPlaceholderText(_translate("MainWindow", "Start"))
        self.MaxTB.setPlaceholderText(_translate("MainWindow", "End"))
        self.MaxLabel.setText(_translate("MainWindow", "Max"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
        
        
    def on_click_plot(self):
        eqn = self.FuncTB.toPlainText()
        minVal = self.MinTB.toPlainText()
        maxVal = self.MaxTB.toPlainText()

        print(eqn+" "+minVal+" " + maxVal)


        if(eqn == "" or minVal == "" or maxVal == ""):
            msg = QMessageBox()
            msg.setText("Empty Value: You must enter the equation, min and max values")
            msg.setWindowTitle("Error")
            msg.exec_()


        else:
            try:
                minVal = float(minVal)
                maxVal = float(maxVal)
                print(minVal, type(minVal))
                stepSize = (maxVal - minVal) / self.noSamples    # taking 20 samples
                xValues = (np.arange(minVal, maxVal, stepSize)).tolist()
                print(xValues)
                self.f_x(xValues, eqn)
            except:
                msg = QMessageBox()
                msg.setText("Incorrect Value of min/max")
                msg.setWindowTitle("Error")
                msg.exec_()


    def f_x(self, xValues, eqn):
        if("^" in eqn):
            eqn = eqn.replace("^","**")
        print(eqn)

        yValues = [0] * self.noSamples


        try:
            for i in range(self.noSamples):
                temp = eval(eqn,{'x':xValues[i]})
                yValues[i] = temp
            print(yValues)
        except:
            msg1 = QMessageBox()
            msg1.setText("Incorrect Function: Check function format and variables")
            msg1.setWindowTitle("Error")
            msg1.exec_()

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
