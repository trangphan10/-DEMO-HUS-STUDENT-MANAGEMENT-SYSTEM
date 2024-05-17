from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, \
QPushButton,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit, QHBoxLayout
from PyQt5.QtCore import QCoreApplication
import sys,sqlite3
import home,login,enter
from database import DBHelper
# Xây dựng giao diện
def HomeUI(): 
    global ui 
    ui = home.Ui_Form()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda: EnterUI(Widget))
    ui.pushButton_2.clicked.connect(lambda: showStudent(QMainWindow))
    ui.pushButton_3.clicked.connect(lambda: deleteStudent(QMainWindow))
    MainWindow.show()
    # ui.pushButton.clicked.connect(lambda: EnterUI(MainWindow))
    # ui.pushButton_2.clicked.connect(view)
    # ui.pushButton_3.clicked.connect(delete)
    # MainWindow.show()
class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.ui = login.Ui_Signin()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handleLogin)
    def handleLogin(self):
        if (self.ui.lineEdit.text() == 'chan' and
            self.ui.lineEdit_2.text() == '1010'):
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Bad user or password')
def LoginUI(): 
    login = LoginDialog()
    return login
    # global ui 
    # ui = login.Ui_Signin()
    # ui.setupUi(QDialog)
    # ui.pushButton.clicked.connect(QDialog.accept) 
    # ui.pushButton_2.clicked.connect(view)
    # ui.pushButton_3.clicked.connect(delete)
    # MainWindow.show()
def EnterUI(Widget):
    global ui 
    ui = enter.Ui_Form(Widget)
    ui.__init__(Widget)
    Widget.show()

class showStudent(): 
    def __init__(self, Form):
        self.rollToBeSearched = 0
        self.vbox = QVBoxLayout()
        self.text = QLabel("Enter the roll no of the student")
        self.editField = QLineEdit()
        self.btnSearch = QPushButton("Search", self)
        self.btnSearch.clicked.connect(self.show)
        self.vbox.addWidget(self.text)
        self.vbox.addWidget(self.editField)
        self.vbox.addWidget(self.btnSearch)
        self.setLayout(self.vbox)
        self.setWindowTitle("Enter Roll No")
        self.show()
    def show(self): 
        self.db = DBHelper()
        self.lst = DBHelper.searchStudent(self.editField.text())
        return DBHelper.showStudent(self.lst)

class deleteStudent(): 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rollForDelete = 0
        self.vboxDelete = QVBoxLayout()
        self.textDelete = QLabel("Enter the roll no of the student")
        self.editFieldDelete = QLineEdit()
        self.btnSearchDelete = QPushButton("Delete", self)
        self.btnSearchDelete.clicked.connect(self.delete)                       
        self.vboxDelete.addWidget(self.textDelete)
        self.vboxDelete.addWidget(self.editFieldDelete)
        self.vboxDelete.addWidget(self.btnSearchDelete)
        self.setLayout(self.vboxDelete)
        self.setWindowTitle("Delete Record")
        self.show()
    def delete(self): 
        self.db = DBHelper()
        return self.db.deleteRecord(self.editFieldDelete.text)


# Thiết kế cơ sở dữ liệu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QDialog()
    Widget = QtWidgets.QWidget()
    login = LoginUI()

    if login.exec_() == QDialog.Accepted:
        window = HomeUI()
    sys.exit(app.exec_())      

