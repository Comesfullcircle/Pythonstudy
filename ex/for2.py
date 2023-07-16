#중첩 반복문으로 피라미드 만들기 
#1
output = ""

for i in range(1,10):
    for j in range(0,i):
        output += "*"
    output += "\n"

print(output)

#1번과 동일
output = ""

for i in range(1, 10):
    output += ("*"*i)
    output += "\n"

print(output)


#2
output = ""

for i in range(1, 15):
    for j in range(14, i, -1):
        output += ' '
    for k in range(0, 2 * i -1):
        output += '*'
    output += '\n'

print(output)
