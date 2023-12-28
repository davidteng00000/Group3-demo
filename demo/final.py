from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import requests
from bs4 import BeautifulSoup


#----------------------------爬蟲區---------------------------
urls = {
    'restaurant': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=0',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=10',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=20',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=30',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=40',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=50',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=60'],
    'transportation': ['https://in.ncu.edu.tw/alumni/web/benefits.php?type=transportation#'],
    'grocery': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=grocery&page=0',
                'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=grocery&page=10',
                'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=grocery&page=20'],
    'amusement': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=amusement&page=0',
                  'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=amusement&page=10'],
    'snack': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=snack&page=0',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=snack&page=10',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=snack&page=20'],
    'school': ['https://in.ncu.edu.tw/alumni/web/benefits.php?type=school#'],
    'hotel': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=0',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=10',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=20',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=30',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=40',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=50',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=60',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=70',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=80',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=90'],
    'medicine': ['https://in.ncu.edu.tw/alumni/web/benefits.php?type=aesthetic%20medicine#']
}
typelist = ['restaurant', 'transportation', 'grocery', 'amusement', 'snack', 'school', 'hotel', 'medicine']
benefitlist = []
for i in range(8):
    typeurl = urls[typelist[i]]
    length = len(typeurl)
    mlist = []
    for j in range(length):
        url = typeurl[j]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find_all(class_='row py-3')
        for element in elements:
            slist = []
            title = element.find('h4', class_='my-1')
            slist.append(title.get_text(strip = True))
            content = element.find_all('p', class_='my-0')
            index1 = ''
            index = 0
            for c in content:
                if index <= 4:
                    index1 += c.get_text(strip=True)
                    index1 += '\n'
                    if index==4:
                        slist.append(index1)                    
                if index==5:
                    slist.append(c.get_text(strip=True))
                if index==6:
                    i=str(c)
                    s=""
                    for j in range(52,1000):
                        if i[j]=="\"":
                            if i[j-1] == '/':
                                s+='?'
                            break
                        s+=i[j]
                    
                    slist.append(s)
                index+=1
            # print(slist)
            mlist.append(slist)
    benefitlist.append(mlist)
index_type=0
index_nth=0
#-----------------------UI區-----------------------------------

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
Form.setWindowTitle('Demo')
Form.resize(600, 812)

label1 = QtWidgets.QLabel(Form) #標題
label1.setFont(QtGui.QFont('times',5,QtGui.QFont.Bold))
label1.setGeometry(0,125,600,70)
label1.setText(benefitlist[0][0][0])
label1.setAlignment(QtCore.Qt.AlignCenter)

label1.setStyleSheet('''
    QLabel {
        font-size:30px;
        font-family:Microsoft JhengHei;
        color:#2F4F4F;
    }
''')

textedit1 = QtWidgets.QTextEdit(Form) #本文
textedit1.setGeometry(25,200,550,370)
textedit1.setReadOnly(True)
textedit1.setPlainText(benefitlist[0][0][1])


textedit1.setStyleSheet('''
    QTextEdit {
        font-size:15px;
        font-family:Microsoft JhengHei;
    }
''')

label3 = QtWidgets.QLabel(Form) #優惠期限
label3.setGeometry(25,565,600,70)
label3.setText(benefitlist[0][0][2])

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
link2.setText(f"<a href={benefitlist[0][0][3]}>網站連結</a>")

link2.setStyleSheet('''
    QLabel {
        font-size:15px;
        font-family:Microsoft JhengHei;
    }
''')
page = QtWidgets.QLabel(Form) #標題
page.setGeometry(0,740,600,70)
page.setText("1"+"/"+str(len(benefitlist[index_type])))
page.setAlignment(QtCore.Qt.AlignCenter)
page.setFont(QtGui.QFont('Times', 13,QtGui.QFont.Bold))



style_btn = '''
    QPushButton{
        background:#D0D0D0;
        border:1px solid #000;
        border-radius:10px;
       
    }
    QPushButton:pressed{
        background:#8E8E8E;
    }
'''

font = QtGui.QFont()
font.setPointSize(15)  # 設定字體大小
font.setFamily("Microsoft JhengHei")
font.setBold(True)    # 設定為粗體

pushButton_next = QtWidgets.QPushButton(Form)
pushButton_next.setGeometry(QtCore.QRect(472, 750, 113, 32))
pushButton_next.setObjectName("pushButton1")
pushButton_next.setText("下一則")
pushButton_next.setStyleSheet(style_btn)
pushButton_next.setFont(font)


pushButton_pre = QtWidgets.QPushButton(Form)
pushButton_pre.setGeometry(QtCore.QRect(15, 750, 113, 32))
pushButton_pre.setObjectName("pushButton2")
pushButton_pre.setText("上一則")
pushButton_pre.setStyleSheet(style_btn)
pushButton_pre.setFont(font)


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

def check_button():
    global index_nth,index_type,benefitlist
    if index_nth==0:
        pushButton_pre.setDisabled(True)
    else:
        pushButton_pre.setDisabled(False)

    if index_nth==(len(benefitlist[index_type])-1) :
        pushButton_next.setDisabled(True)
    else:
        pushButton_next.setDisabled(False)

def update(i,j):
    global benefitlist
    check_button()
    tmp = benefitlist[i][j][0]
    if(len(tmp) > 19):
        tmp = benefitlist[i][j][0][0:19] + "..."
    label1.setText(tmp)
    textedit1.setPlainText(benefitlist[i][j][1])
    label3.setText(benefitlist[i][j][2])
    link2.setText(f"<a href={benefitlist[i][j][3]}>網站連結</a>")

def change_type():
    global index_nth,index_type,benefitlist
    index_type=box.currentIndex()
    index_nth=0
    update(index_type,index_nth)
    page.setText(str(index_nth+1)+"/"+str(len(benefitlist[index_type])))

def next():
    global index_nth,index_type,benefitlist
    index_nth+=1
    update(index_type,index_nth)
    page.setText(str(index_nth+1)+"/"+str(len(benefitlist[index_type])))
    

def back():
    global index_nth,index_type,benefitlist
    index_nth-=1
    update(index_type,index_nth)
    page.setText(str(index_nth+1)+"/"+str(len(benefitlist[index_type])))


box.currentIndexChanged.connect(change_type)     
pushButton_next.clicked.connect(next)
pushButton_pre.clicked.connect(back)
pushButton_pre.setDisabled(True)

Form.show()
sys.exit(app.exec_())
