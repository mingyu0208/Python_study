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


