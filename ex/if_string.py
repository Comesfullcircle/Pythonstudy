number = int(input("점수 입력>"))

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))

#if 조건문과 긴 문자열
number = int(input("점수 입력>"))

if number % 2 == 0:
    print("입력한 문자열은 {}입니다. \n{}는(은) 짝수입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다. \n{}는(은) 홀수입니다.".format(number, number))

#괄호로 문자열 연결하기
test = (
    "이렇게 입력해도"
    "하나의 문자열로 연결되어"
    "생성됩니다."
)

print("test:", test)
print("type(test):", type(test))

#여러 줄 문자열과 if구문을 조합했을 때의 문제 해결(1)
number = int(input("정수 입력>"))

if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다."
    ).format(number, number))

#여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결
number = int(input("정수 입력 > "))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number, number))

#이터레이터
#변수를 선언
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print("reversed_numbers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
