from PyQt5 import QtGui, QtWidgets, QtCore
import sys



app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
Form.setWindowTitle('Demo')
Form.resize(600, 812)

label1 = QtWidgets.QLabel(Form) #標題
label1.setGeometry(0,125,600,70)
label1.setText("foodpanda校友貴賓獨享優惠")
label1.setAlignment(QtCore.Qt.AlignCenter)

label1.setStyleSheet('''
    QLabel {
        font-size:40px;
        font-family:Microsoft JhengHei;
        color:#2F4F4F;
    }
''')

textedit1 = QtWidgets.QTextEdit(Form) #本文
textedit1.setGeometry(25,200,550,370)
textedit1.setReadOnly(True)
textedit1.setPlainText("地區\n聯絡電話\n地址\n優惠內容:\n適用對象 全體同仁\n一、加入步驟：\n［同仁升級企業帳號］\n員工自行填表申請加入，表單 https://forms.gle/am3rtbBYFu8ECT9G9\nstep2.信箱點開<立即啟用您的企業帳號> *填寫完成後1工作天收到開通信件\n\n\n\n\n\n\n\n\n\n\n\nhaha")

textedit1.setStyleSheet('''
    QTextEdit {
        font-size:15px;
        font-family:Microsoft JhengHei;
    }
''')

label3 = QtWidgets.QLabel(Form) #優惠期限
label3.setGeometry(25,565,600,70)
label3.setText("優惠期限")

label3.setStyleSheet('''
    QLabel {
        font-size:15px;
        font-family:Microsoft JhengHei;
        color:#DAA520;
    }
''')

link2=QtWidgets.QLabel(Form) #網站連結
link2.setOpenExternalLinks(True)
link2.setGeometry(25, 600, 600, 70)
link2.setText('<a href="https://www.google.com">網站連結</a>')

link2.setStyleSheet('''
    QLabel {
        font-size:15px;
        font-family:Microsoft JhengHei;
    }
''')

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
