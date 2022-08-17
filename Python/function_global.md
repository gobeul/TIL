# global

함수 내의 변수는 기본적으로 지역변수이다.<br>
함수 내의 변수 중 전역 변수로 사용하고 싶은 경우 `global`을 사용한다.

전역변수로의 전환이 필요한 경우는 함수내의 지역 네임스페이스에 없는 변수에 값을 할당하고 할 때 이다.

---
### 예시1
```python
def aa():
  print(test)

test = [1,2,3,4,5]  
aa()
>> [1, 2, 3, 4, 5]
```
test 는 전역 네임스페이스에 있는 변수다. `aa()`라는 함수내에서 test라는 변수를 호출했는데 함수의 지역 네임스페이스에는 `test`라는 변수가 없어서 전역 네임스페이스에서 test를 찾아 불러왔다.

---
### 예시2
```python
def aa():
  test[1] = 111

test = [1,2,3,4,5]  
aa()
print(test)
>> [1, 111, 3, 4, 5]
```
인덱스로 접근하여 값을 변경하는 것도 가능했다.

---
그런데...
### 예시3
```python
def aa():
  test += 90

test = 10
aa()
print(test)
>> UnboundLocalError: local variable 'test' referenced before assignment
```
오류가 난다..! 전역 네임스페이스에서 test 변수를 갑자기 불러오지 못하게 된 것일까??<br>
아니다. `test += 90` 을 조금 생각해 볼 필요가 있는데 이를 풀어쓰면

`test = test + 90` 이다. 이것이 의미 하는 것은 test 변수에 90 을 더한 값을 다시 test 변수에 할당하는 것인데<br>
함수내에서는 `지역 네임스페이스`안에 있는 test 라는 변수에 값을 할당하는 것으로 컴파일 된다.

그래서 지역 네임스페이스안에 없는 test라는 변수를 찾을려고 해서 오류가 나오는 것이다.

이는 마치 ..<br>
`test += 100`
test 변수 정의 없이 이렇게 시도하는 것으로 볼 수 있다.<br>

이를 해결하기 위해서 `global`을 이용해 test를 전역 변수로 선언해주면 해결된다.

```python
def aa():
  global test
  test += 90

test = 10
aa()
print(test)
>> 100
```