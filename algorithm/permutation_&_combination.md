# 조합과 순열
## 순열 Permutation
서로 다른 n 개의 원소에서 r개를 중복없이 뽑은 후 순서를 가지도록 정렬하는 것 (순서를 구분한다.)<pr>
nPr<br>
=> n! / (n-r)!

=> nPn == n!
## 조합
서로 다른 n개의 원소중 r개를 순서없이 골라낸 것.<br>
nCr

=> nCr = n! / ((n-r)! x r!)<br>
=> 재귀적 표현 : nCr = (n-1)C(r-1) + (n-1)Cr

=> nC0 = 1
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

### N 개의 원소중에서 M개 뽑기
### 중복가능, 오름 차순 정리
```python
def recur(s, last): # 오름 차순을 위해 last 변수를 정
    if s == M:
        print(*arr)
        return
    
    for i in range(last, N+1): # 중복 및 오름차순을 위해 시작은 last 부터
        arr[s] = i
        recur(s+1, i)

N, M = map(int, input().split())
arr = [0]*M

recur(0, 1)
```


### N 개의 원소중에서 M개 뽑기
### 주어진 원소안에서 중복불가, 순서 상관 있게
```python
def recur(s):
    if s == M:
        print(*arr)
        return
    
    for i in range(N):
        if not used[i]:
            arr[s] = nums[i]
            used[i] = True
            recur(s+1)
            used[i] = False



N, M = map(int, input().split())
nums = list(map(int, input().split())) # 주어진 숫자들
nums.sort() # 오름차순을 위한 정렬

used = [False]*N
arr = [0]*M
```


### N 개의 원소중에서 M개 뽑기
### 주어진 원소안에서 중복불가, 수열내의 순서는 오름 차순으로 
```python
def recur(s, last): # 수열내의 순서를 오름차순으로 잡기위해 인덱스는 항상 전보다 큰 값을 가지도록
    if s == M:
        print(*arr)
        return
    
    for i in range(last+1, N):
        if not used[i]:
            arr[s] = nums[i]
            used[i] = True
            recur(s+1, i)
            used[i] = False



N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

used = [False]*N
arr = [0]*M

recur(0, -1)
```


### N 개의 원소중에서 M개 뽑기
### 주어진 원소안에서 중복불가, 수열내의 순서는 오름 차순으로 
```python
def recur(s, last): # 수열내의 순서를 오름차순으로 잡기위해 인덱스는 항상 전보다 큰 값을 가지도록
    if s == M:
        print(*arr)
        return
    
    for i in range(last+1, N):
        if not used[i]:
            arr[s] = nums[i]
            used[i] = True
            recur(s+1, i)
            used[i] = False



N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

used = [False]*N
arr = [0]*M

recur(0, -1)
```


### N 개의 원소중에서 M개 뽑기
### 주어진 원소안에서 중복가능, 전체 출력은 사전순으로 
```python
def recur(s): # 바로 위에 문제에서 last 변수만 빠짐 => 중복가능함으로!!
    if s == M:
        print(*arr)
        return
    
    for i in range(N):
        if not used[i]:
            arr[s] = nums[i]
            used[i] = True
            recur(s+1)
            used[i] = False



N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

used = [False]*N
arr = [0]*M

recur(0)
```


### N 개의 원소중에서 M개 뽑기
### 주어진 원소안에서 중복가능, 수열내의 순서는 오름 차순으로 + 전체 출력은 사전순으로  
```python
def recur(s, last):
    if s == M:
        print(*arr)
        return

    for i in range(last, N):
        arr[s] = nums[i]
        recur(s+1, i)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = [0]*M

recur(0, 0)
```


### N 개의 원소중에서 M개 뽑기
### 주어진 원소안에서 중복 부분가능??, 수열내의 순서 구분 + 전체 출력은 사전순으로 + 주어진 원소 중에서 중복된 원소가 있을 수 있으며 중복된 만큼 원소를 사용할 수 있으나 수열 자체는 중복되면 안됨.
```python
def recur(s):
    if s == M:
        print(*arr)
        return

    for i in range(N):
        if cnt_nums[i] > 0: # visit 가 아니라 있는 만큼 사용 9가 2번 등장하면 2번 까지 사용할 수 있음.
            arr[s] = set_nums[i]
            cnt_nums[i] -= 1
            recur(s+1)
            cnt_nums[i] += 1

N, M = map(int, input().split())
nums = list(map(int, input().split()))

set_nums = sorted(list(set(nums))) # 중복 제거를 위해 set() 거쳐준다.
cnt_nums = [0]*len(set_nums) # set_nums 리스트에 i 인덱스의 값은 원래 집합(nums)에 몇번 등장하는지 cnt_nums리스트의 i인덱스에 작성
for i in nums:
    idx = set_nums.index(i)
    cnt_nums[idx] += 1

N = len(set_nums)
arr = [0]*M

recur(0)
```

### N 개의 원소중에서 M개 뽑기
### 주어진 원소안에서 중복가능, 수열내의 순서 구분 + 전체 출력은 사전순으로 + 주어진 원소 중에서 중복된 원소가 있을 수 있으며 있음 하지만 수열 자체는 중복되면 안됨.
```python
def recur(s):
    if s == M:
        print(*arr)
        return
    
    for i in range(N):
        arr[s] = set_nums[i]
        recur(s+1)


N, M = map(int, input().split())
nums = list(map(int, input().split()))

set_nums = list(set(nums)) # set 으로 중복만 제거하고 M개를 중복을 어용하여 뽑기
set_nums.sort()

N = len(set_nums)
arr = [0]*M

recur(0)
```

