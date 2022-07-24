# 범위 Scope
잘 이해가 안 될수도 있지만 계속 이해하려고 노력해야함.

함수는 코드 내부에서 local Scope 를 생성하고 그 외의 공간에서는 global Scope 로 구분한다.
- global Scope : 코드 어디에서든 참조할 수 있는 공간.
- local Scope : 함수가 만든 Scope로, 함수 내부에서만 참조가능.
- 글로벌 변수
- 로컬 변수

### 변수의 수명주기
변수는 각자의 수명 주기가 존재한다.
- bulit-in Scope : 파이썬이 실행된 이후부터 영원히 유지.
- global Scope : 모듈이 호출된 시점 이후부터, 혹은 인터프리터가 끝날때까지 유지(우리가 프로그램 작성하는 페이지?)
- local Scope : 함수가 호출될때 생성, 그리고 함수가 종료될때 까지 유지

### 이름 규칙
파이썬에서 사용되는 식별자(이름)들은 이름공간에 저장되어 있다.

LEGB Rule 에 따른 순서대로 이름을 찾아 나아간다.
- Local Scpoe : 지역범위(현재 작업중인 범위)
- Enclose Scope : 지역범위 한단계 위 범위
- Global Scope : 최상단에 위치한 범위
- Built-in Scope : 모든것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것, ex) print() )

```python
def legb(a):
    print = len

    return print(a)

print(legb([1,2,3,4,5]))
>> 5
```
print 라는 변수명을 함수내에서, 즉 로컬 스코프에서 len 로 정해주었다.<br>
그래서 print(a) 를 반환시에 print 라는 변수명을 로컬 스코프에서 찾기 떄문에 len(a) 와 같게 되는것.<br>
len 라는 이름은 L-E-G-B 순으로 찾고 L-E-G 에서 len을 정의해준게 없기 때문에 Built-in 에서 정의된 len 가 호출되는것.<br>
Global Scope의 print 도 마찬가지
