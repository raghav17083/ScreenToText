import sys
import pyperclip
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class ExampleWindow(QMainWindow):
    def __init__(self,m):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440, 240))    
        self.setWindowTitle("Work Area") 

        # Add text field
        self.text = m
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText(m)
        self.b.move(10,10)
        self.b.resize(400,200)
        pybutton = QPushButton('Copy to clipboard', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(150,50)
        pybutton.move(290, 190)        

    def clickMethod(self):
        pyperclip.copy(self.b.document().toPlainText())

def function3(s):
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow(s)
    mainWin.show()
    sys.exit( app.exec_() )

