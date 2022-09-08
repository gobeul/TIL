# Custom User model

## 유저모델을 사용하지 않고 커스텀한 유저모델을 사용하는 이유
User model의 기본 인증 요구 사항이 적절하지 않을 수 있기 때문이다.

예를 들어 서비스 내 회원가입시 username 대신 email을 식별값으로 사용하는 경우도 많은데 장고의 기본 user model 은 username을 식별값으로 사용하기에 적합하지 않다.

그래서 `AUTH_USER_MODEL`이라는 변수값으로 새로운 설정값을 제공하여 기존에 것을 덮어씌울 것 이다. (재정의)

기존 User 모델값을 쓰더라고 커스텀으로 교체해야 할까??<br> 
그렇다. 장고의 강력한 권장사항임. 상속받아서 진행하기에 손해 볼게 없음.

## AUTH_USER_MODEL
프로젝트에서 User를 나타낼때 사용하는 모델이다.

기본값은 AUTH_USER_MODEL = 'auth.User' 이며 이는 auth라는 앱의 User 클래스를 나타냄.<br>
(auth는 인증시스템의 앱으로 플젝 시작시 자동으로 등록 되어 있음.)<br>
(AUTH_USER_MODEL은 sttings.py 에는 없는데 이는 sttings.py의 상위 인 global_settings.py 에 등록되어있음)

첫번째 마이그래이션이 된 후에는 변경할 수 없음..!<br>
(사실 할 수는 있는데 수정사항이 너무너무 복잡하고 어려워서 권장 절대 안 함)<br>
+ 데이터 베이스 파일을 초기화하는 방법도 있음 (이건 간단한데..?)<br>
실제 프로젝트에서는 데이터베이스를 초기화하면 안돼서 그런가?

### 데이터베이스 초기화
1. migrations 파일 삭제<br>
0001 0002 이런애들만

2. db.sqlite3 삭제

3. 다시 migrations 진행

## 커스텀 유저모델로 바꾸는 방법
공식문서에 순서대로 나와있음.
(모듈 임포트하는건 따로 안 적음)

1. `AbstractUesr` 클래스를 상속받을 User 클래스 만들기. (accounts 앱의 models.py 에 작성)<br>
  (상속 받기 떄문에 둘은 같은 모습을 지님.)

2. `AUTH_USER_MODEL` 값을 우리가 위에서 만든 값으로 설정해줌.<br>
-->> AUTH_USER_MODEL = 'accounts.User' (accounts는 앱 이름)


3. admin.py에 커스텀 User모델을 등록<br>
`admin.site.register(User, UserAdmin)`