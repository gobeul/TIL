### 리스트 (시퀀스형 - 가변형)

여러개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용한다. <br>
파이썬에서는 리스트에 어떠한 자료형도 저장할 수 있고 리스트 안에 리스트를 넣는 것도 가능하다.<br>
생성이후 내용변경이 가능하다 ⇒ 가변자료형

`my_list = [] or my_list = list() # 리스트 생성`

<br>


### 인덱스를 통한 접근(시퀀스형)
```python
# 인덱스를 이용한 접근
boxes = [”a”, “b”, [”abc”, “defg”, “xyz”] ]

print(len(boxes)
>> 3

print(boxes[2])
>> [”abc”, “defg”, “xyz”]

print(boxes[2][-1])
>> xyz

print(boxes[-1][1][0])
>> d
```

### list comprehension
리스트 구조안에 제어, 조건문 등을 넣어 리스트를 만드는 방법.

형태 : `[코드 for 변수 in 시퀀스 컨테이너]`
```python
a = [num*5 for num in range(5)]
print(a)
>> [0, 5, 10, 15, 20]

# if절도 추가할 수 있다.
a = [num*5 for num in range(5) if num > 2]
# num 이 2보다 크다면 5를 곱해서 리스트에 추가.
print(a)
>> [15, 20]
```
