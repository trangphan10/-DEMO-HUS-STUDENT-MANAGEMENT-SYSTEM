from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout,QPushButton,QWidget, QMainWindow
app = QApplication([])
# QMainWindow và QWidget là khối chứa tất cả đối tượng
# Với QMainWindow không dùng layout, mình khai báo trực tiếp trong QLabel(parent = window,text='') tuy nhiên dễ bị overlap giao diện và cần điều chỉnh thêm với .move(toạ độ)

window = QWidget()
layout = QVBoxLayout() 
# tạo layout theo chiều dọc
label = QLabel('Hello World')
layout.addWidget(label)

button = QPushButton('Click')
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec()