# TIL

>#### Today I Learn

---
### 기본 룰

> 1. 공부한게 없다면 커밋하지 않는다. 정직하게 하자.



---

### 알고리즘

---

### Markdown

- 마크다운을 쓰는 이유는?
  개발자로서 프로그램을 구현하다 보면 문서작업을 할 경우가 많이 있는데 이를 위해 문서의 구조와 내용을 쉽고 빠르게 나타내기 위함.
  **개발의 코드를 문서답게**
- README.md
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
      print("Hellow world!!")
      # python 코드블럭 사용 예시 
      ```
    
      ` 을 양쪽에 한개씩 붙여서 
    
       문장안에 코드블럭 `print("Hellow")` 을 넣는 것도 가능.
    
    - 링크 넣기
      **\[string(문자)](url 주소)**
      예시)  \[네이버](https://www.naver.com) => [네이버](https://www.naver.com)
    
    - 이미지 넣기
      **\[스트링(없어도됨)](이미지 경로)**
    
    - 텍스트 관련
      볼드체 : \*\*문자열** or \__문자열__ =  **문자열**
      이텔릭 : \*문자열\* or \_문자열\_ = *문자열*
      취소선 : \~~문자열~~ = ~~문자열~~
      다 한꺼번에 적용 가능 : *__~~문자열~~__*
    
    - 수평선
      --- or --- or ***
    
    - 수직선 : >
    

---

### GIT

- 분산 + 버전관리 + 시스템

- git bash 명령어 (리눅스로 구현된 프로그램으로 리눅스 명령어가 사용된다.)
  - **cd {디렉토리}** : 현재 디렉토리에서 {디렉토리}로  이동한다.
  - **ls** : 현재 디렉토리내에 있는 디렉토리와 파일 리스트를 보여준다.
  - **touch {파일이름.확장자}** : 현재 디렉토리에 파일을 생성한다.
  - **mkdir {디렉토리 이름}** : 현재 디렉토리에 하위 디렉토리를 생성한다.
  - **code .** : 현재 디렉토리의 vscode를 실행시켜준다.
  - 기타
    - **~** : 홈 디렉토리를 나타냄, cd ~ = 홈디렉토리로 이동한다.
    - **../** : 상위 디렉토리를 뜻함, cd ../ = 상위 디렉토리로 이동한다.
    - **현재 디렉토리**는 **작업디렉토리**라고도 하며 **wd**로도 나타냄.
    - **절대 경로와 상대경로** : 절대 경로는 모든 경로가 다 기입된 것이고 상대 경로는 wd를 기준으로 특정디렉토리의 상대적경로를 기입한 것.
      예를 들어 wd가 C:/Users 이고 특정 디렉토리의 경로가 C:\Users\gbj\Desktop\dev 라면, 상대경로는 gbj\Desktop\dev 가 된다.
- Repository 만들기
  - Repository (이하 Repo)는 Local Repo 와 Remote Repo로 나뉜다.
    로컬은 우리가 사용하고 있는 컴퓨터를 생각하면 되고
    원격은 대표적으로 깃헙을 생각하면 된다.
    깃을 통해 로컬 Repo을 만들어야 한다.


- commit 하기

  - 커밋이란 특정 버전으로 남기는 것을 뜻한다.

  - 커밋은 3가지 영역을 바탕으로 동작한다.
    wd   ->   staging dir   ->   Repo

  - staging dir 은 왜 존재하는가? __ 잘 이해 안됨

    커밋이 파일자체가 아닌 특정버전으로 관리하고 싶은 wd의 수정사항을 저장하는건데.. 이게 없으면 wd내의 배포하고 싶지 않은 버전의 파일들은 따로 다른 dir에 보관해야됨. ,,,,,, 그냥 따로 보관하면 되지않나..?

  커밋과정

  - 파일을 만든다.   -  지금 상태는 untracked 상태 = 깃이 추적하지 않는/관리하지 않는 상태  -  git add 를 이용해 이 파일을 staging dir 로 옮긴다( = staged 한다.)  -  파일의 상태가 tracked로 변함. = 깃이 추적하는/관리하는 상태  -  git commit 을 이용해 Repo에 commit 한다.

  1. git init
     깃을 통해 관리하고자 하는 dir를 로컬Repo로 만들기위해 맨처음 한번만 해주면 되는 부분.
     명령어를 사용하면 .git/ 라는 숨겨진 dir가 생성되는데 이는 깃으로 관리하는 Repo를 하나 만든것이며 굳이 건들 필요가 없으므로 숨겨진채로 생성된다.

  2. git config --global user.email "{이메일}"
     git config --global user.name "{유저이름}"
     깃을 권한을 주는 부분?? "--global"옵션은 전체 권한을 준다고 생각하면 된다.
     역시 처음 한번만 설정해주면 됨
  3. git add
     git add {파일이름.확장자} : 생성 or 수정한 파일을 커밋하기 위해 wd에서 staging dir로 옮긴다. wd에 많은 파일을들 일일이 add하기엔 귀찮으므로 **git add .** 을 이용하면 wd내 수정되거나 추가된 전체 파일을 대상으로 할 수 있다. ( . 는 현제 dir을 뜻함) 
  4. git commit -m "메세지, 보통은 커밋하는 이유를 적는다."
     메세지 부분을 적지 않으면 커밋이 되지 않는것 같은데 잘은 모르겠다.

  - git status
    dir의 상태를 보여줌.
  - git log
    커밋 기록을 보여줌
  - git log --oneline
    커밋기록 중 중요한(?) 부분만 보여줌

- Remote Repsoitory 연결하기

  1. Remote Repo 생성하기

     1. 기본 branch 이름 master 로 변경하기
        깃허브 브랜치 디폴트가 master에서 main 으로 변경되었는데..
        이유는 흑인 인권운동 관련되어 있음.
        이걸 왜 굳이 master로 바꾸냐면 보통 회사들은 master로 사용하고 있기때문.

     1. new Repo 생성버튼 클릭 후 이름설정, 그리고 생성!

  2. Local Repo 생성하기
     mkdir {dir}  ->  cd {dir}  ->  git init  ->  git remote add origin {remote Repo URL}  ->  git remot (origin 이름으로 remote 추가된거 확인)  ->  touch README.md  -> 내용수정
  3. 깃허브에 버전 남기기 push
     1. git add {파일명.확장자}
     2. git commit -m "커밋 메세지"
     3. git push origin master : 깃 헙 페이지에 업로드 (push 는 업로드의 개념)
        - git push -u origin master : -u 는 -u 이하의, 즉 여기서는 origin master 를 기본값으로 설정한단뜻, 이거 한번이라도 적용하면 그이후에는 git push 까지만 쳐도 push됨

  - push, clone, pull
    - push : 업로드의 개념
    - clone : 다운로드의 개념
      다른 사람이 만든 Repo를 자신의 Local로 가져올려고
      git colne {다운받을 Repo 주소 url}
    - pull : 업데이트의 개념
      항상 push 전에는 항상 push 전에는 pull 을 한다.
      왜? 다른사람이 먼저 뭔가를 수정해서 커밋했을 수도 있으니깐 버전충돌 방지
      pull push 풀푸시 기억하자.
