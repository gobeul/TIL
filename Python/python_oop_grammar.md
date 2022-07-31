# OOP 문법

### 기초
<br>
클래스 만들기, 클래스명의 첫들자는 대문자로!(권장)<br>
클래스는 공통된 속성(attribute)과 조작법(mrthod)을 가진 객체들의 분류이다.

```python
class Person:
  pass
```
<br>
인스턴스 생성 : 특정 클래스의 실제 데이터 예시(instance), 모든 객체는 특정 클래스의 인스턴스다.

```python
minsu = Person() # Person 이라는 특정 클래스의 인스턴스(객체) minsu 생성!!
```
<br>
`isinstance` : `minsu` 가 `Person` 이라는 클래스의 인스턴스인지 확인해보자.

```python
print(isinstance(minsu, Person))
>> True
```
<br>
`type` : 생성된 객체의 클래스를 확인할 수 있다.

```python
print(type(minsu))
>> <class '__main__.Person'>
```
<br>
인스턴스 변수 : == 인스턴스의 속성 / 각 인스턴스의 개별적인 데이터 / 생성자 메서드에서 `self.변수명`으로 정의할 수 있음.(이거 말고 직접 정의할 수 도 있음.) / 인스턴스 생성후 `인스턴스.변수명` 으로 접근 및 할당 가능

```python
minsu.name = "민수" # name이라는 인스턴스 변수(속성)에 "민수" 를 할당해줌.
print(minsu.name)
>> 민수
```
<br>
메서드 : 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위(behavior)들<br>
인스턴스 메서드는 인스턴스가 사용할 메서드이다.<br>
클래스 내부에서 정의되는 메서드는 기본적으로 인스턴스 메서드이다.(데코레이션으로 변경 가능)<br>
메서드 선언시, 첫번째 인자로 인스턴스 자기 자신에 해당하는 `self` 가 전달된다.<br>
메서드 호출시 `self` 에 해당하는 인자는 따로 적지 않는다.

```python
class Person:
    def talk(self): ## 첫번째 인자 명이 self 필요는 없지만 개발자들 사이에서 암묵적인 약속같은 것이다.
        return "안녕!"
    def hi(adafgsg): ## 인스턴스 메서드의 첫 인자는 self로 쓰자는 약속
        return "Hi"
    def eat(self, a): # 메서드도 함수이다 여러개의 인자를 추가할 수 있다.
        return f"{a} 냠냠"
    def test(slef)
        return self


minsu = Person()

print(minsu.talk()) # self의 인자는 자기자신으로 따로 적지 않는다.
>> 안녕!
print(minsu.hi())
>> Hi
print(minsu.eat("바나나")) 
>> 바나나 냠냠

print(minsu)
<__main__.Person object at 0x000001238E4EBE50>
print(minsu.test())
<__main__.Person object at 0x000001238E4EBE50> # 두개가 같다. 즉 메서드의 첫번째 인자 self는 객체(minsu) 그 자신이다.
```
<br>
생성자 메서드 : 인스턴스가 생성될 때 자동으로 호출되는 함수이다. 함수명은 `__ init __`을 사용한다.<br>
자동으로 호출 되기 때문에 `self` 말고 다른 인자가 있다면 인스턴스 생성시에 인자를 할당해준다.<br>
생성자 메서드를 사용하면 인스턴스 생성시에 속성을 정의해 줄수도 있다.

```python
class Person:

    def __init__(self):
        print("두두등장!")

p1 = Person() # __init__ 를 호출하지 않았지만 인스턴스 생성시에 자동으로 호출되었다.
>> 두두등장!

#################################################################################
class Person:

    def __init__(self, name): 
        print(f"{name} 두두등장!")

p1 = Person("김민수") # 생성자 메서드의 name 변수를 할당해 준다.
>> 김민수 두두등장!

#################################################################################
class Person:

    def __init__(self, name):  # my_name 이라는 속성을 정의 해주었다.
        self.my_name = name 

p1 = Person("김민수")
print(p1.my_name)
>> 김민수
```
<br>
소멸자 메서드 : 생성자 메서드와 다르게 인스턴스가 소멸되기 직전에 자동으로 호출되는 메서드이다.<br>
함수은 `__ del __` 을 사용한다.

```python
class Person:

    def __del__(slef):
        print("사라진다~~")

p1 = Person()

del p1 # 인스턴스를 제거할때 del 을 사용한다.
>> 사라진다~~
print(p1)
>> NameError: name 'p1' is not defined

```
<br>
인스턴스 속성(= 인스턴스 변수?)<br>
일반적으로 생성자 메서드 안에서 정의한다.(객체 생성과 동시에 속성값을 할당해 줄 수 있기 때문)<br>
물론 클래스 밖에서 정의할 수도 있고, 기존의 속성을 바꿔줄 수도 있다.

```python
class Person:

    def __init__(self, a, b):
        self.name = a
        self.age = b
    
    def talk(self):
        print(f"안녕 난 {self.name}이고 {self.age}살 이야!")\

    def talk2(self):
        print(f"난 {self.job} 이야")

p1 = Person("김민수", 20)

p1.talk()
>> 안녕 난 김민수이고 20살 이야!
## 여기시 talk2() 를 호출하면 job이라는 속성이 아직 할당 되지 않았기 때문에 오류가 난다.

p1.name = "김철수"
p1.job = "대학생"
p1.talk()
>> 안녕 난 김철수이고 20살 이야!
p1.talk2()
>> 난 대학생 이야
```
<br>
매직(스페셜) 메서드 : 생성자 메서드나 소멸자 메서드처럼 함수명에 더블언더스코어( __ )가 있는 메서드 들을 매직(스페셜) 메서드 라고 한다.

```python
__str__(self),
__len__(self),
__repr__(self),
__lt__(self, other),
__le__(self, other),
__eq__(self, other),
__ne__(self, other),
__gt__(self, other),
__ge__(self, other),
```
<br>
__ str __ : 특정 객체를 출력할때 (print 할때) 보여줄 내용을 정의할 수 있다.

```python
class Person:

    def __str__(slef):
        return "객체를 출력(print) 했다!!"

p1 = Person()

print(p1)
>> 객체를 출력(print) 했다!!
```
<br>
__ gt __ : >, < 를 사용할 때 자동으로 호출된다. self 말고 인자가 하나 더 필요하며 그 인자는 부등호를 기준으로 오른쪽 객체가 들어간다.(self는 왼쪽 객체) 당연히 그 안에서 속성을 정의할 수도 있다.

```python
class Person:

    def __init__(self, a, b):
        self.name = a
        self.age = b

    def __gt__(self, a):
        return a

p1 = Person('철수', 10)
p2 = Person('민수', 20)

print(p1 > 129) ## 등호기준 오른쪽의 객체 129가 a로 들어간다.
>> 129
print(p1 < p2) ## 등호기준 오른쪽의 객체 p2가 a로 들어간다.
>> <__main__.Person object at 0x00000208B04FBFD0>

##################################################################################
class Person:

    def __init__(self, a, b):
        self.name = a
        self.age = b

    def __gt__(self, a): # 부등호가 사용되면 gogo라는 인스턴스 속성을 정의하고 할당해준다.
        self.gogo = a
        return self.gogo

p1 = Person('철수', 10)
p2 = Person('민수', 20)

# 여기서 print(p1.gogo) 를 하면 오류 -> gogo 라는 속정이 p1 객체에 할당되지 않았다
p1 > 500 
print(p1.gogo) # 부등호를 사용하면서 부등호 오른쪽의 객체가 p1의 gogo라는 속성에 할당되었다.
>> 500
```
<br>
__ eq __ : __ gt __ 와 같다. 단, == 를 사용시에 호출된다.

```python
def __eq__(self, other) # 역시 self 외의 인자가 하나 더 필요
```
<br>
클래스 속성 (== 클래스 변수) : 특정 클래스의 인스턴스들이 공통적으로 가지는 속성이다.<br>
생성자 메서드와 속성이 겹치게 되면 생성자 메서드에서 정의한 속성으로 할당된다.<br>

```python
class Soldier:
    gender = "남자"

p1 = Soldier()
p2 = Soldier()

print(p1.gender)
>> 남자
print(p2.gender)
>> 남자
##################################################################################
class Soldier:
    gender = "남자"
    def __init__(self, gender):
        self.gender = gender
    gender = "남자"

p1 = Soldier("여자")

print(p1.gender)
>> 여자
```
<br>
클래스 메서드<br>
`@classmethod` 를 사용하여 정의한다.<br>
클래스가 사용할 메서드를 정의하며, 첫번째 인자로 클래스(cls)가 전달된다.<br>
인스턴스 메서드안에서는 클래스속성의 정의및 할당이 가능하다. 하지만 클래스 메서드 안에서 인스턴스 속성의 정의 및 할당은 불가능하다.

```python
class Person:
    
    @classmethod
    def sleep(cls): # cls 명칭은 self 처럼 암묵적인 룰인거고 바꿔도 이상은 없다.
        return "쿨쿨"

p1 = Person()
print(p1.sleep())
>> 쿨쿨
print(Person.sleep()) # 클래스.클래스메서드 형식으로도 호출이 가능하다.
>> 쿨쿨
############################################################################

class Person:

    gender = "남자"

    @classmethod
    def sleep(cls, power):  ## 클래스 메서드 안에서 클래스 속성을 불러올 수 있다.
        cls.power = power   ## 클래스 속성을 재정의할 수 도 있으며
        return f"{cls.gender} 쿨쿨 {Person.power} {cls.power}" 
        ## cls.속성, 클래스명.속성으로도 호출이 가능하다.
    
    def aaa(self): ## 인스턴스 메서드에서 클래스속성의 할당 및 재정의 가 가능하다.
    Person.power = 100
    Person.gender = "여자"
    Person.blood = "red"


p1 = Person()

print(p1.sleep(100)) # 인스턴스로 클래스 메서드 호출이 가능하다. 근데 가능하지만 하지 않는다.
>> 남자 쿨쿨 100 100

print(Person.sleep(500))
>> 남자 쿨쿨 500 500

print(p1.power)
>> 500

print(Person.power)
>> 500

p1.aaa()
print(p1.gender, p1.power, p1.blood)
>> 여자 100 red
```
<br>
스태틱 메서드(정적 메서드)<br>
클래스가 사용할 메서드이다.<br>
인스턴스 및 클래스의 속성과 무관하다. (근데, 인스턴스 속성은 건들수 없지만 클래스 속성은 가능하다.)<br>
`@staticmethod` 데코레이터를 사용하여 정의한다.<br>
호출시에 self, cls 같은 인자를 전달하지 않는다.<br>
보통 속성을 다루지 않고 기능(행동)만을 하는 메서드를 정의할 때 사용한다.

```python
class Person:

    gender = "남자"

    @staticmethod
    def st():
        Person.gender = "여자"
        print("스테틱 메서드")

p1 = Person()

print(p1.gender)
>> 남자
Person.st() ## p1.st() 로도 호출할 수 있다. 가능하지만 일부러 하지 않는다.
>> 스테틱 메서드
print(p1.gender)
>> 여자
```
<br>
인스턴스와 클래의 이름공간(namespace)<br>
인스턴스와 클래스의 속성이 같은 경우 인스턴스 객체를 사용하여 그 속성에 접근한다면 인스턴스의 속성을 따른다.

```python
class Person:

    gender = "남자" ## 클래스에서 gender 라는 클래스 속성을 정의

    def __init__(self): ## 인스턴스에서 gender이라는 인스턴스 속성을 정의
        self.gender = "여자"

p1 = Person()
print(p1.gender) ## 인스턴스 객체를 사용하여 인스턴스 속성에 접근한 경우
>> 여자
print(Person.gender)
>>남자
```
<br>
인스턴스는 3가지 메서드(인스턴스, 클래스, 스태틱)에 모두 접근할 수 있다.<br>
하지만 인스턴스로는 클래스와 스태틱 메서드를 호출하지 않는다.<br>
인스턴스가 할 행동은 인스턴스 메서드로 한정하여 설계한다.<br>
<br>

클래스메서드는 3가지 메서드(인스턴스, 클래스, 스태틱)에 모두 접근할 수 있다.<br>
(단, 인스턴스 메서드에 접근할 경우 self 인자에 인스턴스 객체를 넣어줘야함)<br>
하지만 클래스는 인스턴스 메서드를 호출하지 않는다.<br>
- 클래스 자체(cls)와 클래스 속성에 접근할 필요가 있다면 클래스 메서드를 사용합니다.
- 클래스 및 인스턴스 속성에 접근할 필요가 없다면 스태틱 메서드를 사용합니다.
