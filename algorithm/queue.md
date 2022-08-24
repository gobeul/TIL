# Queue 큐

스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조

선입선출(FIFO : First In First Out)

### 큐의 주요 연산
1. enQueue(item) : 뒤쪽(rear += 1)에 원소를 삽입하는 연산
2. deQueue() : 앞쪽(front)에서 원소를 삭제하고 반환하는 연산
3. creatQueue() : 공백 상태의 큐를 생성
4. isEmpty() : 큐가 공백상태인지를 확인(front == rear >> True? False??)
5. isFull() : 큐가 포화상태인지를 확인
6. Qpeek() : 앞쪽(front)에서 원소를 반환 (삭제는 하지 않는다. => deQueue()와 차이) 

### 선형큐
- 1차원 배열을 이용한 큐
> 큐의 크기 == 배열의 크기
> front 저장된 첫 번째 원소의 인덱스
> rear : 저장된 마지막 원소의 인덱스

- 상태 표현
> 초기 상태 : front = rear = -1
> 공백상태 : front == rear
> 포화상태 : rear == n-1 (배열의 크기 == n, 즉 n-1은 배열의 마지막 인덱스)

---
### 큐 생성
```python
Queue = [0]*n # 크기 n인 1차원 배열 생성
front, rear = -1, -1 # 프론트와 리어를 -1로 초기화

```
### 큐의 삽입 enQueue(item)
```python
def enQueue(item):
  global rear
  if isFull():
    print("큐가 가득참") # 디버깅용
  else:
    rear += 1
    Queue[rear] = item
  return

# 스택의 push와 매우 유사하군
```

### 큐의 삭제와 반환 deQueue()
```python
def deQueue():
  global front
  if isEmpty():
    print("큐가 비어있음")
  else:
    front += 1 # 옮기고 빼는 거야 (스택은 빼고 옮겼는데)
    return Queue[front]
```

### isEmpty(), isFull()
front = rear = n-1 이면 비어있으면서 가득참??
```python

```

### 검색 Qpeek()
```python

```

---
### 선형 큐의 문제점 - 잘 못된 포화인식
front 와 rear가 증가하면서 앞쪽이 비어있음에도 포화상태로 인식함.

- 해결방법 1<br>
  원소이동 -> 실행속가 너무 느리다.
- 해경방법 2<br>
  1차원배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정 = 원형 큐 -> 만능은 아니다..!

### 원형 큐 cQueue
초기 공백의 상태를 front, rear = 0 으로 둔다. (맨앞을 비워두는 느낌)

front 변수 - 

front = (rear + 1)%n 이면 가득 찬(Full) 상태가 된다.(n은 큐의 크기)<br>
front == rear 이면 비어있는 상태

### 원형 큐의 enQueue(item)

### 원형 큐의 deQueue(), delete()

---
### 우선순위 큐
원소들이 우선순위를 가진다.

FIFO 가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.

- 적용분야<br>
  시뮹레이션 시스템, 네트워크 트래픽제어, 운영체제 테스크 스케줄링 등..

### 우선순위 큐의 구현
1. 배열을 이용한 우선순위 큐
2. 리스트(일반적인 리스트의 의미가 아님) 이용한 우선순위 큐

배열을 이용하여 구현시에 원소를 삽입할때마다 원소의 재배치가 일어남으로<br>
소요되는 시간과 메모리 낭비가 크다. => 배열 + 트리구조로 보완