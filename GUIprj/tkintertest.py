# gui 프로그래밍을 위한 tkinter 임포트
from tkinter import *

# 창 만들고 유지하기
root = Tk()
# 창 크기 설정
root.configure(width="75m", height="100m")
################ 함수 부품 배치 부분 ################
# 문제1.
# test라는 이름의 함수를 만들어주세요.
# 이 함수는 실행시 콘솔창에
# "Hello Python"이라는 문장을 출력합니다.
# 함수를 만들고 "테스트버튼" 버튼에 연결해서 클릭할 때마다
# 콘솔창에 "Hello Python"이 출력되게 해보세요.
def test():
    print("Hello Python")
def test2():
    value = E1.get()
    print(value)
def exchange():
    value = int(E1.get())
    result = value / 38.61
    print("원화" + str(value) + "원: " + str(result) + "NTD 입니다.")
def onselect(evt):
    w = evt.widget
    index = w.curselection()
    value = w.get(index)
    print(index, value)

    
################ 창 부품 배치 부분 ################
Button(root, text="테스트버튼", command=test).place(x=10, y=10, width=100, height=30)
Button(root, text="Entry테스트", command=test2).place(x=150, y=10, width=100, height=30)
Button(root, text="환율", command=exchange).place(x=10, y=60, width=100, height=30)

E1 = Entry(root)
E1.place(x=10, y=130, width=100, height=30)

L1 = Listbox(root)
L1.place(x=130, y=130, width=100, height=150)
L1.insert(0, "닭가슴살")
L1.insert(1, "요거트")
L1.insert(2, "다이어트")
# Listbox의 이벤트 세팅
L1.bind('<<ListboxSelect>>', onselect)

Lb1 = Label(root, text="메뉴판")
Lb1.place(x=130, y=110, width=100, height=20)

Sb1 = Spinbox(root, from_=1, to=5)
Sb1.place(x=10, y=170, width=100, height=30)

option1=["파이썬", "자바", "C++"]#옵션에 넣을 것들
variable = StringVar(root)
variable.set(option1[0]) #메뉴창에 초기에 설정된 값은 "파이썬"
op1=OptionMenu(root, variable, *option1)
op1.place(x=10,y=210,width=100,height=35)





# 문제2.
# 버튼을 하나 더 만든다. 버튼의 text는 "Entry테스트"로 한다.
# 다음 이 버튼에 함수를 연결한다.
# 함수의 이름은 원하는대로 적어주면 되며 Entry에 있는 값을 .get()으로 얻어와서
# print()구문으로 출력해준다.

# 문제3.
# 버튼을 하나 더 만든다. 버튼의 text는 "환율"로 한다.
# 다음 이 버튼에 함수를 연결한다.
# 함수의 이름은 원하는대로 적어주면 되며 Entry에 있는 값을 .get()으로 얻어와서
# Entry에 있는 원화를 숫자로 집어넣는다.
# ex)백만원-> 1000000 입력
# 대만환율 38.61에 따라 원화x원을 입력했을때 대만환율에 따라 몇 NTD인지 출력하기






# gui 프로그래밍의 마지막 지점에 항상 작성되어 있어야 한다.
root.mainloop()
