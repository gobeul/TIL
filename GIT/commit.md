### commit
커밋이란 특정 버전으로 남기는 것을 뜻한다.

  - 커밋은 3가지 영역을 바탕으로 동작한다.
    wd   ->   staging area   ->   Repo

  - staging area 은 왜 존재하는가? __ 잘 이해 안됨

    커밋이 파일자체가 아닌 특정버전으로 관리하고 싶은 wd의 수정사항을 저장하는건데.. 이게 없으면 wd내의 배포하고 싶지 않은 버전의 파일들은 따로 다른 dir에 보관해야됨. ,,,,,, 그냥 따로 보관하면 되지않나..?

### 커밋 과정

  - 파일을 만든다.   -  지금 상태는 untracked 상태 = 깃이 추적하지 않는/관리하지 않는 상태  -  git add 를 이용해 이 파일을 staging area 로 옮긴다( = staged 한다.)  -  파일의 상태가 tracked로 변함. = 깃이 추적하는/관리하는 상태  -  git commit 을 이용해 Repo에 commit 한다.

  1. git init
     깃을 통해 관리하고자 하는 dir를 로컬Repo로 만들기위해 맨처음 한번만 해주면 되는 부분.
     
     명령어를 사용하면 .git/ 라는 숨겨진 dir가 생성되는데 이는 깃으로 관리하는 Repo를 하나 만든것이며 굳이 건들 필요가 없으므로 숨겨진채로 생성된다.
     
  2. git config --global user.email "{이메일}"
     
     git config --global user.name "{유저이름}"
     
     깃을 권한을 주는 부분?? "--global"옵션은 전체 권한을 준다고 생각하면 된다.
     
     역시 처음 한번만 설정해주면 됨
     
  3. git add
     
     git add {파일이름.확장자} : 생성 or 수정한 파일을 커밋하기 위해 wd에서 staging dir로 옮긴다. 
     
     wd에 많은 파일을들 일일이 add하기엔 귀찮으므로 **git add .** 을 이용하면 wd내 수정되거나 추가된 전체 파일을 대상으로 할 수 있다. ( . 는 현재 dir을 뜻함) 
     
  4. git commit -m "메세지, 보통은 커밋하는 이유를 적는다."
     
     메세지 부분을 적지 않으면 커밋이 되지 않는것 같은데 잘은 모르겠다.

  - git status<br>
    현재 Local Repo 의 상태를 확인할 수 있다.<br>
    *습관처럼 입력해보는게 좋다.*

  - git log<br>
    커밋 기록을 보여줌
    
  - git log --oneline\n커밋기록 중 중요한(?) 부분만 보여줌