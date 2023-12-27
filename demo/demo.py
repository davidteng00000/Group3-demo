from PyQt5 import QtGui, QtWidgets, QtCore
import sys



app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
Form.setWindowTitle('Demo')
Form.resize(600, 812)

link=QtWidgets.QLabel(Form)
link.setOpenExternalLinks(True)
link.setGeometry(20, 20, 200, 150)
link.setText('<a href="https://www.google.com">Visit Example.com</a>')

pushButton_next = QtWidgets.QPushButton(Form)
pushButton_next.setGeometry(QtCore.QRect(472, 750, 113, 32))
pushButton_next.setObjectName("pushButton1")
pushButton_next.setText("下一則優惠")

pushButton_pre = QtWidgets.QPushButton(Form)
pushButton_pre.setGeometry(QtCore.QRect(15, 750, 113, 32))
pushButton_pre.setObjectName("pushButton2")
pushButton_pre.setText("上一則優惠")


box = QtWidgets.QComboBox(Form)   # 加入下拉選單
box.addItems(['餐廳','交通','用品','休閒','甜品','校內優惠','飯店','醫療'])   # 加入四個選項 # box.currentIndex()去讀list
box.setGeometry(375,15,200,30)
box.setItemIcon(0,QtGui.QIcon('pic/restaurant.jpg'))
box.setItemIcon(1,QtGui.QIcon('pic/transportation.jpg'))
box.setItemIcon(2,QtGui.QIcon('pic/grocery.jpg'))
box.setItemIcon(3,QtGui.QIcon('pic/amusement.jpg'))
box.setItemIcon(4,QtGui.QIcon('pic/snack.jpg'))
box.setItemIcon(5,QtGui.QIcon('pic/school.jpg'))
box.setItemIcon(6,QtGui.QIcon('pic/hotel.jpg'))
box.setItemIcon(7,QtGui.QIcon('pic/aesthetic.png'))
Form.show()
sys.exit(app.exec_())