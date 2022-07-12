# 로또복권은 추첨 순서를 따지지 않는다.
# 추첨 순서와 관계없이 추첨된 숫자만 일치하면 당첨이다.
# 파이썬에서는 배열이 같은지 다른지 비교할 때 내부 요소로만
# 비교하지 않고, 내부 요소의 순서까지 고려한다.
# [1, 2] == [2, 1] => False
# [1, 2] == [1, 2] => True
# 위의 조건식을 이용해서 로또복권을 몇 번 사야 1등 당첨이 되는지
# 시뮬레이션 해주는 코드를 작성해라.
import random

luckynumber = []
getnumber = []
count = 0
while(len(luckynumber) != 6): # 첨부터 6으로 하면 오래걸리니 3부터 하나씩 늘리기
    number = random.randint(1, 45)
    if number not in luckynumber:
        luckynumber.append(number)
luckynumber.sort()

while luckynumber != getnumber:
    getnumber=[]
    count +=1
    while(len(getnumber) != 6): # 첨부터 6으로 하면 오래걸리니 3부터 하나씩 늘리기
        number = random.randint(1, 45)
        if number not in getnumber:
            getnumber.append(number)
    getnumber.sort()
print("로또복권을 %d장 사서 당첨되었습니다." % count)
print("로또복권을 %d원어치 사서 당첨되었습니다." % (count * 1000))
print("당첨번호: ", luckynumber, getnumber)