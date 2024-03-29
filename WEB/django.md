# 장고

파이썬 기반의 웹 프레임워크<br>
`서버`를 구현하는 웹프레임워크이다.

#### 프레임워크
서비스 개발에 필요한 기능을 미리 구현해서 모아 놓은 것<br>
특정 프로그램을 개발하기 위한 여러 도구들과 규약을 제공하는 것

소프트웨어의 생산성과 품질을 높일 수 있다.

### 디자인 패턴
소프트웨어의 관점에서 디자인패턴이란<br>
각각의 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 때 공통적인 설계 문제가 있고 이를 해결하는 방법에서도 공통점이 존재한다.

이러한 유사점을 패턴이라고 한다.

즉, 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시한다.<br>
성능 및 협업, 유지보수등에서 중요하게 작용한다.


### MVC 패턴
자바에 적용된 디자인 패턴<br>
Model : 데이터와 관련된 로직을 관리<br>
View : 레이아웃과 화면을 처리<br>
Controller : 명령을 model과 view부분을 연결

MVC 디자인패턴의 목적은 관심사의 분리<br>
개발 효율성 및 유지보수가 쉬워진다.<br>
다수의 멤버로 개발하기 용이 == 협업에 좋다.


### MTV 패턴
장고에 적용된 디자인 패턴<br>
MVC에 디자인패턴을 조금 변형한 형태 

#### Model : Model - 데이터 관련
MVC 패턴에서 Model 역할에 해당한다.<br>
데이터 관련된 로직을 관리한다.<br>
응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리한다.<br>

데이터를 구조화하고 조작하기 위한 모델(추상적인 계층)을 제공한다.

모델을 통해 데이터에 접근하고 조작함

사용하는 데이터들의 필수적인 필드(열)들과 동작(메서드)을 포함

모델 클래스 1개를 만들게 되고 이는 데이터베이스 테이블 1개를 의미함<br>
모델 != 데이터베이스

#### Template : View - 화면 관련
MVC 패턴에서 View 역할에 해당한다.<br>
레이아웃과 화면을 처리한다.<br>

#### View : Controller - 중간 처리 및 응답 반환
MVC 패턴에서 Controller 역할에 해당한다.<br>
모델 및 템플릿과 괸련된 로직을 처리해서 응답을 반환한다.<br>
클라이언트의 요청에 개해 처리를 분기하는 역할

데이터가 필요하면 model에 접근해서 데이터를 가져오고<br>
가져온 데이터를 tamplate으로 보내 화면을 구성하여<br>
클라이언트에게 반환한다.

### Django Template, DTL
(뷰를 배우면 안쓰긴 해)

데이터 표현을 제어하는 도구이자, 표현에 관련된 로직


### Migration
데이터베이스에 모델에 변경사항을 반영하는 방법

필수명령어 : makemigrations, migrate

설계도 생성 : `python -m makemigrations`<br>
우리가 만들 조금은 부족한 내용을 완전하게 만들어줌(반영은 x)

모델의 변경사항을 데이터베이스에 동기화(반영)<br>
: `python manage.py migrate`


### ORM objct-relational-mapping
DB 는 파이썬 언어를 알지 못하는데 이를 중간에서 번역하는 역할이 필요하다 그게 ORM

sql등의 데이터베이스 언어를 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체

장점 : sql을 몰라도 객체지향 언어로 db조작 가능-> 높은 생산성

단점 : 훗날 db가 엄청 커졌을때는 orm만으로 세밀한 db조작을 구현하기에는 어려움

### CRUD
creat / read / update / delete

기본적인 데이터처리기능 4가지를 묶어서 일컫는 말

CUD 는 POST 방식
R 은 GET방식

#### CRUD - Crete

#### CRUD - Read

#### CRUD - Update
수정은 조회가 우선시되어야함

#### CRUD - Delete
