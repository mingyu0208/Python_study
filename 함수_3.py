# (2024. 08. 19)

# def 함수이름(매개변수, 매개변수, ..., *가변 매개변수):
#     문장
# ==========================================

# 가변 매개변수
# def print_n_times(n, *values):   # 변수를 원하는 만큼 받을 수 있는 가변 매개변수 함수: 매개변수 개수가 변할 수 있다는 의미입니당.
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
# ==========================================

# 기본 매개변수=값
# def print_n_times(value, n = 2):
#     for i in range(n):
#         print(value)
# print_n_times("안녕하세요")

# 결론: 기본 매개변수는  가변 매개변수 앞에 써도 의미가 없다.

# ==========================================
# def print_n_times(*value, n = 2):  
#     for i in range(n):
#         print(value)
# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", 3)

# 결과:
# ('안녕하세요', '즐거운', '파이썬 프로그래밍', 3)
# ('안녕하세요', '즐거운', '파이썬 프로그래밍', 3)

 # 결론: 가변 매개변수가 우선된다.
# ==========================================

# 이런식으로 가능함.

# def test(a, b = 10, c = 100):
#     print(a+b+c)

# test(10, 20, 30)

# test(a = 10, b = 100, c = 200)

# test(c=10,a=100,b=200)

# test(10,c=200)
# ==========================================

# 팩토리얼 함수
# n! = n * (n - 1) * (n - 2) * ... * 1
# def factorial(n):
#     output = 1

#     for i in range(1,n+1):
#         output *=i
#     return output

# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))

# ==========================================

# 재귀함수로 팩토리얼 구하기
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))
# ==========================================

# 재귀 함수로 구현한 피보나치 수열(1)
# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print("1!:", fibonacci(1))
# print("2!:", fibonacci(2))
# print("3!:", fibonacci(3))
# print("4!:", fibonacci(4))
# print("5!:", fibonacci(5))

# ==========================================
# counter = 0
# def fibonacci(n):
#     global counter    #global 외부 참조
#     counter += 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))

# dictionary = {
#     1:1,
#     2:1
# }

# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     else:
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output

# print("10!:", fibonacci(10))
# print("20!:", fibonacci(20))
# print("30!:", fibonacci(30))
# print("40!:", fibonacci(40))
# print("50!:", fibonacci(50))