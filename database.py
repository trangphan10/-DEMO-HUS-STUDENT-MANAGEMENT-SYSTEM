import sys,sqlite3,time
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, \
QPushButton,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit, QHBoxLayout
from PyQt5.QtCore import QCoreApplication

class DBHelper():
    def __init__(self): 
        self.conn = sqlite3.connect('studentdb.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS student(id VARCHAR(8),name VARCHAR(255),grade VARCHAR(255),falcuty VACHAR(255),course_a VARCHAR(255),course_b VARCHAR(255),course_c VARCHAR(255),course_c VARCHAR(255))")
        