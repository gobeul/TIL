# 순열 Permutation
서로 다른 n 개의 원소에서 r개를 중복없이 뽑은 후 순서를 가지도록 정렬하는 것

=> n! / (n-r)!


### 모듈 없이 구현해보기
```python
## nPn 구현해보기 - 재귀함수 ##
def perm(i, k):
    if i == k :
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]


p = [1,2,3]
perm(0, 3)
####################################
##### nPn 방법2 ####################
def perm2(i, k):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if not uesd[j]:
                uesd[j] = True
                p[i] = a[j]
                perm2(i+1, k)
                uesd[j] = False

a = [1,2,3]
uesd = [False]*len(a)
p = [0]*len(a)

perm2(0, 3)
#####################################
##### nPr 방법 ######################
def perm3(i, n, r):
    if i == r:
        print(p)
    else:
        for j in range(n):
            if not uesd[j]:
                uesd[j] = True
                p[i] = a[j]
                perm3(i+1, n, r)
                uesd[j] = False

n = 5
r = 3
a = [i for i in range(1, n+1)]
uesd = [False]*n
p = [0]*r

perm3(0, n, r)
```


### 모듈 사용

```python
from itertools import permutations
```