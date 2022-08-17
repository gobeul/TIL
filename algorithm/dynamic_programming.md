# 다이나믹 프로그래밍 DP

최적화 문제를 해결하는 알고리즘.

작은 부분의 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 문제들을 해결하는 알고리즘.

Memoization 은 DP 의 핵심 스킬이라고 할 수 있음!

### DP를 이용한 피보나치
```python
# 테이블 크기를 주지 않고 푸는방법
def fibo2(n):
  f = [0, 1]

  for i in range(2, n+1):
    f.append(f[i-1] + f[i-2])
  
  return f[n]

print(fibo2(40))

# 테이블 크기를 주고 푸는 법
def fibo3(n):
  memo[0] = 0
  memo[1] = 1
  for i in range(2, n+1):
    memo[i] = memo[i-2] +  memo[i-1]
  return

memo = [0]*101
fibo3(100)
print(memo[40])

## n이 커질수록 append보다 크키를 주고 푸는게 더 빠르다!
```

### 재귀? 반복문?
Memoization 을 재귀적 구조에 사용하는거 보다는 반복적 구조로 Dp를 구현한 것이 성능면에서 보다 효율적이다.<br>
왜냐?? -> 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문. 함수를 호출, 복귀 자체로도 시간이 들기 떄문임