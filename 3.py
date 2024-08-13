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


