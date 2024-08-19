# 2024.08.13
#  04-1  리스트와 반복문

# 리스트 끼리 더하기
# list_a = [1,2,3]
# list_b = [4,5,6]
# print(list_a+ list_b) # [1, 2, 3, 4, 5, 6] 리스트 끼리 연산자 사용 가능

#  append(요소), insert(위치, 요소)
#  extend() 함수
# list_a = [1,2,3]
# list_b = [4,5,6]
# list_a.extend(list_b) # 파괴적
# != list_a + list_b 비파괴적
# print(list_a)

# list_a = [1,2,3,4,5,6,7,8,9]
# list_a.pop(3)
# print(list_a)

# print(list_a)
# del list_a[4:]
# print(list_a)

# 리스트[시작_인덱스 : 끝 : 단계] 리스트 슬라이싱

# 값으로 제거하기: remove()  === 리스트.remove(값)
# 모두 제거하기 clear() === 리스트.clear()

# 정렬 
# 리스트.sort() 오름차순
# 리스트.sort(reverse=True)

# 중첩반복문
# list_of_list = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9]
# ]
# for items in list_of_list:
#     for item in items:
#         print(items)

# 전개 연산자  * 기호를 붙이면 리스트를 전개한 것 과 같이 된다.
# a = [1,2,3,4]
# b = [*a, *a] # 비파괴적
# print(b)

# 결과 1
# 273 는 홀수 입니다.
# 103 는 홀수 입니다.
# 5 는 홀수 입니다.
# 32 는 짝수입니다.
# 32 는 홀수 입니다.
# 65 는 홀수 입니다.
# 9 는 홀수 입니다.
# 72 는 짝수입니다.
# 72 는 홀수 입니다.
# 800 는 짝수입니다.
# 800 는 홀수 입니다.
# 99 는 홀수 입니다.
# 코드
# numbers = [273,103,5,32,65,9,72,800,99]
# for number in numbers:
#     if number%2==0:
#         print(f'{number} 는 짝수입니다.')
#     print(f'{number} 는 홀수 입니다.')
# ==========================================
# 결과 2 [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[], [], []]

# 코드
# for number in numbers:
#     output[(number + 2)%3].append(number)
# print(output)
# ==========================================

# 결과
# i= 0, j=1
# i= 1, j=3
# i= 2, j=5
# i= 3, j=7
# [1, 4, 3, 16, 5, 36, 7, 64, 9]

# 코드
# numbers = [1,2,3,4,5,6,7,8,9]

# for i in range(0, len(numbers)//2):
#     j = (i * 2) + 1
#     print(f'i= {i}, j={j}')
#     numbers[j] = numbers[j] ** 2
# print(numbers)
# ==========================================

# 딕셔너리 요소 추가하기
# dic = {}

# print("요소 추가 이전:", dic)

# dic["name"] = '새로운 이름'
# dic["head"] = "새로운 정신"
# dic["body"] = '새로운 몸'
# del dic["name"] = "새로운 이름"  # 딕셔너리 삭제
# print("요소 추가 이후:", dic)
# ==========================================

# 딕셔너리 조합
# pets = [{"name": "구름", "age": 5},
#         {"name": "초코", "age": 3},
#         {"name": "아지", "age": 1},]

# for key in pets:
#     print(f'{key["name"]} {key["age"]}살')
# ==========================================

# 숫자가 몇번 등장하는지 출력하는 코드
# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] = counter[number] + 1
#     else:
#         counter[number] = 1
# print(counter)


# dic = {
#     'name': '7d 건조 망고',
#     'type': '다절임',
#     'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
#     'origin': '필리핀'
# }

# for key in dic:
#     print(smell_key, ':', dic[key])


# ==========================================

# 결과
# name : 기사
# level : 12       
# sword : 불꽃의 검
# armor : 풀플레이트
# skill : 베기
# skill : 세게 베기
# skill : 아주 세게 베기

# 코드
# char = {
#     "name": "기사",
#     "level": "12",
#     "items": {
#         "sword": "불꽃의 검",
#         "armor": "풀플레이트"
#     },
#     "skill": ["베기", "세게 베기", "아주 세게 베기"]
# }

# for key in char:
#     if type(char[key]) is dict:
#         for smell_key in char[key]:
#             print(smell_key, ':', char[key][smell_key])
#     elif type(char[key]) is list:
#         for elem in char[key]:
#             print(key, ':', elem)
#     else:
#         print(key, ':', char[key])
# ==========================================


# n  = 10
# a = range(0, int(n/2))
# print(list(a))

# for i in range(5, 10):
#     print(f'{i} = 반복 변수')
# ==========================================

# 역반복문 1
# for i in range(4, -1, -1):
#     print("현재 반복 변수: {}".format(i))

# 역반복문 2
# for i in reversed(range(5)):
#     print("현재 반복 변수{}".format(i))
# ==========================================

# 별 피라미드 삼각형
# for i in range(1,10):
#     for j in range(i):
#         print("*",end="")
#     print()
# 별 피라미드 삼각형 2
# output = ""
# for i in range(1,10):
#     for j in range(0, i):
#         output += "*"
#     output += "\n"
    
# print(output)
# ==========================================

# 반복문 피라미드 만들기
# output = ""
# for i in range(1,10):          
#     for j in range(10,i, -1): 
#         output += " "  
#     for k in range(1,i * 2):  
#         output += "*"
#     output += "\n"
# print(output)

#  ## 참고 ##
# output = ""

# for i in range(1, 10):
#     output += ("*" * i)
#     output += "\n"
# print(output)
# ==========================================


# list_a = [1,2,1,2]

# value = 3

# while value in list_a:
#     list_a.remove(value)
# print(list_a)

# 특정 시간동안 프로그램 정지 시키기 
# import time 

# number = 0

# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number+=1
# print("5초 동안 {}번 반복했습니다.".format(number))
# ==========================================

# break 
# i = 0

# while True:

#     print("{}번째 반복문입니다.".format(i))
#     i+=1
#     # 반복을 종료 합니다.
#     input_text = input("> 종료하시겠습니까?(y/n): ")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break

# ==========================================

# continue
# numbers = [5, 15, 6, 20, 7, 25]

# for number in numbers:
#     if number < 10:
#         continue
#     print(number)

# ==========================================


# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀"
# }

# key = input("> 접근하고자 하는 키: ")

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키")

# ==========================================


#  (2024. 08. 17)

# 문제 1
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# char = {}

# for i in range(len(key_list)):
#      char[key_list[i]] = value_list[i]
# # 최종 출력
# print(char)

# 결과: {'name': '기사', 'hp': 200, 'mp': 30, 'level': 5}
# ==========================================

# 문제 2
# limit = 10000
# i = 1
# sum_vlaue = 0

# while sum_vlaue<=limit:
#     sum_vlaue += i
#     i+=1

# print("{}를 더할 떄 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_vlaue))

# 결과: 141를 더할 떄 10000을 넘으며 그때의 값은 10011입니다.
# ==========================================

# 문제 3

# max_vlaue = 0
# a = 0
# b = 0

# for i in range(1, 100//2 + 1):
#     j = 100 - i

# temp = i * j
# if max_vlaue < temp:
#     a = i
#     b = j
#     max_vlaue = temp

# print("최대가 되는 경우: {} * {} = {}".format(a, b, max_vlaue))

# 결과: 최대가 되는 경우: 50 * 50 = 2500

# ==========================================
 
# list_a = [1,2,3,4,5]
# list_revered = reversed(list_a)

# print("# reversed() 함수")
# print("reversed([1,2,3,4,5]):", list_revered)
# print("list(reversed([1,2,3,4,5])):", list(list_revered))
# print()

# print("# reversed() 함수와 반복문")
# print("for i in reversed([1,2,3,4,5])):")
# for i in reversed(list_a):
#     print("-", i)

# ==========================================


# 안되는 예시
# temp = reversed([1,2,3,4,5,6])

# for i in temp:
#     print("첫 번째 반복문: {}".format(i))

# for i in temp:
#     print("두 번째 반복문: {}".format(i))

# 되는 예시
# numbers = [1,2,3,4,5,6]

# for i in reversed(numbers):
# 	print("첫 번째 반복문: {}".format(i))

# for i in reversed(numbers):
# 	print("두 번째 반복문: {}".format(i))

# ==========================================

# enumerate 함수
# example = ['요소A', '요소B', '요소C']

# print(list(enumerate(example)))
# 결과: [(0, '요소A'), (1, '요소B'), (2, '요소C')]

# for i, value in enumerate(example): 
#     print("{}번째 요소는 {}입니다.".format(i,value))

# ==========================================


# (2024.08.18)

# 딕셔너리의 items() 함수와 반복문 조합하기 

# example = {
#     "키A": "값A",
#     "키B": "값B",
#     "키C": "값C",
# }

# print("items():", example.items())

# for key, element in example.items():
#     print("dicionary[{}] = {}".format(key, element))
# ==========================================

# 리스트 안에 for문 사용

#  리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]   
# array = [i * i for i in range(0, 20, 2)]
# print(array)

#  리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
# array = ['사과', '자두', '초콜릿', '바나나', '체리']
# output = [fruit for fruit in array if fruit !='초콜릿']
# print(output)
# ==========================================

# 문자열.join(문자열로 구성된 리스트) 함수

# n = int(input('정수 입력> '))
# if n % 2==0:
#     print("\n".join([
#         '입력한 문자열은 {}입니다.',
#         '{}는(은) 짝수입니다.'
#     ]).format(n,n))
# else:
#     print("\n".join([
#         '입력한 문자열은 {}입니다.',
#         '{}는(은) 홀수입니다.'
#     ]).format(n,n))
# ==========================================

# next() 함수를 적용해 하나하나 꺼낼 수 있는 요소를 이터레이터라고 한다.

# n = [1,2,3,4,5,6]
# r_num = reversed(n)

# print("reversed_number : ", r_num)  #여기서 이터레이터가 나옴.
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# ==========================================

# # 10진수 --> 2진수
# print("{:b}".format(10))
# print(int("1010",2))

# # 10진수--> 8진수
# print("{:o}".format(10))
# print(int("12",8))

# # 10진수--> 16진수
# print("{:x}".format(10))
# print(int("10",16))
# ==========================================
# print("안녕안녕하세요".count("안"))  == 문자열을 매개변수로 넣어야함.

# ==========================================

# 마무리 문제: 1 ~ 100 사이 숫자 중 2진수로 변환했을 떄 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드를 만들어 보시오.
# output = [i for i in range(1,100+1) 
#           if "{:b}".format(i).count("0") == 1]

# for i in output:
#     print("{} : {}".format(i, "{:b}".format(i)))
# print("합계:", sum(output))

# 결과: 
# 2 : 10
# 5 : 101
# 6 : 110
# 11 : 1011
# 13 : 1101
# 14 : 1110
# 23 : 10111
# 27 : 11011
# 29 : 11101
# 30 : 11110
# 47 : 101111
# 55 : 110111
# 59 : 111011
# 61 : 111101
# 62 : 111110
# 95 : 1011111
# 합계: 539
# ==========================================

# (2024. 08. 19)
# 도전 문제

# 1. 숫자의 종류

# num_list = [1,2,3,4,1,2,3,1,4,1,2,3]
# answer = {}

# for i in num_list:
#     if i not in answer:
#         answer[i] = 0
#     answer[i] += 1

# print("{}에서".format(num_list))
# print("사용된 숫자의 종류는 {}개입니다.".format(len(answer)))
# print("참고: {}".format(answer))

# 결과: [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]에서
        # 사용된 숫자의 종류는 4개입니다.
        # 참고: {1: 4, 2: 3, 3: 3, 4: 2}
# ==========================================

# 2. 염기의 개수

# a = input("염기 서열을 입력해 주세요: ")
# DNA = {
#     'a': 0,
#     't': 0,
#     'g': 0,
#     'c': 0
# }

# for i in a:
#     DNA[i] +=1

# for key in DNA:
#     print(f'{key}의 개수: {DNA[key]}')

# 입력 값: ctacaatgtcagtatacccattgcattagccg

# 결과: 
# 염기 서열을 입력해 주세요: ctacaatgtcagtatacccattgcattagccg
# a의 개수: 9
# t의 개수: 9
# g의 개수: 5
# c의 개수: 9
# ==========================================

# 3. 염기 코돈 개수

# a = input("염기 서열을 입력해주세요: ")

# counter = {}

# for i in range(0,len(a)+1, 3):
#     condon = a[i:i+3]
#     if len(condon) == 3:
#         if condon not in counter:
#             counter[condon] = 0
#         counter[condon] += 1
# print(counter)

# 결과:
# 염기 서열을 입력해주세요: ctacaatgtcagtatacccattgcattagccg
# {'cta': 1, 'caa': 1, 'tgt': 1, 'cag': 1, 'tat': 1, 'acc': 1, 'cat': 1, 'tgc': 1, 'att': 1, 'agc': 1}
# ==========================================

# 4. 2차원 리스트 평탄화
# list_a = [1,2,[3,4], 5, [6,7], [8,9]]
# list_flatten = []

# for elem in list_a:
#     if type(elem) == list:
#         for ans in elem:
#             list_flatten.append(ans)
#     else:
#         list_flatten.append(elem)

# print(f'{list_a}를 평탄화하면\n {list_flatten}입니다.')

# 결과:
# [1, 2, [3, 4], 5, [6, 7], [8, 9]]를 평탄화하면
# [1, 2, 3, 4, 5, 6, 7, 8, 9]입니다.
# ==========================================

# end
