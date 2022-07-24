### 딕셔너리 (시퀀스 - 가변형)
key-value 쌍으로 이루어진 자료형<br> (버전 3.7부터는 시퀀스형, 이전 버전은 비 시퀀스형)<br>
` a = {"key" : value } `

`my_dict = {} or my_dict = dict() # 딕셔너리 생성`

### key
키는 변경불가능한 데이터만 만 활용가능,, string, integer, float, boolean, tuple, range<br>
key 를 통해 value 에 접근한다.
```python
print(a["key"])
>> value
``` 

### value
모든 종류의 데이터가 할당 가능하다.

<<<<<<< HEAD
---
=======
### 딕셔너리에 값 추가하기
```python
D = dict()
D["아무거나"] = 3 # 값 추가 방법
print(D)

>> {'아무거나': 3}
```

>>>>>>> 9e1d539f3e7dd80feac1d371c695533206eefca6

# 관련 메소드

### .key() / .value() / .items()
```python
a = {
    "김밥" : 3000, 
    "라면" : 4000, 
    "아메리카노" : 3000, 
    "구운 계란" : 1000, 
    "빵" : 1000,
    "카페라떼" : 3500
}

print(a.keys()) # .keys()
>> dict_keys(['김밥', '라면', '아메리카노', '구운 계란', '빵', '카페라떼'])
>> 타입은 <class 'dict_keys'>

print(a.values()) # .valuse()
>> dict_values([3000, 4000, 3000, 1000, 1000, 3500])
>> 타입은 <class 'dict_values'>

print(a.items()) #.items()
>> dict_items([('김밥', 3000), ('라면', 4000), ('아메리카노', 3000), ('구운 계란', 1000), ('빵', 1000), ('카페라떼', 3500)])
>> 타입은 <class 'dict_items'>

## 타입을 리스트로 변경할 수 있다.
menu_list = list(a.keys())
print(menu_list, type(menu_list))
>> ['김밥', '라면', '아메리카노', '구운 계란', '빵', '카페라떼'] <class 'list'>
```

<<<<<<< HEAD
### .get(key)
key 에 해당하는 value 를 가져온다.
```python
a = {
    "이름" : "고길동",
    "나이" : "30",
    "성별" : "남자",
    "출생" : "1993-06-29",
    "가족" : [
        {
            "이름" : "둘리",
            "종" : "공룡",
            "출생" : "??"
        },
        {
            "이름" : "또치",
            "종" : "타조",
            "출생" : "??"
        }
    ]
}

print(a.get("이름"))
>> 고길동

###가져온 value 값을 슬라이싱할 수도 있다.
print(a.get("출생)[5:])
>> 06-29

### key 가 없으면 "None"을 반환한다.
print(a.get("키"))
>> None

### None 대신 반환할 값을 추가할 수도 있다.
print(a.get("키", "키 정보가 없습니다."))
>> 키 정보가 없습니다.

### get() 메소드를 두번사용하여 값을 호출할 수도 있다.
print(a.get("가족")[1].get("종"))
>> 타조
=======
### dictionary comprehension
딕셔너리 안에 구조안에 제어, 조건문 등을 넣어 딕셔너리를 만드는 방법.

형태 : `[key: value for 변수 in 시퀀스 컨테이너]`
```python
a = {num : num**3 for num in range(5)}
print(a)
>> {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# key 값을 문자열로도 만들수 있다.
a = {f"{num}" : num**3 for num in range(5)}
print(a)
>> {'0': 0, '1': 1, '2': 8, '3': 27, '4': 64}

# 당연히 value 값도 가능.
a = {num : f"{num**3}" for num in range(5)}
print(a)
>> {0: '0', 1: '1', 2: '8', 3: '27', 4: '64'}

# if 절을 추가해 줄 수도 있다.
a = {num : num**3 for num in range(5) if num > 2}
print(a)
>> {3: 27, 4: 64}
>>>>>>> 9e1d539f3e7dd80feac1d371c695533206eefca6
```