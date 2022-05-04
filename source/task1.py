import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QDesktopWidget
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Function Plotter'
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

        # Create a button in the window
        self.button = QPushButton('Plot', self)
        self.button.move(20, 120)

        # connect button to function on_click
        self.button.clicked.connect(self.syntCheck)
        self.show()

    @pyqtSlot()
    def syntCheck(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")

    #def on_click_plot(self):




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())








