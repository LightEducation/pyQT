from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300) 
    win.setWindowTitle("My first window!") 


    win.show()
    sys.exit(app.exec_())

main()  # make sure to call the function
