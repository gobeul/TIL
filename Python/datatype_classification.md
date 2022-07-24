# 자료형 분류

### 자료형 이란?
프로그래밍에서는 다양한 종류의 값(데이터)을 쓸 수 있다.<br>
사용할 수 있는 데이터의 종류들을 자료형(datatype) 이라고 한다.

### 수치형
- int (정수)
- float (부동 소수점)<br>
  실수의 값 처리 시 의도치 않는 결과가 나올 수 있다.<br>
  ```python
  print(3.2 - 3.1)
  >> 0.10000000000000009
  ```
  컴퓨터는 2진수를 사용하고, 0.1 은 2진수로 표현시에 무한대로 반복되기 때문에 10진법의 근사값으로 표현한다. 하지만 이 값은 0.1은 아니다.<br>
  고로 3.2 - 3.1 이 0.1과 같은 값인지 정확하게 비교할 수가 없으며,<br>
  이러한 오류를 [Floating point rounding error](#floating-point-rounding-error) 라고 한다.
- complex
- 진수 표현
```python
print(0b10) # 2진수(0b)
>> 2
print(0o30) # 8진수(0o)
>> 24
print(0x10) # 16진수(0x)
>> 16
```

### 문자형 
모든 문자는 string 타입이다.
- Escape sequence (역슬래시 \ ) _ 이스케이프 시퀀스 역시 문자열이다.<br>
  \n : 줄바꿈<br>
  \t : 탭<br>
  \r : 캐리지 리턴 - 커서를 현재 줄의 맨 앞으로 옮긴다.<br>
  ```python
  print("원숭이 \r 투")
  >> 투숭이
  ```
  \0 : 널<br>
  \ \ : \ \
  \ ' : 단일 인용부호(')<br>
  \ " : 이중 인용부호(")<br>
  문자열이기 때문에 `print("\n"*5)` 이런식의 연산도 가능하다.
- 문자열을 변수로 사용하는 법<br>
  - f-string (python 3.6이상)
  ```python
  name = "철수"
  print(f"{name}야, 안녕?")
  >> 철수야, 안녕?
  ```
- 문자열 또한 연산이 가능하다.<br>
  ```python
  show = "무한도전"
  print(show+"은 재미있다.")
  >> 무한도전은 재미있다.
  ```

<br>

### bool 자료형
논리 자료형으로 참과 거짓을 표현한다. (True, False)
- 비교연산자<br>
  <, <=, < , <=, >, >=, ==, !=, is (객체 아이텐티티 OOP), is not
- 논리 연산자<br>
  and, or, not<br>
  논리연산자 또한 우선 순위가 존재한다.
  not - and - or <br>
  ```python
  not True and False or not False 
  == ((not True) and False ) or (not False))
  == True
  ```
  가로를 없애면 코드 길이는 줄어든다. 하지만 가독성이 좋지 않다.
  짧은 코드와 가독성코드 어느것이 좋은 코드 일까???
- Falsy<br>
  엄밀하게 False 는 아니다 하지만 False로 취급되는 값.<br>
  ex) `0, 0.0, (), {}, [], None, ""`

- None<br>
  파이썬 자료형 중 하나로 값이 '없음'을 나타낸다. 일반적으로 반환값이 없는 함수에 사용된다.

### Floating point rounding error
이러한 오류를 해결하기 위해 다양한 방법이 있다.

- 반올림 함수를 이용하는 방법<br>
- math 모듈의 isclose() 를 사용하는 방법<br>
  ```python
  import math
  n1 = 0.1*3
  n2 = 0.3
  math.isclose(n1, n2)
  >> True
  ```
