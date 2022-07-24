# zip
`zip(*iterables)`
여러개의 순회가능한 데이터(iterable)를 모아 인덱스 별로 짝을 지어 튜플형태로 반환한다.
```python
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]

zip_ex = zip(a, b)

print(list(zip_ex))
>> [(1, 'a'), (2, 'b'), (3, 'c')]
```
list a 의 3, 4번 인덱스는 짝이 없기때문에 반환되지 않았다.<br>
즉 zip 의 튜플요소의 총 개수는 요소의 개수가 가장 작은 데이터가 기준이 된다.