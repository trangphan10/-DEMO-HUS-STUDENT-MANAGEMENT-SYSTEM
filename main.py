from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, \
QPushButton,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit, QHBoxLayout
from PyQt5.QtCore import QCoreApplication
import sys 
import home,login,enter
# Xây dựng giao diện
MainWindow = QtWidgets.QMainWindow()
def HomeUI(): 
    global ui 
    ui = home.Ui_Form()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(enter)
    # ui.pushButton_2.clicked.connect(view)
    # ui.pushButton_3.clicked.connect(delete)
    # MainWindow.show()
def LoginUI(): 
    global ui 
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(home)
    # ui.pushButton_2.clicked.connect(view)
    # ui.pushButton_3.clicked.connect(delete)
    # MainWindow.show()
def EnterUI():
    global ui 
    ui = enter.Ui_Form()
    ui.setupUi(MainWindow)
    # ui.pushButton.clicked.connect(home)
    # ui.pushButton_2.connect(home)
    # ui.pushButton_3.connect(home)
    # MainWindow.show()

# Thiết kế cơ sở dữ liệu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginUI()

    if login.exec_() == QDialog.Accepted:
        window = HomeUI()
        window.show()
    sys.exit(app.exec_())      

