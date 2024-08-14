# ====================================================================== 자료형, 조건문 1p ~ 188p 
# 2024.08.08 
# 1장 파이썬 시작하기 
# 이진 숫자: 0과 1로 이루어진 수.
# 프로그래밍 언어: 컴퓨터가 이해할 수 있는 이진 코드로 벼호나되는 것을 목표로 만들어진, 사람이 쉽게 이해라 수 있는 형대의 언어.
# 소스 코드 : 사람들이 쉽게 일고 이해할 수 있도록 프로그래밍 언어로 작성한 코드.
# 인터프리터: 프로그래밍 소스 코드를 곧바로 실행해 주는 프로그램. 한 번에 코드 한 줄씩 읽어 실행.
# 식별자: 함수나 변수의 이름을 붙일 때 사용하는 단어. 
# 함수: 코드의 집합
# 리터럴: 소스 코드 내에서 직접 입력된 값.
# print("hello Coding Python")

# print("Hello! " *3)

# print("""동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세
# 무궁화 삼천리 화려강산 대한사람
# 대한으로 길이 보전하세
# """)

# ======================================================================
# 2024.08.11
# 자료형: 자료의 형태, --숫자: 실수, 정수 구분// --문자열: 큰따옴표 혹은 작은따옴표입력.
# 이스케이프 문자(escape character): \(백슬래시) 기호가 붙은 특수한 문자 리터럴, 문자열 내부에서 특수한 기능을 수행.
# 인덱스: 리스트, 문자열과 같은 자료형에서 자료가 메모리에 저장된 순서대로 매겨진 버호, 리스트 내부에서 값의 위치를 의미.
# 부동 소수점: 소수점이 있는 실수 데이터를 저장하는 방식.
# 캐스트: 어떤 자료형을 다른 자료형으로 바꾸는 것. 특히, input() 함수의 입력 자료형은 항상 문자열이기 떄문에 입력받은 문자열을 숫자로 변환해야 연산에 활용가능하다. ex) n = int(input())

# print("안녕" + "하세요"  *3)
# # 안녕하세요하세요하세요

# print("안녕" + ("하세요" * 3))
# # 곱하기가 우선으로 되는것이 맞아서 둘다 값이 같지만, 괄호를 하는 것이 좋다.

# print(type(2))
# # type 함수

# ======================================================================
# #  2024.08.12 
# #  2-4 숫자와 문자열의 다양한 기능

# # formmat함수
# print('{} {} {}'.format(10, 20, 30, 40))

# format_a = "{} {} {}".format(1, "문자열", True)
# print(format_a)

# # 특정 칸에 출력하기
# output_a = "{:5}".format(52)
# print(output_a)
# output_b = "{:10d}".format(52)
# print(output_b)

# # 빈칸을 0으로 채우기
# output_c = "{:05d}".format(52)  # 양수
# print(output_c)
# output_d = "{:05d}".format(-52) # 음수 
# print(output_d)

# # 기호 표시
# print("{:+d}".format(52))
# print("{:+d}".format(-52))
# print("{: d}".format(52))
# print("{: d}".format(-52))

# # 조합하기
# print("{:+5d}".format(52))
# print("{:+5d}".format(-52))
# print("{:=+5d}".format(52)) # 기호를 앞으로 밀기
# print("{:+05d}".format(52))
# print("{:+05d}".format(-52))

# #  부동 소수점 출력하기
# print("{:f}".format(52.253))
# print("{:+015f}".format(52.253))
# print("{:15.3f}".format(52.253))
# print("{:15.2f}".format(52.253))
# print("{:15.1f}".format(52.253))

# # 의미 없는 소수점 제거하기   {:g}
# output_1 = 52.0
# ouput_2 = "{:g}".format(output_1)
# print(output_1)
# print(ouput_2)

# # 문자열 양옆의 공백 제거하기 : strip()
# a = """
#     안녕하세요
# 문자열의 함수를 알아봅시다
#     """
# print(a.strip())            #stip() 공백제거

# # isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인
# b = "asdf123"
# print(b.isalnum()) 

# # isalpha(): 문자열이 알파벳으로만 구성되어 있는지 확인
# c = "asdf"
# print(c.isalpha())

# # isidentifier(): 문자열이 식별자로 사용할 수 있는 것인지 확인
# d = "abc"
# print(d.isidentifier())

# # isdecimal(): 문자열이 정수 형태인지 확인
# e = "1234"
# print(e.isdecimal())
# # isdigit(): 문자열이 숫자로 인식될 수 있는 것인지 확인

# # isspace(): 문자열이 공백으로만 구성되어 있는지 확인
# f = "   "
# print(f.isspace())
# # islower(): 문자열이 소문자로만 궁성되어 있는지 확인
# g = "abc"
# print(g.islower())

# # isupper(): 문자열이 대문자로만 구성되어 있는지 확인
# h = "ABC"
# print(h.isupper())


# # 문자열 찾기: find(), rfind() 특정 문자가 어디에 위치하는지 찾는 함수.
# str_a = "안녕안녕하세요".find("안녕")
# str_b = "안녕안녕하세요".rfind("안녕") 
# print(str_a)
# print(str_b)

# split_a = "10 20 30 40 50".split(" ")
# print(split_a)  

# # f스트링으로 하면 일일이 값을 넣어야 하는데,,
# data = ['별', 2, 'M', '서울특별시 강서구', 'Y']

# print(f"""이름: {data[0]}
#     나이: {data[1]}
#     성별: {data[2]}
#     지역 {data[3]}
#     중성화 여부: {data[4]}""")

# # format으로 하면 더 간단하게 입력 리스트 요소를 한꺼번에 출력할 수 있음.
# print("""이름: {}
#    나이: {}
#    성별: {}
#    지역: {}
#    중성화여부: {}""".format(*data)) #  '*'전개 연산자를 사용하여 리스트 내용을 전개함.


# # upper, lower 함수를 사용만 하면 원본은 절대 안 바뀜.
# upper_1 = 'abc'
# upper_1.upper()
# print(upper_1)

# 1. 구의 부피와 겉넓이 
# r = float(input())
# pi = 3.141925
# 부피 = (4/3) * pi * (r **3)
# 겉넓이 = 4 * pi * (r ** 2)
# print(f'구의 부피는: {부피}입니다.')
# print(f'구의 겉넓이는: {겉넓이}입니다.')

# 피타고라스의 정리
# w = float(input("밑변의 길이를 입력해주세요: "))
# h = float(input("높이의 길이를 입력해주세요: "))
# 빗변 = (w ** 2 + h ** 2) ** 0.5
# print(f'빗변의 길이는 {빗변}입니다.')

# @@@ 참고 @@@ 
# raise NotlmplementedError
#  "아직 구현하지 않은 부분이라는 오류를 강제로 발생시킬 수 있음!"

# ======================================================================

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