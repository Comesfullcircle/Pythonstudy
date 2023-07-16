array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))

# 역 반복문
for i in range(4, 0 -1, -1):
    print("현재 반복 변수:{}".format(i))

#역 반복문2
for i in reversed(range(5)):
    print("현재 반복 변수:{}".format(i))
