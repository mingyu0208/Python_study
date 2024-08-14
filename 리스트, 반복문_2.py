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

# 코드
numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(numbers)//2):
    j = (i * 2) + 1
    print(f'i= {i}, j={j}')
    numbers[j] = numbers[j] ** 2
print(numbers)

