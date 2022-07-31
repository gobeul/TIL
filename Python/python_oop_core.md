# 추상화(Abstraction)



---
# 상속(Inheritance)
<br>
클래스에서 상속을 통해 부모 클래스의 모든 속성을 자식 클래스에 상속 시킬 수 있다. 이는 코드 재사용성을 높인다.

```python
class Person:
    population = 0
    
    def __init__(self, name='사람'):
        self.name = name
        Person.population += 1
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


class Student(Person):
    def __init__(self, student_id, name='학생'):
        self.name = name
        self.student_id = student_id  
        Person.population += 1


p1 = Person("철수")
p1.talk()
>> 반갑습니다. 철수입니다.
print(Person.population)
>> 1

p2 = Student(930629)
p2.talk()
>> 반갑습니다. 학생입니다.
print(Person.population)
>> 2
```
<br>
`issubclass(a_class, b_class)`<br>
a_class 와 b_class 의 상속 관계를 판별한다.<br>
a_class 가 b_class 의 자식 클래스면 True 를 반환한다.

```python
print(issubclass(Student, Person))
>> True

print(issubclass(Person, Student))
>> False
```
<br>
`super()`<br>
부모클래스의 내용을 사용하고자할 때 사용합니다.<br>
중복을 제거할 수 있다.<br>

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
      
    
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        ## 부모클래스의 생성자 메서드에서 name, age, number, email 인자 들을 사용하겠다는 뜻!
        self.student_id = student_id
```
---
# 다형성(Polymorphism)
동일한 메소드가 클래스에 따라서 다르게 동작할 수 있음을 나타낸다.<br>
즉, 서로 다른 객체들이 동일한 메서드에 대해 다른 결과를 내놓을 수 있다.<br>

### 메서드 오버라이딩
부모 클래스에서 상속받은 메서드를 자식클래스에서 재정의 하는 것

```python
class Person():

    def talk(self):
        print("안녕~")

class Soldier(Person):

    def talk(self):
        print("충성!")

p1 = Person()
p2 = Soldier()

p1.talk()
>> 안녕~
p2.talk()
>> 충성!
```
---
# 캡슐화(Encapsulation)
객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단하는 것을 뜻한다. (주민등록 번호 같은 정보)<br>
다른 언어와 달리 파이썬에서 캡슐화는 암묵적으로는 존재하지만, 언어적으로는 존재하지 않는다.

### Publie Member
언더바가 없이 시작하는 메서드나 속성들이 이에 해당한다.<br>
어디서나 호출 가능하다.<br>
하위 클래스에서 메서드 오버라이딩을 허용한다.<br>
<br>
<br>

### Protected Member
언더바 1개로 시작하는 메서드나 속성들이 이에 해당한다.<br>
암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능하다.<br>
하위 클래스에서 메서드 오버라이딩을 허용한다.<br>
<br>
<br>

### Private Member
언더바 2개로 시작하는 메서드나 속성들이 이에 해당한다.<br>
본 클래스 내부에서만 사용이 가능하다.<br>
하위 클래스 상속 및 호출이 불가능하다.<br>
외부 호출이 불가능하다<br>

```python
class Person:

    def __init__(self, age): ## __age 는 Private Member
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Person(20)

print(p1.get_age())
>> 20

print(p1.__age) ## 직접적인 접근은 불가능 하다.
>> AttributeError: 'Person' object has no attribute '__age'

```