# 동작시간 줄여보기.

### copy() 는 꽤나 느린 모듈이다. (2020년)
copy() 는 느리고 deepcopy는 더느리다.

슬라이싱으로 대체 해 보자.<br>
copy() -> a[:]
copy.deepcopy() -> b = [ i[:] for i in a ]

### 리스트 요소 끼리의 연선이 필요할때
```python
a = [ [1,2,3], [4, 5, 6], [7,8,9] ]

x = 1 + a[0][0]
y = 2 + a[0][1]
z = 3 + a[0][2]
# 이렇게 인덱스로 접근하는 것보다


for (dx, dy, dz) in a:
  x = 1 + dx
  y = 2 + dy
  z = 3 + dz

#이렇게 for 문 돌리면서 튜플로 묶어서 저장하는게 더 빠르다.
```

### 전체를 함수로 묶어서 처리하는게 더 빠르다.