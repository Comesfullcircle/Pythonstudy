#random 모듈
import random
print("# random 모듈")

#random() : 0.0 <= x < 1.0 사이의 float를 리턴함
print("- random():", random.random())

#uniform(min, max) : 지정한 범위 사이의 float를 리턴함
print("- uniform(10, 20):", random.uniform(10,20))

#randomrange(): 지정한 범위의 int를 리턴함
# - randomrange(max): 0부터 max 사이의 값을 리턴함
# - randomrange(min, max): min부터 max 사이의 값을 리턴함
print("- randomrange(10):", random.randrange(10))

#choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택함
print("- choice([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

#shuffle(list): 리스트의 요소들을 랜덤하게 섞음
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

#sample(list, k=<숫자>): 리스트이 요소 중에서 k 개를 뽑음
print("- sample([1, 2, 3,  4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k = 2))

#sys 모듈
import sys

print(sys.argv)
print("---")
print("getwindowsversion:()", sys.getwindowsversion())
print("copyright:", sys.copyright)
print("version:", sys.version)

sys.exit()

#os 모듈
import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

os.mkdir("hello")
os.rmdir("hello")

#파일을 생성하고 파일이름을 변경
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

os.remove("nex.txt")

#시스템 명령어 실행
os.system("dir")

#datetime 모듈
import datetime

print("#현재 시각 출력")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

#시간 출력방법
print("#시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
                                            now.month,\
                                            now.day,\
                                            now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()

#시간 처리하기
import datetime
now = datetime.datetime.now()

print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y[] %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

#특정 시간 요소 교체하기
print("#now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

#time모듈
import time

print("지금부터 5초 동안 정지합니다ㅣ!")
time.sleep(5)
print("exit")

#urllib 모듈
from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output)
