# GUI 형태로 로또번호 추첨 프로그램 만들기
#
# "추첨"이라고 써진 버튼을 클릭했을 때 번호 6개를 출력하기.
# "초기화"라고 써진 버튼을 클릭했을 때 출력된 번호가 삭제되도록 하기.
# "추첨을 연달아 누르면 누를 때마다 다시 번호를 추첨합니다."
# "제작자"라고 써진 버튼을 누르면 본인의 이름이 레이블로 출력되도록 기능 추가하기

from tkinter import *
import random

#### 창 설정부
root = Tk()
root.configure(width="70m", height="90m")

#### 함수 부
def get_number():
    global Lb1
    getnumber = []
    while(len(getnumber) !=6):
        number = random.randint(1, 45)
        if number not in getnumber:
            getnumber.append(number)
    getnumber.sort()
    Lb1 = Label(root, text=getnumber)
    Lb1.place(x=58, y=100, width=150, height=60)
    
def initialize():
    global Lb1
    Lb1.destroy()
    Lb1 = Label(root, text="")
    Lb1.place(x=50, y=110, width=150, height=60)

def maker():
    Lb2 = Label(root, text="제작자 : ★☆이은송☆★")
    Lb2.place(x=55, y=250, width=150, height=60)
    
#### 창 부품부


Lb1 = Label(root, text="★로또번호 추첨 프로그램★")
Lb1.place(x=33, y=25, width=200, height=20)

Button(root, text="추첨", command=get_number).place(x=10, y=60, width=110, height=30)
Button(root, text="초기화", command=initialize).place(x=145, y=60, width=110, height=30)
Button(root, text="제작자", command=maker).place(x=82, y=200, width=100, height=30)

Lb1 = Label(root)



root.mainloop()