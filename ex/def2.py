#반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

#재귀 함수를 사용해 팩토리얼 구하기
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

#재귀 함수로 구현한 피보나치 수열(1)
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))

#재귀 함수로 구현한 피보나치 수열(2)
counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter #UnboundLocalError에 대한 처리
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)
print("---")
print("fibonacci(10)계산에 활용된 덧셈 횟수는 {}번입니다.". format(counter))

#메모화
dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))

#리스트 평탄화하기(1)
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += item
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))

#리스트 평탄화하기(2) : 1 오류 해결
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item) #flatten()함수를 재귀적으로 호출
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))

#기억 해야 할 것
# 1. 함수의 변수는 함수 호출마다 따로따로 만들어짐
# 2. 함수가 끝나면(리턴되면) 함수를 호출했던 위치로 돌아옴
