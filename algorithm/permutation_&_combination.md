# 조합과 순열
## 순열 Permutation
서로 다른 n 개의 원소에서 r개를 중복없이 뽑은 후 순서를 가지도록 정렬하는 것

=> n! / (n-r)!
## 조합
서로 다른 n개의 원소중 r개를 순서없이 골라낸 것.<br>
nCr

=> nCr = n! / ((n-r)! x r!)

# 알고리즘 구현해보기.
### N 개의 원소중에서 M개 뽑기
### 중복없이, 순서 구분
```python
def recur(step):
    if step == M: # step 가 0 부터 1개씩 증가하여 M까지 되면 만든 리스트 출력.
        print(*arr)
        return
    for i in range(1, N+1):
        if not visited[i]:
            arr[step] = i
            visited[i] = True
            recur(step+1)
            visited[i] = False
            
N, M = 숫자, 숫자
arr = [0 for _ in range(M)] # M 개 배열 미리 생성, 덮어 쓸거다.
visited = [False]*(N+1) # 중복을 피하기 위한 방문처리 리스트

recur(0)
```

### N 개의 원소중에서 M개 뽑기
### 중복없이, 순서 상관 없이
```python
def recur(step, start): # 순서 및 중복을 컨트롤 해줄 start
    if step == M:
        print(*arr)
        return
    for i in range(start, N+1):
        arr[step] = i
        recur(step+1, i+1) # i +1 => 방금 바꿔준거보다 하나 크게

N, M = 숫자, 숫자
arr = [0 for _ in range(M)]

recur(0, 1) # 숫자가 1부터 배정이니깐 start 를 1로
```

### N 개의 원소중에서 M개 뽑기
### 중복가능, 순서 구분해서
```python
def recur(step):
    if step == M:
        print(*arr)
        return
    for i in range(1, N+1): # 중복 허용으로 제한조건이 적다.
        arr[step] = i
        recur(step+1)

N, M = map(int, input().split())
arr = [0 for _ in range(M)]

recur(0)
```