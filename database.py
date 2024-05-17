import sys,sqlite3,time
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, \
QPushButton,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit, QHBoxLayout
from PyQt5.QtCore import QCoreApplication

class DBHelper():
    def __init__(self): 
        self.conn = sqlite3.connect('studentdb.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER,name TEXT,grade INTEGER,falcuty INTEGER,course_a INTEGER,course_b INTEGER,course_c INTEGER,course_d INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS falcuty(fal_id INTEGER,fal_name TEXT,course INTEGER,class INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS course(course_id INTEGER,course INTEGER,fal_name TEXT,credit INTEGER,type INTEGER,slot INTEGER,No_enrolled INTEGER)")

    def addStudent(self,sid,sname,sgrade,sfal,scora,scorb,scorc,scord):
        try: 
            self.cursor.execute('INSERT INTO student(id,name,grade,falcuty,course_a,course_b,course_c,course_d) VALUES (?,?,?,?,?,?,?,?)',(sid,sname,sgrade,sfal,scora,scorb,scorc,scord))
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            QMessageBox.information('Done!','You have done successfully to add new student into HUS Database.')
        except Exception: 
            QMessageBox.warning('Error!','You can not add any students right now')
    def searchStudent(self,sid): 
        self.cursor.execute('SELECT * FROM student WHERE id ='+str(sid))
        self.data = self.cursor.fetchone
        if not self.data: 
            QMessageBox.warning('Failed',str(sid) + 'does not exist') 
            return None
        else: 
            self.lst = []
            self.lst.append(self.data[i] for i in range(0,8))
            self.cursor.close()
            self.conn.close()
            showStudent(self.lst)
    def showStudent(self,list):
        sid = ""
        sname = ''
        sgrade = ''
        sfalcuty = ''
        scora = ''
        scorb = ''
        scorc = ''
        scord = ''
        sid=list[0]
        sname=list[1]

        if list[2]==0:
            sgrade="Fresher Student"
        elif list[2]==1:
            sgrade="Second-year Student"
        elif list[2]==2:
            sgrade="Junior Student"
        elif list[2]==3:
            sgrade="Major Student"

        if list[3]==0:
            sfalcuty="MIM"
        elif list[3]==1:
            sfalcuty="Chemistry"
        elif list[3]==2:
            sfalcuty="Biology"
        elif list[3]==3:
            sfalcuty="Geography"
        elif list[3]==4:
            sfalcuty="Physics"

        if list[4]==0:
            scora="Design and analysis algorithm"
        elif list[4]==1:
            scora="Optimization"
        elif list[4]==2:
            scora="Calculus"
        elif list[4]==3:
            scora="Python programing"
        elif list[4]==4:
            scora="Database"
        elif list[4]==5:
            scora="Computer security"
        elif list[4]==6:
            scora="Computer Science"
        elif list[4]==7:
            scora="Natural language processing"

        if list[5]==0:
            scorb="Design and analysis algorithm"
        elif list[5]==1:
            scorb="Optimization"
        elif list[5]==2:
            scorb="Calculus"
        elif list[5]==3:
            scorb="Python programing"
        elif list[5]==4:
            scorb="Database"
        elif list[5]==5:
            scorb="Computer security"
        elif list[5]==6:
            scorb="Computer Science"
        elif list[5]==7:
            scorb="Natural language processing"

        if list[6]==0:
            scorc="Design and analysis algorithm"
        elif list[6]==1:
            scorc="Optimization"
        elif list[6]==2:
            scorc="Calculus"
        elif list[6]==3:
            scorc="Python programing"
        elif list[6]==4:
            scorc="Database"
        elif list[6]==5:
            scorc="Computer security"
        elif list[6]==6:
            scorc="Computer Science"
        elif list[6]==7:
            scorc="Natural language processing"

        if list[7]==0:
            scord="Design and analysis algorithm"
        elif list[7]==1:
            scord="Optimization"
        elif list[7]==2:
            scord="Calculus"
        elif list[7]==3:
            scord="Python programing"
        elif list[7]==4:
            scord="Database"
        elif list[7]==5:
            scord="Computer security"
        elif list[7]==6:
            scord="Computer Science"
        elif list[7]==7:
            scord="Natural language processing"


        table=QTableWidget()
        tableItem=QTableWidgetItem()
        table.setWindowTitle("Student Details")
        table.setRowCount(7)
        table.setColumnCount(2)

        table.setItem(0, 0, QTableWidgetItem("Roll"))
        table.setItem(0, 1, QTableWidgetItem(str(sid)))
        table.setItem(1, 0, QTableWidgetItem("Name"))
        table.setItem(1, 1, QTableWidgetItem(str(sname)))
        table.setItem(2, 0, QTableWidgetItem("Year"))
        table.setItem(2, 1, QTableWidgetItem(str(sgrade)))
        table.setItem(3, 0, QTableWidgetItem("Falcuty"))
        table.setItem(3, 1, QTableWidgetItem(str(sfalcuty)))
        table.setItem(4, 0, QTableWidgetItem("Slot A"))
        table.setItem(4, 1, QTableWidgetItem(str(scora)))
        table.setItem(5, 0, QTableWidgetItem("Slot B"))
        table.setItem(5, 1, QTableWidgetItem(str(scorb)))
        table.setItem(6, 0, QTableWidgetItem("Slot C"))
        table.setItem(6, 1, QTableWidgetItem(str(scorc)))
        table.setItem(6, 0, QTableWidgetItem("Slot D"))
        table.setItem(6, 1, QTableWidgetItem(str(scord)))
        table.horizontalHeader().setStretchLastSection(True)
        table.show()
        dialog=QDialog()
        dialog.setWindowTitle("Student Details")
        dialog.resize(500,300)
        dialog.setLayout(QVBoxLayout())
        dialog.layout().addWidget(table)
        dialog.exec()
    def deleteRecord(self,sid): 
        try:
            self.cursor.execute('DELETE from student where id ='+str(sid))
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            QMessageBox.information('Done!', 'You deleted successfully')
        except Exception: 
            QMessageBox.warning('Error','sid did not exist')


            