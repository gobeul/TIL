# Django - authentication system

인증과 권한 부여를 함께 제동(처리) 하며 이를 인증시스템이라고 함.

인증 : 신원확인

권한 : 권한부여(인증된 사용자가 수행할 수 있는 작업을 결정)


## 초기 설정
두번째 앱 `account` 를 생성 및 등록<br>
앱이름이 꼭 account 여야 하는건 아니지만 이렇게 하면 후에 다른 수정사항들을 거칠 필요가 없다.(즉, 권장사항)


## 인증관련 bulit-in forms 익히기

## 로그인
로그인은 Session을 Create 하는 과정

`AuthenticationForm`<br>
로그인을 위한 빌트인 폼.

`login(request, 유저정보, back=None)`<br>
인증된 사용자를 로그인 시키는 로직으로 view 함수에서 사용되고 보통 import 해서 이름바꾸고 쓴다. login 함수는 우리가 또 렌더링 용으로 만드니깐..!

`get_user()`<br>
AuthenticationForm의 인스턴스 메서드<br>
유효성검사(.is_valid())를 통과한 경우 로그인한 사용자 객체를 반환

`base.html` 에서 내가 context 데이터를 주지 않았어고 {{user}} 변수로 로그인한 사용자 이름을 호출할 수 있음. 이는 settings.py context processors 설정값 덕분 (이는 모든 템플릿에서 호출가능함)<br>
이때문에 실제 context 를 작성할때 user 변수를 쓰지는 않음

## 로그아웃
Session을 Delete 하는 과정

`logout(request)`<br>
반환값이 없으며, 역시 모듈을 임포트해서 이름을 바꿔서 쓴다.<br>
사용자가 로그인하지 않은 경우, 별도의 오류를 발생시키진 않음.
1. 현재 요청에 대한 session data를 DB에서 삭제

2. 클라이언트 쿠키에서도 session id 를 삭제 <br>
이건 다른 사람이 동일한 웹 브라우저를 사용하여 로그인 했을때 이전사용자의 세션 데이터에 접근하는걸 방지하기 위함임.

## 회원가입
User 를 creat하는 것이며 `UserCreationForm` 빌트인 폼을 사용한다.

`UserCreationForm`<br>
주어진 username 과 password로 권한이 없는 새 user를 생성하는 ModelForm.<br>
3개의 필드를 가짐<br>
-> username, password1, password2

## Custom user 와 Built-in auth forms 의 관계
앞서 기본 User 모델을 Custom user 모델로 변경했다.

그런데 우리가 쓰는 auth forms 과 같은 빌트인 모델 들은 기본 User 을 기본으로 받고 있기때문에 오류가 발생한다.

어떻게 바꿔야할까?

-- 다시 커스텀 해야 되는 클래스 --

상속을 통해 커스텀 한다.

1. UserCreationForm (회원가입)
2. UserchangeForm (회원 정보 수정)

## get_user_model()
현재 프로젝트에서 활성화된 사용자 모델을 반환해준다.

직접 참조하지 않는 이유..<br>
이걸 사용하면 자동으로 커스텀 된 유저모델을 반환해주기에???<br>
-> 직접 참조해도 되는데.. 이부분은 추후에 다시 다룰 예정


## 회원 탈퇴
DB에서 유저를 Delete하는 것과 같다.

## 회원 정보 수정
User를 UPdate 하는 것이며 `UserChangeForm` 을 사용한다.<br>
(비밀번호 변경은 다른 모델폼을 쓴다.)

## 비밀번호 변경
`PasswordChangeForm` 을 사용한다.<br>
이건 `SetPasswordFrom` 을 상속받는 모델폼임.

`update_seesion_auth_hash()`<br>
비밀변호 변경시에 자동 로그아웃 되지 않도록, 새로운 비밀번호의 세션 데이터로 세션을 업데이크 해줌

## 로그인 사용자에 대한 접근 제한하기
1. The raw way
  - is_authenticated attribute <br>
  사용자가 인증되어 있는지 알 수 있는 방법<br>
  모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성이다.<br>
  AnonymousUser에 대해서는 항상 False <br>
  일반적으로 request.user 에 이속성을 사용한다 <br>
  -> requset.user.is_authenticated<br>
  *주의) 권한과는 관련이 없고, 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지도 확인하지 않음..!<br>
  단지 지금 사용자가 로그인 사용자인가 비로그인 사용자 인가.


2. The login_required decorator
  - 데코레이터 `@login_required`<br>
  인증된 사용자 아니라면 로크인 페이지로 이동시킨다.<br>
  궁금증
    1. 장고는 로그인페이지를 어떻게 알았지?(페이지 명시 안했는데)
      - 사실 모름 그냥 accounts/login/으로 보내는데 마침 우리가 그 주소를 로그인 페이지로 쓰고 있는 것 뿐임.(accounts 맞춰준 효과)
    2. 강제 이동된 주소에 /?next=/~~ 이건 뭐지?<br>
      - 직전에 요청한 주소임 만약 로그인처리가 되면 그 주소로 이동시켜주는 역할을 함-> 그런데 이렇게 할려면 폼태그에 action 속성을 비워놓고 `result = request.GET.get('next')`로 next(키값)의 value 값을 가져와야함. ( 이건 당연히 get으로 요청이 감. --> `@require_POST`하고 같이쓰면 로직에 오휴가 있음 한쪽을 포기하고 안에 if문을 활용하던가 해야됨!)