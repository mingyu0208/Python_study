# PYTHON 기초 정리하기

**(2024.08.12)**  3.py memo 새로운 함수들을 알았다 나중에 써먹기 좋을 듯ㅎ

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

**(2024.08.13)** 4.py
