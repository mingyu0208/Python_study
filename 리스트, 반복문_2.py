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

numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for number in numbers:
    output[].append(number)
print(output)