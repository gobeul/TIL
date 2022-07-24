# 유클리드 호제법
## 최대공약수(GCD), 최소공배수(LCM) 구하기.
> 2부터 1씩 늘려가며 찾는 방법의 시간 복잡도는 O(N)인 반면<br>
> 유클리드 호제법의 시간복잡도는 O(logN) 이다.

---
### 최대공약수(GCD, Greatest Common Divisor)
> 두 정수 a, b 가 있고 (a > b), <br>
> a%b == r 이고  r != 0 이라면<br>
> a와 b의 최대 공약수는 b 와 r의 최대 공약수와 같다.<br>
> GCD(a,b) == GCD(b,r)

코드 구현
```python
def GCD(a, b):
    if a == b:
        return a
    elif a > b:
        r = a%b
        if r == 0:
            return b
        else:
            return GCD(b, r)
    else:
        r = b%a
        if r == 0:
            return a
        else:
            return GCD(a, r)
```


---
### 최소공배수 (LCM, Least Common Multiple)
> 두 정수 a, b의 최대 공약수를 g 라고 할때,<br>
> a와 b의 최소공배수는 (a\*b)/g 와 같다.
> LCM(a,b) == (a\*b) / GCD(a,b)

코드 구현
```python
def LCM(a, b):
    G = GCD(a, b)
    return (a*b)//G
```


---
### 관련문제
- [백준 1934번](https://www.acmicpc.net/problem/1934)