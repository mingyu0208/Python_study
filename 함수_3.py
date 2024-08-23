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
# 재귀 함수로 구현한 피보나치 수열(2)
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
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))

# ==========================================

# 재귀 함수로 구현한 피보나치 수열(3)
# counter = 0

# def fibonacci(n):
#     counter+=1    # counter가 외부에 있는 것을 들고 오지 못함 그래서 global로 불러오는 것임.
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))

# 에러: UndoundLocalError

# ==========================================
# 메모화(재귀함수 사용시 많이 사용한다.): 딕셔너리를 사용해서 한 번 계산한 값을 저장합니다. 이를 메모한다고 표현합니다. 딕셔너리에 값이 메모되어 있으면 처리를 수행하지 않고 곧바로 메모된 값을 돌려주면서 코드의 속도를 빠르게 만드는 것입니다. 

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
# ==========================================


# extend()함수는 리스트연산 가능한 함수임.
# ex) a = [1,2,3] b = [4,5,6]를 a+=b 한 것과 같음 
# 결과:[1,2,3,4,5,6]

# ==========================================
# 재귀 함수 100명의 사람이 하나 이상의 테이블에 나눙 앉는 패턴의 경우의 수를 구하세요.

#  메모활용, 재귀처리 방법까지 다 배울 수 있었음.
# min_people = 2
# max_people = 10
# all_people = 100
# memo = {}

# def question(remain_people, sit_people):
#     key = str([remain_people, sit_people])

#     # 종료 조건
#     if key in memo:
#         return memo[key]
    
#     if remain_people < 0:
#         return 0
    
#     if remain_people == 0:
#         return 1
    
#     # 재귀 처리
#     cnt = 0
#     for i in range(sit_people, max_people + 1):
#         cnt += question(remain_people - i, i)

#     memo[key] = cnt

#     return cnt

# print(question(all_people, min_people))

# ==========================================

#  함수 고급
#  튜플: 리스트와 다르게 한번 결정된 요소를 바꿀 수 없다. 
#  람다: 매개변수로 함수를 전달사기 위해 함수 구문을 작성하는 것이 번거롭고, 코드 공간 낭비라는 생각이 ㄷ르 때 함수를 간단하고 쉽게 선언하는 방법. 

# 튜플은 괄호가 없이도 여러 값을 할당할 수 있어 유용할 듯 함. ex) tuple_list = 10, 20, 30, 40