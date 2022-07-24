### 제어문
파이썬은 기본적으로 위에서 아래로 명령수행하는데, \
특정상황에 따라 코드를 선택적 실행(조건or분기)하거나 계속 실행(반복)할 때 사용한다.

'순서도'로도 작성이 가능하다.

<br>

---

<br>

### 조건문
참/거짓 을 판단할 수 있는 조건식과 사용한다. (True, False)
```python
if 조건1 :
	조건1이 참일 때 실행하는 코드
elif 조건2 :
	조건1이 거짓인데 조건2가 참일 때 실행하는 코드 
else:
	위 조건이 다 거짓인 경우 실행하는 코드

# 동시 검사가 아닌 위에서부터 하나씩 검증된다.
```

<br>

---

<br>


### 중첩 조건문
조건문 안에 조건문이 들어오는 것(들여쓰기)도 가능하다.
```python
if 조건1:
	if 조건2:
		조건1 이 참이고 조건2 가 참이면 실행
	else:
		조건1은 참이지만 조건2 가 거짓이면 실행
else:
	조건1 이 거짓이면 실행 (조건2는 관계없음)
```

<br>

---

<br>


### 조건 표현식 ( = 삼항 연산자)
조건문을 한줄로 표현한 것이다.

(조건이 Ture 인 경우의 값) if (조건) else (False 인 경우의 값)<br>
왼참 오거
```python
# num 의 절대 값을 value에 할당하는 코드

value = num if num>= 0 else -num
```

<br>

---

<br>


### 반복문
특정 조건을 만족할때까지 같은 동작을 계속하고 싶을때 사용한다.

반복문의 종류 : while 문, for 문<br>
반복제어 : break, continue, for-eles

### while 문
조건식이 True 라면 반복한다.<br>
종료 조건이 없다면 무한 루프에 빠진다.
```python
while 조건 :
	코드블럭 1
	코드블럭 2
	.
	.
	.
	코드블럭 N

	#들여쓰여 있는 코드블럭을 모두 실행(중간에 반복제어가 없다면) 후 조건을 다시 검토한다.
```

<br>

---

<br>


### for문
시퀀스(string, tuple, list, range, dictionary(3.7버전 이상))를 포함한 순회가능한 객체의 요소를 모두 순회한다. *set도 되던데..

dictionary 의 경우 디폴트는 key 값을 순회한다.<br>
- item() 메소드 사용시 key value 모두 순회 가능.
  ```python
	D = {"a" : 1, "b" : 2, "c" : 3}
	for a in D:
			print(a, end=" ")
	>> a b c  

	for a, b in D.items():
			print(a, b, end=", ")
	>> a 1, b 2, c 3,
	```
	
<br>

---

<br>


### enumerate()
for 문에서 시퀀스 순회시에 인덱스와 해당 값을 모두 가져올 수 있다.
```python
n = ["a", "b", "c"]

for a, b in enumerate(n):
    print(a, b, end=", ")

>> 0 a, 1 b, 2 c, 
```
enumerate(n, start=x) 의 방법으로 인덱스에 임이의 숫자를 더 해줄 수 있다.
```python
for a, b in enumerate(n, start=1):
    print(a, b, end=", ")

>> 1 a, 2 b, 3 c,

# 음수도 가능하다.
for a, b in enumerate(n, start=-5):
    print(a, b, end=", ")

>> -5 a, -4 b, -3 c,
```
enumerate(n)에서 n은 리스트 뿐만 아니라 시퀀스 형은 거의 다 쓸 수 있다. 

<br>

---

<br>

### 반복문 제어
- break<br>
  반복문을 강제 종료 시킨다.
- continue<br>
  continue 이후의 코드 블럭은 시행하지 않고 반복을 다시 수행한다. (스킵)
- for-else<br>
  만약 for 문이 온전히 실행 되었다면 else 문을 실행하고,<br>
	break 등으로 for 문이 모든 시퀀스를 순회하지 못했다면 else 문을 실행하지 않는다.
	```python
	for i in range(5):
    	print(i, end=" ")
	else:
    	print("")
    	print("for 문이 모두 실행되었다!")
	
	>>0 1 2 3 4 
	  for 문이 모두 실행되었다!

	# for 문이 모두 실행되지 못한경우
	for i in range(5):
    	print(i, end=" ")
    	if i == 3:
        	break
	else:
    	print("")
    	print("for 문이 모두 실행되었다!")

	>> 0 1 2 3
	```
- pass<br>
	아무것도 하지 않는다.
	코드 작성중에 중간중간 디버깅하기 위해서 쓰일 수 있다.