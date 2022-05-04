from random import random

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Matplotlib Embeding In PyQt5"
        top = 400
        left = 400
        width = 900
        height = 500

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.MyUI()


    def MyUI(self):

        self.canvas = Canvas(self, width=8, height=4)
        self.canvas.move(0,0)

        self.button = QPushButton("Click Me", self)
        self.button.move(100, 450)

        button2 = QPushButton("Click Me Two", self)
        button2.move(250, 450)

        self.button.clicked.connect(lambda x: self.on_click_plot())

    def on_click_plot(self,xValues,yValues):
        x = [random.random() for i in range(1,10)]
        y = [random.random() for j in range(1, 10)]
        self.canvas.plot(xValues,yValues)


class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)


        FigureCanvas.__init__(self, fig)
        self.setParent(parent)


    def plot(self,x,y):

        ax = self.figure.add_subplot(111)
        ax.plot(x, y)




app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()