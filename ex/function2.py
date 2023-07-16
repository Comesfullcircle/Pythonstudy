#구문 내부에 여러 줄 문자열을 사용했을 때의 문제점
#if 조건문과 여러 줄 문자열(1)
#number = int(input("정수 입력>"))

number = 13 # 예시

if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(number, number))

#if 조건문과 여러 줄 문자열(2)
#number = int(input("정수 입력>"))
number = 13 # 예시

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))

#if 조건문 과 긴 문자열
#number = int(input("정수 입력>"))
number = 13 # 예시

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.""".format(number, number))
