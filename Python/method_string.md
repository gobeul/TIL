# 문자열
변경 불가능하고(immutable) 순서가 있으며(ordered) 순회가능한(iterable)  자료형.<br>
변경이 불가능하기에 관련 메서드들은 비파괴메서드 이다.<br>
순서가 있기에 인덱스로 접근 가능하다.<br>

---

# 관련 메서드

### .find(x)
x 의 첫번째 위치를 반환한다 없다면  -1 을 반환한다.
```python
a = "apple"
print(a.find("a"))
>> 0  # "a"는 "apple" 의 0번째 인덱스에 있다.

print(a.find("z"))
>> -1  #"z"는 "apple" 문자열에 없다.
```
---
### .index(x)
find() 와 거의 같다. 단, x가 없다면 error가 나온다.
```python
a = "apple"
print(a.index("z"))
>> ValueError
```
---
### .startswith(x) // .endswith(x)
문자열이 x로 (시작하면 // 끝나면) True 를 반환하고 아니라면 False를 반환한다.
```python
a = 'hello python!'
print(a.startswith("hello"))
>> True
print(a.endswith("helllo"))
>> False
```
---
### .isupper() // .islower()
문자열이 (대문자 // 소문자)로만 이루어져 있다면 True, 아니라면 False 를 반환한다.
```python
a = "APple"
print(a.isupper())
>> False
print(a.islower())
>> False
print(a.swapcase())
>> apPLE
```
---
### .upper() // .lower() // .swapcase()
문자열을 (대문자 // 소문자 // 대문자 <-> 소문자)로 바꾸어 반환한다
```python
a = "APple"
print(a.upper())
>> APPLE
print(a.lower())
>> apple
```
---
### replace(old, new[, count])
문자열의 old를 new로 (count 번)바꾸어 반환한다.
```python
a = "apple"

print(a.replace("p", "o"))
>> aoole  # count 를 따로 지정해주지 않았다면 바꿀 수 없을 때까지 바꾸어 준다.
print(a.replace("p", "o", 1))
>> aople
print(a.replace("ppl", "good"))
>> agoode
```
---
### .strip([char]) // .lstrip([char]) // .rstrip([char])
문자열 (양끝 // 왼쪽 // 오른쪽)에서 [char] 을 찾아 제거한다.<br>
단, char 의 길이가 2이상일 경우 이를 1씩 쪼개서 하나하나 찾아가며 제거해서 반환한다.
```python
a = "apple"
print(a.strip("a"))
>> pple
print(a.strip("p"))
>> apple  # "p" 양끝에 없으므로 제거 하는 문자가 없다.
print(a.strip("ape"))
>> l
## "ape"를  하나씩 쪼갠다. -> "a", "p", "e"
apple 양 끝에 a 가 있으면 제거한다. -> pple
pple 양 끝에 a 가 있으면 제거한다. -> 없다면 p로 넘어가서 찾는다.. -> 반복
```
---
### .split(sep= None, maxsplit= -1)
문자열을 특정한 단위(sep=)로 (maxsplit 횟수만큼)나누어 리스트로 반환한다.
```python
a = "q,w,e,r,y,u,i,o,a,s,d,f,g,h,j,l"
print(a.split(","))
>> ['q', 'w', 'e', 'r', 'y', 'u', 'i', 'o', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'l']
## maxsplit= 에 값을 지정해 주지 않는다면 (-1) 쪼갤 수 없을때 까지 쪼갠다.

print(a.split())
>> ['q,w,e,r,y,u,i,o,a,s,d,f,g,h,j,l'] ## sep= 를 지정하지 않는다면 공백을 기준으로 쪼갠다.

print(a.split(",", 3))
>> ['q', 'w', 'e', 'r,y,u,i,o,a,s,d,f,g,h,j,l']
```
---
### 'separator'.join(iterable)
iterable 의 문자열들을 separator(구분자)로 이어 붙인(join()) 문자열을 반환한다.
```python
a = ["안", "녕", "!"]
print("".join(a))
>> 안녕!
print("_".join(a))
>> 안_녕_!
```
---
### .capitalize()
앞글자를 대문자로 만들어 반환합니다.
```python
a = "apple, banana, orange"
print(a.capitalize())
>> Apple, banana, orange
```
---
### .title()
어포스트로피(')나 공백 이후를 대문자로 만들어 반환합니다.
```python
a = "apple, banana, orange"
print(a.title())
>> Apple, Banana, Orange    
```

