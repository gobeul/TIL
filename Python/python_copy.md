# 얖은 복사와 깊은 복사 (shallow copy, deep copy)

### python에서 복사의 방법
- 할당 (assignment)
- 얕은 복사 (shallow copy)
- 깊은 복사 (deep copy)

### 할당
대입 연산자 ` = ` 를 사용한다.
```python
a = [1, 2, 3]
copy_a = a
print(a, copy_a)
>> [1, 2, 3] [1, 2, 3]

a[0] = "hello"
print(a, copy_a)
>> ['hello', 2, 3] ['hello', 2, 3]
```
cpoy_a 는 대입연산자(=)를 통해 a의 주소를 참조하고 있다.<br>
그래서 a 값에 변화가 생기면 a의 주소가 변하고 a의 주소를 참조하고 있는 copy_a도 동일하게 변하게 된다.

### 얕은 복사
슬라이싱하여 넣어 주거나 ` .copy() ` 를 사용한다.
```python
a = [1, 2, 3]
copy_a = a
print(a, copy_a)
>> [1, 2, 3] [1, 2, 3]

a[0] = "hello"
print(a, copy_a)
>> ['hello', 2, 3] [1, 2, 3]
```

### 깊은 복사
` import copy ` 로 모듈을 불러온뒤에 `copy.deepcopy()`를 사용해서 복사한다.
