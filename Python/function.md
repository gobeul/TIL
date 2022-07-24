# 함수

### 왜 사용할까?
분해(decomposition) 와 추상화(abstraction)
-  분해 : 기능을 분해하고 재사용하게 만든다.<br>
    ```python
    # 리스트의 길이를 구하는 방법
    num = [1, 2, 3]
    ## 1.
    cnt = 0
    for i in num:
        cnt += 1
    print(cnt)

    ## 2. 함수 이용
    print(len(num))

    ## 함수가 훨씬 편하다!
    ```
- 추상화<br>
스마트폰의 원리를 몰라도 우리가 잘 사용할 수 있는 것 처럼, 함수의 원리를 몰라도 잘 사용할 수 있다.<br>
ex) print()

### 함수의 종류
내장, 외장, 사용자 정의 함수
- 내장함수<br>
파이썬에 기본으로 내장되어 있는 함수 (ex. prit() , 하지만 import 로 들고 와야되는 것도 있다.)

- 외장함수<br>
다른 개발자들이 만들어 놓은 함수 (imtport 를 통해 외부 라이브러리에서 제공)

- 사용자 정의 함수<br>
내가 직접 만들어서 사용하는 함수

### 함수의 기본구조
- 선언(생성)과 호출(사용)<br>
선언은  def 키워드를 통해서<br>
호출은 `def 함수이름("parameter")` 를 통해서 *parameter 가 없는 경우도 있다.
- 입력<br>
parameter(재료) 와 argument(인자) 로 나뉜다.<br>
parameter 는 선언할때, argument 는 호출할 때 사용<br>
- 문서화
- 범위
- 결과 값<br>
void function : 리턴값이 없는 함수<br>
None 을 return 하고 함수 종료

    value returnning function <br>
    리턴문을 통해 값을 return 하고 함수 종료


### return

기본적으로 return 은 항상 하나의 값만 반횐한다.
하지만 tuple 이나 list 로 묶어서 두 개 이상의 값을 반환할 수 있다.
```python
def ii(a, b):
    return a+b, a-b

def oo(a,b):
    return [a+b, a-b]


print(ii(10, 5))
>> (15, 5)
print(oo(10, 5))
>> [15, 5]
```

print() 와 return의 차이점
```python
def void():
    print("good!")

void()
>> good!

print(void())
>> None # void()라는 함수는 return 문이 없어서 None을 리턴한 것이다.
```

### Aregument(인자)
함수 호출시 parameter 에 들어가는 값

argument는 크게 꼭 있어야하는 `필수 argument` 와 없어도 되는 `선택 argument` 로 나뉜다.

- positional argument

  기본적으로 함수 호출시에 argument는 위치에 따라 함수에
   전달된다.
  ```python
  def abc(a, b):
    return a*5 + b**2

  abc(1, 20)
  >> 순서대로 a에 1이, b에 20이 들어간다.
  ```

- keyword argument

  직접 변수의 이름을 특정 argument에 전달 가능하다.
  ```python
  def aa(x, y):
    return x*4 + y

  print(aa(y= 10, x= 3))
  >> 22 # 3*4 + 10
  ```
- 주의! keyword 다음에 positional 이 올 수 없다.<br>
  positional 다음에 keyword 는 가능.

  ```python
  print(aa(x =2, 10))
  >> error!!

  print(aa(10, y =2))
  >> 42
  ```

- default argument
  
  선언(생성)할 때 값을 넣어줘서 호출시에 argument 값을 주지 않도록 한다.
  ```python
  def aa(x, y= 5):
    return x*4 + y

  print(aa(10)) ## 호출시에 따로 y를 주지 않음. 근데 다른 값을 넣어도 됨
  >> 45
  ```

### 가변 인자 `*args`
```python
def vv(*args):
    return args

print(vv(1,2,3,4,5))
>> (1, 2, 3, 4, 5)
```

### 가변 키워드 인자 `**args`
가변 키워드 인자를 이용하여 딕셔너리 자료형을 인자로 사용할 수 있음.
```python
def vv(**args):
    return args

print(vv(a="하이", b="바이"))
>> {'a': '하이', 'b': '바이'}
## 이때 key값을 문자열로 지정하지 않는다 => 자동으로 문자열이 됨.
```

### 가변 인자 + 가변 키워드 인자
가변 인자와 가변 키원드 인자를 함께 쓸수도 있다.
```python
def vv(*a, **b):
    return a, b

print(vv(1, 2, 3, a="하이", b="바이"))
>> ((1, 2, 3), {'a': '하이', 'b': '바이'})
```

