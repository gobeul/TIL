# TIL

>#### Today I Learn

---
### 기본 룰

> 1. 공부한게 없다면 커밋하지 않는다. 정직하게 하자.



---

### 알고리즘
- [deque 자료구조](https://github.com/gobeul/TIL/tree/master/algorithm/deque.md)


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
  - [범위(Scope)](https://github.com/gobeul/TIL/tree/master/Python/Scope.md)
  - [변수](https://github.com/gobeul/TIL/tree/master/Python/variable.md)
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

