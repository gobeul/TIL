# HTML

### Hyoer Text Markdown Language

- Hyper Text ??<br> 
  하이퍼링크(참조)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- Markup Language ??<br>
  태그 등을 문서나 데이터 구조를 명시하는 언어 -> 글의 가독성을 높일 수 있다.

---
### HTML ??
웹페이지를 작성(구조화)하기 위한 언어

HTML 스타일 가이드<br>
들여쓰기를 할 때 2칸 띄운다.(2 space) <br>
파이썬은 4칸이다.

---
### HTML 기본 구조

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

HTML : 문서의 최상위 요소<br>
head : 문서의 메타데이터 요소 (문서 제목, 인코딩, 스타일, 외부 파일 로딩 등 일반적으로 브라우저에 나타나지 않는 내용)<br>
body : 문서 본문 요소 (실제 화면 구성과 관련된 내용) 

#### 요소(element)<br>
HTML의 요소는 태그 + 내용 으로 구성되어 있다.<br>
` <h1>~내용~</h1> `<br>
<u>닫는 태그가 없는</u> 태그들도 있으며 이경우에는 <u>내용도 없다.</u><br>
요소는 중첩(들여쓰기)될 수 있다. 열고 닫는 태그쌍을 잘 확인해야 하며 잘못됐다 하더라도 오류를 반환하지 않기 때문에 디버깅이 힘들다.

#### 속성(attribute)
` <a href="https://google.com"></a> `<br>
속성의 예시. `a`가 태그명, `href`가 속성명, `구글주소`가 속성 값이 된다.<br>
태그별로 사용할 수 있는 값이 다르다.<br>
속성작성시에 `=`뒤에 공백은 주지 않고 속성값은 `쌍따옴표`로 감싼다.

속성을 통해 태그의 부가적인 정보 설정이 가능하다.<br>
요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재한다.<br>
모든 태그에 사용할 수 있는 속성도 있는데 이를 `HTML Global Attribute`라고 한다.


#### 시맨틱 태그
HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것을 말한다.<br>
예를들어 `<h1>` 태그는 "이 페이지에서 최상위 제목" 인 텍스트를 감싸는 역할(혹은 의미)을 나타낸다.<br>
또한 `<footer>` 는 문서 전체나 섹션의 마지막 부분을 의미한다.

이와 반대인 `Nom semantic` 요소도 있으며 예시로는 `<div>`(블럭요소) , `<span>`(라인요소) 등이 있다.

시맨틱 태그 사용의 의의<br>
요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게한다.<br>
검색 엔진 최적화(SEO) ???


#### 렌더링(Rendering)
웹 사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정이다.


#### DOM(Document Object Model) 트리
텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조.<br>

HTML 문서에 대한 모델을 구성하고,<br>
HTML 문서 내의 각 요소에 접근하여 수정에 필요한 프로퍼티와 메서드를 제공한다.

---
### HTML 문서 구조화
HTML 요소는 크게 인라인 과 블록 요소로 나눌 수 있다.

#### 인라인 요소
글자처럼 취급하는 요소로 글자에 필요한 공간만 사용한다.<br>
```HTML
<a></a> : href 속성을 활용하여 다른 URL로 연결하는 하이퍼 링크를 생성한다.

<b></b>
<strong></strong> : 굵은 글씨를 표현해준다. 

<i></i>
<em></em> : 기울임 글씨를 표현해 준다.

<br> : 텍스트 내에 줄 바꿈을 생성한다.

<img> : scr 속성을 활용하여 이미지를 표현한다.

<span></span> : 의미 없는 인라인 컨테이너(논시매틱)
```


#### 블록 요소
인라인 요소와는 다르게 글자의 개수에 관계없이 한줄을 모두 사용한다.

```HTML
<p></p> : 하나의 문단 Paragraph

<hr> : 문단 레벨 요소에서 주제의 분리를 의미하며 수평선으로 표현된다

<ol></ol> : 순서가 있는 리스트
<ul></ul> : 순서가 없는 리스트

<pre></pre> : HTML에 작성한 내용을 그대로 표현. (문장이 길어도 한줄이면 가로로 길게 나타낸다.)공백문자를 유지한다.

<blockquote>
</blockquote> : 들여쓰기로 표현된다.

<div></div> : 의미 없는 블록 컨테이너 (논시매틱)
```

#### form
`<form>`은 정보(데이터)를 서버에 제출하기 위해서 사용하는 태그이다.

#### `<form>` 기본 속성
action : 제출할 데이터가 도착할 곳, 데이터를 받는곳의 URL, 공란일 경우 받는곳은 자신이 된다?

method : 데이터를 제출할 때 사용할 HTTP 메서드로 보통 GET 방싱 or POST 방식이 주로 사용된다.

enctype : 메서드가 POST 방식인 경우 데이터의 유형


#### `<input>` 와 속성
웹페이지 창에 사용자가 데이터를 입력할 수 있는 공간을 만들어 준다.

type : 문자에대한 입력(text) 뿐만아니라 체크박스등도 활성화 할 수 있다.

name : `<form>` 로 입력한 데이터를 제출시에 name 으로 할당된 변수에 그 데이터가 저장된다.

value : ` type="text" `로 문자를 입력할 창을 생성했을때 기본적으로 그 창에 들어갈 문자를 넣을 수 있다. 당연하게도 사용자는 그 문자를 지우고 다시 문자를 넣을 수 있다.<br>
혹은 문자입력이 아닌 ` type= checkbox ` 등에서 사용자가 선택할 경우 value 값을 name 변수에 저장하여 제출한다.

autofocus : 웹페이를 열었을때 사용자가 데이터 입력창을 마우스 클릭을 안해도 이미 마우스 클릭이 되어 있어 바로 문자등을 입력할 수 있는 상태오 만들어 준다.

#### `<label?`
label 을 클릭하여 input에 초점을 맞추거나 활성화 시킨다.<br>
`<input>`의 id 속성을 `<label>`에서는 for 속성을 서로 일치시켜 연결한다.<br>
```HTML
<label for="id-info">아이디를 입력하세요.</label>
<input type="text" name="userid" id="id-info">
```

#### input - type
`<input type="ooo">`<br>
`text` : 일반 텍스트 입력한다. <br>
`password` : 입력시 값을 특수기호(*)로 숨겨준다.<br>
`email` : 이메일 형식이 아니라면 form 이 불가능하다. <br>
`number` : min, max, step 속성을 이용하여 숫자범위 설정 가능하다.<br>
`file` : accept 속성을 활용하여 파일 탑입을 지정한다.<br>
`checkbox` : 체크박스를 생성한다. 동일한 항목의 여러 선택지인 경우에는 네임변수를 같게, value 값을 다르게 지정해야 한다. (중복체크 활용)<br>
`radio` : 동그란 체크박스를 생성한다. (중복체크가 아닌 단일 선택일 경우 사용한다.)<br>
`color picker, date picker ... ` : 여러 종류의 선택창을 보여준다.<br>
`hidden`: 사용자 입력은 필요없지만 보내야할 데이터가 있을때 이를 사용자에게 보이지 않도록 숨겨준다.<br>

그 외 다양한 유형에 대해서는 [MDN](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input) 참고

