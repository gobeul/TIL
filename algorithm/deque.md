# deque
### 특징
- queue 가 선입선출의 방식으로 동작되는 반면, deque 는 앞쪽과 뒤쪽 양방향에서 요소의 추가 및 제거가 가능하다.<br>

- append() 및 pop() 등의 연산에서 deque 가 압도적으로 빠르다. O(n) vs O(1)

---
### 사용
```python
from collections import deque

deq = deque()
```
```python
deq = deque("python")
print(deq)

>> deque(['p', 'y', 't', 'h', 'o', 'n'])
```
<br>
데크 안에 리스트를 넣는다고 이중 배열로 생성되진 않는다.
<br>


```python
deq = deque(["python"])
print(deq)

>> deque(['python'])
```

---
### deque 메소드

  1. `popleft()` :  맨 왼쪽의 요소를 제거하고 변수에 저장한다.

```python
deq = deque(['p', 'y', 't', 'h', 'o', 'n'])
a = deq.popleft()
print(a)

>> p
```

2. `appendleft()` : 맨 왼쪽에 요소를 추가한다.

```python
deq = deque(['p', 'y', 't', 'h', 'o', 'n'])
deq.appendleft("a")
print(deq)

>> deque(['a', 'p', 'y', 't', 'h', 'o', 'n'])
```

3. `rotate()` : 데크의 [-1]의 요소를 [0]으로 옮긴다.

```python
deq = deque(['p', 'y', 't', 'h', 'o', 'n'])


deq.rotate(1) # 한 개옮긴다.
print(deq)
>> deque(['n', 'p', 'y', 't', 'h', 'o'])


deq.rotate(2) # 두 개 옮긴다.
print(deq)
>> deque(['o', 'n', 'p', 'y', 't', 'h'])


deq.rotate(-1) # 음수의 경우 방향을 바꾼다 [0]의 요소를 [-1]쪽으로 
print(deq)
>> deque(['y', 't', 'h', 'o', 'n', 'p'])
```
