# sort()
sort()의 시간복잡도는 O(nlogn) 이다. 이는 퀵,머지 등과 같은 시간복잡도를 보인다.

### sort(key= function )
`key= `를 이용하여 정렬에 조건을 추가할 수 있다.
```python
a = ["one", "two", "three", "four"]

a.sort()
print(a)
>> ['four', 'one', 'three', 'two']

a.sort(key=len) # len 함수
print(a)
>> ['one', 'two', 'four', 'three'] # 길이 순으로 정렬
```
---

`lambda` 함수를 사용하면 이중배열의 정렬도 다채롭게 가능하다.
```python
a = [[0,4,100], [5,50,3], [80,50,1], [-1, 120, 66]]

a.sort() # 디폴트 : 첫번째 인덱스 순서대로
print(a)
>>[[-1, 120, 66], [0, 4, 100], [5, 50, 3], [80, 50, 1]]

a.sort(key= lambda x : x[1]) # 1번 인덱스 순서대로
print(a)
>>[[0, 4, 100], [5, 50, 3], [80, 50, 1], [-1, 120, 66]]

a.sort(key= lambda x : (x[1], x[2])) # 1번 인덱스가 같은게 있다면 차순으로 2번 인덱스
print(a)
>> [[0, 4, 100], [80, 50, 1], [5, 50, 3], [-1, 120, 66]]
```
---
### sort() 의 리턴 값은 없다(None)
```python
a = [3,4,1,2]
p = a.sort()

print(p)
>> None
# sort()는 리스트의 요소를 바꿔주긴하지만 리턴하지는 않는다.
## 정렬된 리던값을 얻고 싶다면 p = sorted(a) 를 사용하자.
```