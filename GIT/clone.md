### clone
"다운로드"의 개념<br>
다른 사람의 remote Repo 의 업로드 되어 있는 파일들을 내 local Repo 에  저장할 수 있다.

### clone 하고 push 까지
1. clone 할 위치로 이동한다. (저장할 dir)
2. git clone URL
    1. git init 할 필요가 없다. 자동으로 .git/ 이 생성된다. 이때 저 url 로 remote 도 같이 되는 거 같음.
3. 수정 후 저장한다.
4. add, commit, push 를 진행한다.
    1. 역시 git remote add origin URL 할 필요는 없는 거 같음, 2번 고정에서 자동으로 되는듯.

### clone 과 pull
clone 이 다운로드라면 pull 은 업데이트에 가깝다.<br>
초기에 clone 을 통해 remote Repo 와 같은 파일을 받았다면 그 이후부터는 변경사항이 있다면 pull 을 이용해 업데이트 하면 된다.