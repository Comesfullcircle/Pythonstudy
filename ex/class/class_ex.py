#instance()함수 활용
#학생 클래스 선언
class Student:
    def study(self):
        print("공부를 합시다.")

#선생님 클래스 선언
class  Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

#교실 내부의 객체 리스트를 생성함
classroom = [Student(), Student(), Teacher(), Student(), Student()]

#반복을 적용해서 적절한 함수 호출
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()


#__str__()함수
#클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

#학생 리스트를 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

#출력
print("이름", "총점", "평균", sep ="\t")
for student in students:
    print(str(student))

#크기 비교 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science =science

    def get_sum(self):
        return  self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

#학생 리스트를 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

#학생 선언
student_a = Student("윤인성", 87, 98, 88, 95),
student_b = Student("연하진", 92, 98, 96, 98),

#출력
print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)

#클래스 변수
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        #인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english =english
        self.science = science

        #클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

#학생 리스트를 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

#출력
print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))

#클래스 함수
class Student:
    count = 0
    students = []

    #클래스 함수
    @classmethod
    def print(cls):
        print("-----학생 목록 -----")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("----- ------ ------")

    #인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_averge(self):
        return self.get_sum() / 4

    def __str__(self):
        return  "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_averge())

#학생 리스트 선언
Student("윤인성", 87, 98, 88, 95),
Student("연하진", 92, 98, 96, 98),
Student("구지연", 76, 96, 94, 90),
Student("나선주", 98, 92, 96, 92),
Student("윤아린", 95, 98, 98, 98),
Student("윤명월", 64, 88, 92, 92),
Student("김미화", 82, 86, 98, 88),
Student("김연화", 88, 74, 78, 92),
Student("박아현", 97, 92, 88, 95),
Student("서준서", 45, 52, 72, 78)

#현재 생성된 학생 모두 출력
Student.print()

#가비지 컬렉터 : 변수에 저장 하지 않는 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))

Test("A")
Test("B")
Test("C")

#가비지 컬렉터:변수에 저장한 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))

a = Test("A")
b = Test("B")
c = Test("C")


#원의 둘레와 넓이를 구하는 객체 지향 프로그램
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius ** 2)

#원의 둘레와 넓이
circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

#프라이빗 변수
import math

class Circle:
    def __init__(self, radius):
        self.__radius = None
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

#원의 둘레와 넓이
circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

#__radius에 접근 < 오류나게 됨>
#print(circle.__radius)

#게터와 세터
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    #게터와 세터 선언
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

#원의 둘레와 넓이
circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

#간접적으로__radius에 접근
print(circle.get_radius())

#원의 둘레와 넓이 구함
circle.set_radius(2)
print("#반지름을 변경하고 원의 둘레와 넓이를 구함")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

#상속의 활용
#부모 클래스 선언
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Praent 클래스의 test() 메소드 입니다.")

#자식 클래스를 선언
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child 클래스의 __init()__메소드가 호출되었습니다.")

#자식 클래스의 인스턴스를 생성하고 부모의 메소드를 호출
child = Child()
child.test()
print(child.value)

#사용자 정의 예외 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        super().__init__()

raise CustomException

#자식 클래스로써 부모의 함수 재정의(오버라이드)하기
class CustomException(Exception):
    def __init__(self):
        super().__init__()
        print("#오류 발생")
    def __str__(self):
        return "#오류발생"

raise CustomException

#자식 클래스로써 부모에 없는 새로운 함수 정의하기
#사용자 정의 예외 생성
class CustomException(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("##오류 정보")
        print("메시지:", self.message)
        print("값:", self.value)

#예외 발생
try:
    raise CustomException("딱히 이유x", 273)
except CustomException as e:
    e.print()
