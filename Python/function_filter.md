# filter
`filter(function, iterable)`

순회가능한 데이터(iterable)의 모든 요소에 함수(function)를 적용하고 그 결과가 True라면 map object로 반환한다.

```python
a = [1, 2, 3, 4, 5]

def pp(a):
    return a-3

filter_a = filter(pp, a)

print(list(filter_a))
>> [1, 2, 4, 5]
```
결과값이 0 인 것은 False(Falsy)이기 때문에 반환하지 않았다.<br>
그래서 리스트 길이가 하나 줄어듬.