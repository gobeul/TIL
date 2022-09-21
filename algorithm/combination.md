# 조합
서로 다른 n개의 원소중 r개를 순서없이 골라낸 것.<br>
nCr

nCr = n! / ((n-r)! x r!)

### 재귀적 접근
nCr = n-1Cr-1 + n-1Cr

```python
def nCr(s, r, lst, j):
    if s == r:
        print(lst)
        return

    for i in range(j+1, n-r+1+s):
        nCr(s+1, r, lst+[arr[i]], i)

n = 10
arr = [i for i in range(1, n+1)]


nCr(0, 3, [], -1)

n = 10
arr = [i for i in range(1, n+1)]

nCr(0, 3, [])
```