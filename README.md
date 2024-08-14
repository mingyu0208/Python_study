# PYTHON 모르는 것  만 정리.

**(2024.08.12)** 자료형, 조건문.py

##memo## 새로운 함수들을 알았다 나중에 써먹기 좋을 듯 ㅎ

```python
# isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인
b = "asdf123"
print(b.isalnum()) 

# isalpha(): 문자열이 알파벳으로만 구성되어 있는지 확인
c = "asdf"
print(c.isalpha())

# isidentifier(): 문자열이 식별자로 사용할 수 있는 것인지 확인
d = "abc"
print(d.isidentifier())

# isdecimal(): 문자열이 정수 형태인지 확인
e = "1234"
print(e.isdecimal())
# isdigit(): 문자열이 숫자로 인식될 수 있는 것인지 확인

# isspace(): 문자열이 공백으로만 구성되어 있는지 확인
f = "   "
print(f.isspace())
# islower(): 문자열이 소문자로만 궁성되어 있는지 확인
g = "abc"
print(g.islower())

# isupper(): 문자열이 대문자로만 구성되어 있는지 확인
h = "ABC"
print(h.isupper())
```

**(2024.08.13)** 리스트, 반복문.py

# extend() 함수

```extend
list_a =[1,2,3]
list_b =[4,5,6]
list_a.extend(list_b)  
print(list_a)
```

list_a 는 [1,2,3,4,5,6] 으로 파괴적 처리를 함.

일반적으로 list_a + list_b 한 것 과는 다름.

(2024.08.14)   # 딕셔너리

# 파이썬 특정 값이 어떤 자료형인지 확인하는 법

```
type("문자열")is str	# 문자열인지 확인
type([])is list		# 리스트인지 확인
type({})isdict		# 딕셔너리인지 확인
```
