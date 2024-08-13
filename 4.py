# 2024.08.13
# 03-1 불 자료형과 if조건문
#  pass 곧 개발하겠다는 뜻

# 1. 간단한 대화 프로그램
# import datetime
# a = input()
# now = datetime.datetime.now()
# if a =='안녕' or a=='안녕하세요.':
#     print('안녕하세요')
# elif a == '지금 몇 시야?' or a=='지금 몇 시예요?':
#     print('지금음 {}시입니다.'.format(now.hour)) 
# else:
#     print(a)

# datetime 시간
# import datetime
# now = datetime.datetime.now()
# print(now.year, '년')
# print(now.month, '월')
# print(now.day, '일')
# print(now.hour, '시')
# print(now.minute, '분')
# print(now.second, '초')

#  2. 나누어 떨어지는 숫자
# b = int(input())
# if b%2==0:
#     print(f'{b}는 2로 나누어 떨어지는 숫자 입니다.')
# else:
#     print(f'{b}는 2로 나누어 떨어지지 않는 숫자가 아닙니다.')

# if b%3==0:
#     print(f'{b}는 3로 나누어 떨어지는 숫자 입니다.')
# else:
#     print(f'{b}는 3로 나누어 떨어지는 숫자가 아닙니다.')

# if b%4==0:
#     print(f'{b}는 4로 나누어 떨어지는 숫자 입니다.')
# else:
#     print(f'{b}는 4로 나누어 떨어지는 숫자가 아닙니다.')

# if b%5==0:    
#     print(f'{b}는 5로 나누어 떨어지는 숫자 입니다.')
# else:
#     print(f'{b}는 5로 나누어 떨어지는 숫자가 아닙니다.')


#  04-1  리스트와 반복문
# 리스트 끼리 더하기
# list_a = [1,2,3]
# list_b = [4,5,6]
# print(list_a+ list_b) # [1, 2, 3, 4, 5, 6]
