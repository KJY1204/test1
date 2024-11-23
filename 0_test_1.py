import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) # GUI 앱(창) 객체 생성

win = QWidget() # 위젯 객체 생성
win.setWindowTitle("나의 첫 창") # 창 제목
win.setGeometry(100, 100, 300, 120) # x여백, y여백, 가로 길이, 세로 길이
win.move(60, 20) # 창의 위치 조정(x=60, y=20)

hellomsg = QLabel("<h1>Hello World!</h1>", parent=win) # 이 라벨을 win의 자식으로 설정 하겠음.
hellomsg.move(60, 20) # 글자 위치 조정(x=60, y=20)

win.show() # 창 띄우기

sys.exit(app.exec_()) # app 이벤트 루프 시작 -> 시스템 종료
