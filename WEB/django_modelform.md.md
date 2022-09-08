# Django - ModelForm

form 클래스 작성시에 model 클래스와 중복되는 부분이 많음을 느낄 수 있었다.

ModelForm을 이용하여 이를 좀더 효율적으로 작성할 수 있다.

ModelForm은 Model 을 기반으로 Form을 작성한다.

### class Meta - 모델폼의 이너 클래스
model = 참조할 모델 클래스 (호출이 아님 () 이거 안 붙임)<br>
fields = 가져올 모델의 필드 ( `'__all__'` 로 모두 가져올 수 있음.)<br>
exclude = ('이름',) 형태로 제외할 모델 필드를 정할 수 있음. - 튜플의 형태이다.<br>

### 참조값을 사용하는 이유
함수를 당장 호출하지 않고 `필요한 시점`에서 호출을 원하는 경우<br>

### ModelForm 을 이용한 유효성 검사
`is_vaild()` 메서드 사용<br>
데이터가 유효여부를 boolean 으로 반환


### ModelForm 과 Form
ModelForm 이 Form 보다 꼭 좋다고 할 수는 없음-> 각각의 역할이 다른 것.

DB에 영향을 미치지 않고 단순히 데이터만 사용된다면 Form을 사용<br>
예시로 로그인등의 과정에서 데이터를 받아 인증과정에서 사용되는 경우, 이는 DB에 별도로 저장하지는 않기에 Form을 사용한다.

데이터를 받아 DB에 저장하는 등의 연관되어 있는 경우 ModelForm을 사용함