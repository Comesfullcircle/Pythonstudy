#test_module.py
PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_cirumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius
