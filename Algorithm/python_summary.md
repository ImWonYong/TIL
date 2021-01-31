# 코딩 테스트를 위한 Python 문법

## 자료형
### 수 자료형
정수형
```python
a = 1000 # 양의 정수
print(a)

a = -7 # 음의 정수
print(a)

# 0
a = 0
print(a)
```
실수형
```python
# 양의 실수
a = 157.39
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 10억의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3594e-3
print(a)
```
- 보통 컴퓨터 시스템은 수 데이터 처리 시 2진수 사용, 실수 처리할 때 부동 소수점 방식 이용.
- 가장 널리 쓰이는 IEEE754 표준에서 실수형 저장하기 위해 4바이트, 8바이트 고정된 크기에 메모리를 할당하기 때문에 실수 정보 표현하는 정확도에 한계를 가짐.
```python
a = 0.3 + 0.6
print(a)

if a == 0.9:
	print(True)
else:
	print(False)
```
- 따라서 소수점 값을 비교하는 작업 시에 round() 함수 이용
```python
a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
	print(True)
else:
	print(False)
```
- 흔히 코딩 테스트에서 실수 데이터 비교할 때 소수점 다섯 번째 자리에서 반올림한 결과가 같으면 정답으로 인정하는 식으로 처리함.

수 자료형 연산
```python
a = 7
b = 3

# 나누기
print(a / b)

# 나머지
print(a % b)

# 몫
print(a // b)

# 거듭제곱
print(a ** b)
```
### 리스트 자료형
리스트 만들기
- 리스트는 대괄호 안에 원소를 넣어 초기화하여, 쉼표로 구분
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 인덱스 4, 즉 다섯 번째 원소에 접근
print(a[4])

# 빈 리스트 선언 방법 1)
a = list()
print(a)

# 빈 리스트 선언 방법 2)
a = []
print(a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)
```

리스트의 인덱싱과 슬라이싱
- 특정한 원소에 접근하는 것을 인덱싱이라 함
- 파이썬에서는 음의 정수를 넣으면 거꾸로 탐색
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경
a[3] = 7
print(a)
```
- 연속적인 위치를 갖는 원소를 가져올 때 슬라이싱 이용
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])
```
리스트 컴프리헨션
- 리스트를 초기화하는 방법 중 하나
- 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화
```python
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

#일반적인 소스코드 방식
array = []
for i in range(20):
	if i % 2 == 1:
		array.append(i)

print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]

print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
```
- 언더바(_)는 어떤 일을 하나?
	- 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바 사용
```python
for _ in range(5):
	print("hello world")
```

- 특정 크기의 2차원 리스트를 초기화 할 때는 반드시 리스트 컴프리헨션 이용해야 함.
```python
# N X M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)
```
- 내부적으로 포함된 리스트가 모두 동일한 객체에 대한 레퍼런스로 인식되기 때문

리스트 관련 기타 메서드
```python
a = [1, 4, 3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬: ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)
```
- remove_all() 같은 함수 제공하지 않기 때문에 다음과 같은 방법을 쓰면 좋다.
```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
```
### 문자열 자료형
문자열 초기화
```python
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)
```
문자열 연산
```python
a = "Hello"
b = "World"

print(a + " " + b)

a = "String"

print(a * 3)

# 문자열은 내부적으로 리스트와 같이 처리
# 인덱싱과 슬라이싱 사용 가능
a = "ABCDEF"
print(a[2 : 4])
```
### 튜플 자료형
- 튜플은 한 번 선언된 값을 변경할 수 없다.
- 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용한다.
```python
a = (1, 2, 3, 4)
print(a)

# 오류
a[2] = 7
```
### 사전 자료형
- 키와 값의 쌍을 데이터로 가지는 자료형
- 내부적으로 '해시 테이블'을 이용하므로 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있음
```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

# in 문법은 리스트, 문자열, 튜플같은 iterable 자료형에 모두 사용 가능
if '사과' in data:
	print("'사과'를 키로 가지는 데이터가 존재합니다.")
```
사전 자료형 관련 함수
```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in keyu_list:
	print(data[key])
```
### 집합 자료형
집합 자료형 소개
- 중복을 허용하지 않는다.
- 순서가 없다.
- 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
```python
# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)
```
집합 자료형의 연산
```python
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
```
집합 자료형 관련 함수
```python
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
```
