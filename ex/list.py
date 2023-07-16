array = [273, 32, 103, "문자열", True, False]
print(array)

list_a = [273, 32, 103, "문자열",  True, False]
list_a[0]
list_a[1]
list_a[2]
list_a[1:3]
list_a[0] = "변경"
list_a[-1]
list_a[-2]
list_a[-3]
list_a[3]
list_a[3][0]

list_b = [[1,2,3], [4,5,6], [7,8,9]]
list_b[1]
list_b[1][1]

#리스트를 선언함
list_c = [1,2,3]

#리스트 뒤에 요소 추가하기
list_c.append(4)
list_c.append(5)
print(list_c)
print()

#리스트 중간에 요소 추가하기
list_c.insert(0, 10)
print(list_c)
