# 문자열 돌리기
# 문자열 str이 주어집니다.
# 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

for a in input():
    print(a)



# 문자열 뒤집기
# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요
def solution(my_string):
    answer = my_string[::-1]
    return answer

# 배열 원소의 길이
# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

//배열 자르기
//정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
//numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요

def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

//최댓값 만들기
//정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    numbers.sort(reverse=True)
    answer = numbers[0] * numbers[1]
    return answer

//뒤에서 5등까지
//정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    num_list.sort()
    return num_list[0:5]

//문자열로 변환
//정수 n이 주어질 때, n을 문자열로 변환하여 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = str(n)
    return answer

//뒤에서 5등 위로
//정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    num_list.sort()
    answer = num_list
    return answer[5:]