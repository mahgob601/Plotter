import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QDesktopWidget
import numpy as np
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):


    def __init__(self):
        super().__init__()
        self.title = 'Function Plotter'
        self.noSamples = 20
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.setWindowTitle(self.title)
        self.center()
        self.resize(800,500)

        #Create Label
        self.Funclabel = QLabel(self)
        self.Funclabel.setText("<b><font style=\"font-size:20px\" color=blue>Function</font></b>")
        self.Funclabel.move(15,10)

        # Creating Function textbox

        self.FuncTextbox = QLineEdit(self)

        self.FuncTextbox.move(20, 60)
        self.FuncTextbox.resize(280, 40)
        f = self.FuncTextbox.font()
        f.setPointSize(12)
        self.FuncTextbox.setFont(f)

        # Creating Min label
        self.Minlabel = QLabel(self)
        self.Minlabel.setText("<b><font style=\"font-size:20px\" color=blue>Min</font></b>")
        self.Minlabel.move(20, 120)

        # Creating Max label
        self.Maxlabel = QLabel(self)
        self.Maxlabel.setText("<b><font style=\"font-size:20px\" color=blue>Max</font></b>")
        self.Maxlabel.move(180, 120)

        # Creating Minimum textbox

        self.MinTextbox = QLineEdit(self)

        self.MinTextbox.move(20, 160)
        self.MinTextbox.resize(70, 40)
        f1 = self.MinTextbox.font()
        f1.setPointSize(12)
        self.MinTextbox.setFont(f1)

        # Creating Maximum textbox

        self.MaxTextbox = QLineEdit(self)

        self.MaxTextbox.move(180, 160)
        self.MaxTextbox.resize(70, 40)
        f1 = self.MaxTextbox.font()
        f1.setPointSize(12)
        self.MaxTextbox.setFont(f1)

        # Create a button in the window
        self.button = QPushButton('Plot', self)
        self.button.move(85, 240)

        # connect button to function on_click
        self.button.clicked.connect(lambda x: self.on_click_plot())
        self.show()

    # @pyqtSlot()
    # def syntCheck(self):
    #     textboxValue = self.textbox.text()
    #     QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
    #                          QMessageBox.Ok)
    #     self.textbox.setText("")

    def on_click_plot(self):
        eqn = self.FuncTextbox.text()
        minVal = self.MinTextbox.text()
        maxVal = self.MaxTextbox.text()


        if(eqn == "" or minVal == "" or maxVal == ""):
            msg = QMessageBox()
            msg.setText("Empty Value: You must enter the equation, min and max values")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            minVal = float(minVal)
            maxVal = float(maxVal)
            print(minVal, type(minVal))
            stepSize = (maxVal - minVal) / self.noSamples    # taking 20 samples


            xValues = (np.arange(minVal,maxVal,stepSize)).tolist()


            print(xValues)
            self.f_x(xValues, eqn)
            print(eqn)

    def f_x(self, xValues, eqn):
        if("^" in eqn):
            eqn = eqn.replace("^","**")
        print(eqn)

        print("Here we go")
        yValues = [0] * self.noSamples
        print(yValues)


        for i in range(self.noSamples):
            temp = eval(eqn,{'x':xValues[i]})
            yValues[i] = temp
        print(yValues)











if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())








