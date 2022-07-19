### 딕셔너리 (비시퀀스 - 가변형)
key-value 쌍으로 이루어진 자료형 (버전 3.7부터는 시퀀스형, 이전 버전은 비 시퀀스형)<br>
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


### 관련 메소드
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

print(a.values()) # .valuse()
>> dict_values([3000, 4000, 3000, 1000, 1000, 3500])

print(a.items()) #.items()
>> dict_items([('김밥', 3000), ('라면', 4000), ('아메리카노', 3000), ('구운 계란', 1000), ('빵', 1000), ('카페라떼', 3500)])

## 리스트로 변경할 수 있다.
menu_list = list(a.keys())
print(menu_list, type(menu_list))
>> ['김밥', '라면', '아메리카노', '구운 계란', '빵', '카페라떼'] <class 'list'>
```