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

//짝수는 싫어요
//정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = [ i for i in range(1, n+1) if i % 2 != 0]
    return answer

//제곱수  판별하기
//어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    if (n**0.5).is_integer():
        return 1
    else:
        return 2

//중앙값 구하기
//중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다.
//예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    array.sort()
    center_idx = len(array)//2
    return array[center_idx]

//배열 두배
//정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer
//옷가게 할인받기
//머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
//구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)

//문자열을 정수로 변환하기
//숫자로만 이루어진 문자열 n_str이 주어질 때, n_str을 정수로 변환하여 return하도록 solution 함수를 완성해주세요.
def solution(n_str):
    answer = int(n_str)
    return answer

//정수부분
//실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.
def solution(flo):
    answer = int(flo)
    return answer

//rny_string
//'m'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다.
//문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(rny_string):
    answer = rny_string.replace('m', 'rn')
    return answer

//A강조하기
//문자열 myString이 주어집니다.
//myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.
def solution(myString):
    answer = myString.lower()
    answer = answer.replace('a', 'A')
    return answer

//대문자와 소문자
//문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = my_string.swapcase()
    return answer

//가장 큰 수 찾기
//정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    return [max(array), array.index(max(array))]