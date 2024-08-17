# PYTHON  정리


> # 첫 (2024.08.12) 자료형

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



> # extend() 함수 (2024.08.13)

```extend
list_a =[1,2,3]
list_b =[4,5,6]
list_a.extend(list_b)  
print(list_a)
```

list_a 는 [1,2,3,4,5,6] 으로 파괴적 처리를 함.

일반적으로 list_a + list_b 한 것 과는 다름.



> # 파이썬 특정 값이 어떤 자료형인지 확인하는 법 (2024.08.14)


```
type("문자열")is str	# 문자열인지 확인
type([])is list		# 리스트인지 확인
type({})isdict		# 딕셔너리인지 확인
```



> # 반복문 피라미드 만들기 **(2024. 08. 15)**

```
output = ""

for i inrange(1,10):

    for j inrange(10,i, -1):

    output +=" "

    for k inrange(1,i *2):

    output +="*"

    output +="\n"

print(output)
```

결과 :

    *
        ***
       *****
      *******
     *********
    ***********



> # 4가지 키워드로 정리하느 핵심 포인트(2024. 08. 16)

* **범위**는 정수의 범위를 나타내는 값입니다. `range()` 함수로 생성합니다.
* `while` 반복문은 조건식을 기반으로 특정 코드를 반복해서 실행할 대 사용하는 구문입니다.
* `break` 키워드는 반복문을 벗어날 때 사용하는 구문입니다
* `continue `키워드는 반복문의 현재 바복을 생략할 때 사용하는 구문입니다.



> # 문제풀기 (2024. 08. 17)

```
# 문제 1
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
char = {}

for i in range(len(key_list)):
     char[key_list[i]] = value_list[i]
# 최종 출력
print(char)

# 결과: {'name': '기사', 'hp': 200, 'mp': 30, 'level': 5}
==========================================

# 문제 2
limit = 10000
i = 1
sum_vlaue = 0

while sum_vlaue<=limit:
    sum_vlaue += i
    i+=1

print("{}를 더할 떄 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_vlaue))

# 결과: 141를 더할 떄 10000을 넘으며 그때의 값은 10011입니다.
==========================================

# 문제 3

max_vlaue = 0
a = 0
b = 0

for i in range(1, 100//2 + 1):
    j = 100 - i

temp = i * j
if max_vlaue < temp:
    a = i
    b = j
    max_vlaue = temp

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_vlaue))

# 결과: 최대가 되는 경우: 50 * 50 = 2500

==========================================
```



> # 문자열, 리스트, 딕셔너리와 관련된 기본 함수 (2024. 08. 18)

* 리스트 뒤집기: `revered()`
* 현재 인덱스가 몇 번째인지 확인하기: `enumerate()`
* 딕셔너리로 쉽게 반복문 작성하기: `items()`
* 리스트 안에 for문 사용하기: 리스트 내포


> #### 제너레이터

```
# 안되는 예시
temp = reversed([1,2,3,4,5,6])
for i in temp:
    print("첫 번째 반복문: {}".format(i))

for i in temp:
    print("두 번째 반복문: {}".format(i))

# 되는 예시
numbers = [1,2,3,4,5,6]

for i in reversed(numbers):
	print("첫 번째 반복문: {}".format(i))

for i in reversed(numbers):
	print("두 번째 반복문: {}".format(i))
```


> #### **enumerate 함수**

```
example = ['요소A', '요소B', '요소C']
print(list(enumerate(example)))
결과: [(0, '요소A'), (1, '요소B'), (2, '요소C')]

for i, value inenumerate(example):  
	print("{}번째 요소는 {}입니다.".format(i,value))

결과:   0번째 요소는 요소A입니다.
	1번째 요소는 요소B입니다.
	2번째 요소는 요소C입니다.
```
