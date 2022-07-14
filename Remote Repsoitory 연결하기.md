# Remote Repsoitory 연결하기

## Remote Repo 생성하기

1. 기본 브랜치 이름 master 로 변경하기
2. new Repo 생성버튼 눌러서 
   1. 이름 설정
   2. 만들기 !

####  Local

1. 새로운 디렉토리 생성
   1. mkdir {디렉토리 생성}
   2. cd {경로}
   3. git init
   4. git remote add origin {원격 레포지 주소 url}
   5. git remote : origin 이름으로 remote 추가된거 확인
   6. touch README.md
      1. 내용 수정(Optional)

2. 버전 남기기 (remote repository로 push 하기전에 반드시 commit 이 있어야한다. 3번 진행하기전에 git commit -m "~"이 진행 되어야한다는 뜻)
   1. git add {파일명.확장자}
      - git add .
   2.  git commit -m "first commit"
   3. git push origin master : 깃 헙 페이지에 업로드 (push 는 업로드의 개념)
      - git push -u origin master : -u 는 -u 이하의 즉 여기서는 origin master 를 기본값으로 설정한단뜻, 이거 한번이라도 적용하면 그이후에는 git push 까지만 쳐도 push됨
   4. push, clone, pull
      - push 는 업로드 : 다른 사람이 만들 Repo를 자신의 로컬로 가져올려고
        - mkdir {다운받은 레포지 넣을 폴더생성}
        - cd {폴더}
        - git clone {레포지 주소}
      - clone 은 다운로드
      - pull 은 업데이트 : 항상 push 전에는 pull 을 한다. 왜? 다른사람이 먼저 뭔가를 수정했을 수도 있으니깐. 안그럼 버전 충돌 일어난다  pull push
        - 만약 버전충돌이 일어났다면 두개의 버전중에 하나를 선택하던지 둘다 적용해서 하던지 해서 적용시켜야함. pull push를 기억하자.

