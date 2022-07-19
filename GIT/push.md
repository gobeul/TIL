### push
"업로드"의 개념. local Repo 에서 수정한 내용들을 remote Repo 에 반영하기 위해 업로드한다.

### push 과정
push 전에는 항상 commit 이 선행되어야 한다.

commit 후 => git push oring master (혹은 git push -u origin master로 설정했다면 => git push)

push 하기 전에는 항상 pull을 먼저 해두자.<br>
다른사람이 먼저 뭔가를 수정해서 커밋했을 수도 있어, 버전충돌 방지기 위함이다.<br>
...<br>
commit -m "~" -> git pull (origin master) -> git push (origin master)

git pull (origin master) -> commit -m "~" -> git push (origin master)

순서가 어느게 맞는 건지...