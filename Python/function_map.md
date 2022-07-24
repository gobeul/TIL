# map
`map(function, iterable)`

순회가능한 데이터(iterable)의 모든 요소에 함수(function)를 적용하고 그 결과를 map object로 반환한다.
```python
a = [1, 2, 3, 4, 5]

def pp(a):
    return a+10

map_a = map(pp, a)
print(map_a)
>> <map object at 0x0000029A4BECAEF0>

### list 로 감싸주면 map object를 확인할 수 있다.
print(list(map_a))
>> [11, 12, 13, 14, 15]
```
