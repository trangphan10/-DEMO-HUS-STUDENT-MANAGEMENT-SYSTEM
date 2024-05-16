from PyQt5 import QtCore,QtGui,QtWidgets
import sys 
import home,login,enter

MainWindow = QtWidgets.QMainWindow()
def HomeUI(): 
    global ui 
    ui = home.Ui_Form()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(enter)
    ui.pushButton_2.clicked.connect(view)
    ui.pushButton_3.clicked.connect(delete)
    MainWindow.show()
def LoginUI(): 
    global ui 
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(home)
    MainWindow.show()
def EnterUI():
    global ui 
    ui = enter.Ui_Form()
    ui.setupUi(MainWindow)
    ui.pushButton_2.connect(home)
    ui.pushButton_3.connect(home)
    
