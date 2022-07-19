### Remote Repsoitory 연결하기

  1. Remote Repo 생성하기

     1. 기본 branch 이름 master 로 변경하기<br>
        깃허브 브랜치 디폴트가 master에서 main 으로 변경되었는데..
        이유는 흑인 인권운동 관련되어 있음.
        이걸 왜 굳이 master로 바꾸냐면 보통 회사들은 master로 사용하고 있기때문.

     2. new Repo 생성버튼 클릭 후 이름설정, 그리고 생성!

  2. Local Repo 생성하기
     mkdir {dir}  ->  cd {dir}  ->  git init  ->  git remote add origin {remote Repo URL}  ->  git remote (origin 이름으로 remote 추가된거 확인)  ->  touch README.md  -> 내용수정
  3. 깃허브에 버전 남기기 push
     1. git add {파일명.확장자}
     2. git commit -m "커밋 메세지"
     3. git push origin master : 깃 헙 페이지에 업로드 (push 는 업로드의 개념)
        - git push -u origin master : -u 는 -u 이하의, 즉 여기서는 origin master 를 기본값으로 설정한단뜻, 이거 한번이라도 적용하면 그이후에는 git push 까지만 쳐도 push됨<br>