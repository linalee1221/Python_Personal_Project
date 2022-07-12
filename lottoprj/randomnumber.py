# 난수발생
# 난수란 무작위로 선택된 값을 말한다.
# 파이썬에서는 import random 이라고 최상단에 적으면
# 난수를 발생시킬 수 있다.
import random

# 정수 난수 : random, randint(시작값, 끝값)
# ex) random.randint(1, 100) 이라고 입력시 1~100 범위의 숫자
# 하나를 무작위로 생성한다.
print(random.randint(1, 100))

# 실수 난수 : random.random()
# ex) random.random() 입력시 0이상 1미만 실수 생성
print(random.random())

# 1~100 범위의 실수를 출력하는 코드를 아래에 작성해라.
print(random.random()*100)
print(random.random() + random.randint(0,99))