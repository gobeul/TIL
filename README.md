# TIL

>#### Today I Learn

---
### 기본 룰

> 1. 공부한게 없다면 커밋하지 않는다. 정직하게 하자.



---

### 알고리즘
- [유클리드 호제법_ 초대공약수(GCD)와 최소공배수(LCM)](https://github.com/gobeul/TIL/tree/master/algorithm/euclidean_algorithm.md)
- [deque 자료구조](https://github.com/gobeul/TIL/tree/master/algorithm/deque.md)
- [sort()](https://github.com/gobeul/TIL/tree/master/algorithm/sort.md)


---

### Markdown

- 마크다운을 쓰는 이유는?
  개발자로서 프로그램을 구현하다 보면 문서작업을 할 경우가 많이 있는데 이를 위해 문서의 구조와 내용을 쉽고 빠르게 나타내기 위함.<br>
  **개발의 코드를 문서답게**
  
- README.md<br>
  md는 마크다운의 준말
  
  - md 명령어
    - **#** : 제목표시, 1개부터 6개까지 사용가능
    
    - 리스트
  
      - **1., 2., ... **: 순서가 있는 리스트
      - **- or * **: 순서가 없는 리스트
        - tab 키를 써서 하위 리스트 생성 가능
    
    - 코드블럭
      **\```{사용언어}```**
    
      ```python
      print("Hello world!!")
      # python 코드블럭 사용 예시 
      ```
    
      ` 을 양쪽에 한개씩 붙여서 
    
       문장안에 코드블럭 `print("Hello")` 을 넣는 것도 가능.
    
    - 링크 넣기
      
      **\[string(문자)](url 주소)**
    
      예시)  \[네이버](https://www.naver.com) => [네이버](https://www.naver.com)
      
    - 이미지 넣기<br>
      **\[스트링(없어도됨)](이미지 경로)**
      
    - 텍스트 관련<br>
      볼드체 : \*\*문자열** or \__문자열__ =  **문자열**<br>
      이텔릭 : \*문자열\* or \_문자열\_ = *문자열*<br>
      취소선 : \~~문자열~~ = ~~문자열~~<br>
      다 한꺼번에 적용 가능 : *__~~문자열~~__*
      
    - 수평선<br>
      --- or --- or ***
      
    - 수직선 : >
    

---

### GIT
Git 이란? 분산 + 버전관리 + 시스템<br>
> git hub 는 git 을 이용한 클라우드 서비스이다.

- [clone](https://github.com/gobeul/TIL/tree/master/GIT/clone.md)
- [commit 하기](https://github.com/gobeul/TIL/tree/master/GIT/commit.md)
- [git bash 명령어](https://github.com/gobeul/TIL/tree/master/GIT/git_bash_cmd.md)
- [push](https://github.com/gobeul/TIL/tree/master/GIT/push.md)
- [Remote Repsoitory 연결하기](https://github.com/gobeul/TIL/tree/master/GIT/conect_remote_Repo.md)
- [Repository 만들기](https://github.com/gobeul/TIL/tree/master/GIT/creat_Repo.md)
  - push, clone, pull
    - push : 업로드의 개념
    - clone : 다운로드의 개념
      다른 사람이 만든 Repo를 자신의 Local로 가져올려고<br>
      git colne {다운받을 Repo 주소 url}
    - pull : 업데이트의 개념<br>
      git pull origin mater<br>
      항상 push 전에는 항상 push 전에는 pull 을 한다.<br>
      왜? 다른사람이 먼저 뭔가를 수정해서 커밋했을 수도 있으니깐 버전충돌 방지<br>
      pull push 풀푸시 기억하자.<br>
      <br>


- [branch](https://github.com/gobeul/TIL/tree/master/GIT/branch.md)
- [gitignore](https://github.com/gobeul/TIL/tree/master/GIT/gitignore.md)

질문 사이트
https://syllaverse.com/courses/11

  ---
  ### PYTHON
  - [기초](https://github.com/gobeul/TIL/tree/master/Python/basics.md)
  - 메서드
    - [문자열(string)](https://github.com/gobeul/TIL/tree/master/Python/method_string.md)
    - [list](https://github.com/gobeul/TIL/tree/master/Python/method_list.md)
    - [set](https://github.com/gobeul/TIL/tree/master/Python/method_set.md)
    - [tuple](https://github.com/gobeul/TIL/tree/master/Python/method_tuple.md)
    - [dictionary](https://github.com/gobeul/TIL/tree/master/Python/method_dictionary.md)
  - [범위(Scope)](https://github.com/gobeul/TIL/tree/master/Python/Scope.md)
  - [변수](https://github.com/gobeul/TIL/tree/master/Python/variable.md)
  - [얕은 복사 / 깊은 복사](https://github.com/gobeul/TIL/tree/master/Python/python_copy.md)
  - [자료형 분류](https://github.com/gobeul/TIL/tree/master/Python/datatype_classification.md)
  - 지능형 리스트
  - [컨테이너](https://github.com/gobeul/TIL/tree/master/Python/container.md)
    - [리스트](https://github.com/gobeul/TIL/tree/master/Python/container_list.md)
    - [튜플](https://github.com/gobeul/TIL/tree/master/Python/container_tuple.md)
    - [레인지](https://github.com/gobeul/TIL/tree/master/Python/container_range.md)
    - [세트](https://github.com/gobeul/TIL/tree/master/Python/container_set.md)
    - [딕셔너리](https://github.com/gobeul/TIL/tree/master/Python/container_dictionary.md)
  - [함수](https://github.com/gobeul/TIL/tree/master/Python/function.md)
    - [packing 과 unpacking](https://github.com/gobeul/TIL/tree/master/Python/function_packing.md)
    - [map](https://github.com/gobeul/TIL/tree/master/Python/function_map.md)
    - [filter](https://github.com/gobeul/TIL/tree/master/Python/function_filter.md)
    - [zip](https://github.com/gobeul/TIL/tree/master/Python/function_zip.md)
    - [lambda](https://github.com/gobeul/TIL/tree/master/Python/function_lambda.md)
  - [형변환](https://github.com/gobeul/TIL/tree/master/Python/typecasting.md)
  - [requests 모듈 사용하기](https://github.com/gobeul/TIL/tree/master/Python/module_requests.md)
  - [json 으로 자료 읽어오기](https://github.com/gobeul/TIL/tree/master/Python/module_json.md)
  - [OOP 객체지향프로그래밍](https://github.com/gobeul/TIL/tree/master/Python/python_oop.md)
    - 클래스 메서드와 스태틱 메서드의 차이..!
    - [문법](https://github.com/gobeul/TIL/tree/master/Python/python_oop_grammar.md)
    - [OOP의 핵심 개념 - 추상화, 상속, 다형성, 캡슐화](https://github.com/gobeul/TIL/tree/master/Python/python_oop_core.md)
  
<br>

---
### WEB
- [웹 사이트](https://github.com/gobeul/TIL/tree/master/WEB/web_site.md)
웹사이트란 브라우저를 통해서 접속하는 웹 페이지(문서)들의 모음을 말하며 "링크"를 통해서 여러 웹 페이지를 연결한것을 뜻한다.
- [HTML](https://github.com/gobeul/TIL/tree/master/WEB/HTML.md)
Hyoer Text Markdown Language

p 태그, span 태그 차이가 뭐지
p = 패러그래프 = 본문 ( 한줄 다씀. = 블록요소)
span = 인라인에 대표적 (한줄 다 안씀 = 인라인)
a 태그도 인라인 링크 옆에 글이 쭉 가는 경우가 많잖아

h7 태그는 없기때문에 쓰면 그냥 효과 없이 처리됨.(에러는 안남.)

div 의미없는 블록 컨테이너.

input 태그에 오토포커스 이거 뭐냐 = 자동으로 인풋하는 곳에 커서가 들어가지게 하는것

디져블드 : 인풋값 못바뀌게 함.

get 방식과 post 방식의 차이

id 선택자는 유일하다?
id="한개"
class="한개 두개 세개 ..."


id선택자는 js 에서 많이 써서 css에서는 안쓰는게 좋다고함



name 변수의 역할은 나중에 장고가서 쓸건데 form 에서 데이터를 주면 그게 네임변수에 저장되기 때문에 값을 불러오거나 할때 네임변수를 써야함.


p:nth-child(n) : id 안에 n번째 태그가 p태그면 적용합니다.

p:nth-of-type(n) : id 안에 p태그만 세어서 n번째 태그에 적용합니다. 
