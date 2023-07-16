# reversed()
from typing import List

list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("# reversed()함수")
print("reversed([1, 2, 3, 4, 5]):", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
print()

# 반복문 적용
print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)

temp = reversed([1, 2, 3, 4, 5, 6])

for i in temp:
    print("첫 번째 반복문: {}".format(i))

for i in temp:
    print("두 번째 반복문:{}".format(i))

# enumerate() - 방법1
example_list = ["요소A", "요소B", "요소C"]
i = 0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i, item))
    i += 1

# enumerate() - 방법2
example_list = ["요소A", "요소B", "요소C"]
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))

# enumerate()함수와 리스트
example_list = ["요소A", "요소B", "요소C"]

print("#단순 출력")
print(example_list)
print()

# enumerate()함수 적용 출력
print("#enumerate()함수 적용 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환 출력
print("#list()함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumerate() 함수 조합해서 사용
print("#반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))

# 딕셔너리의 items() 함수와 반복문
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

print("#딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

print("#딕셔너리의 items()함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

# 리스트 내포
array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)

# 리스트 안에 for문 사용하기
array = [i * i for i in range(0, 20, 2)]
print(array)

# 조건을 활용하여 리스트 내포
array = ["사과", " 자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)

output = [fruit for fruit in array if fruit != "초콜릿"]
