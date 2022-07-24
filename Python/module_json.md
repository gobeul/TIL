# json

```python
import json  ## 먼저 json 모듈 불러오기

## open() 메소드를 이용하여 movie.json 파일을 'utf-8'로 인코딩해서 열어서 "movie_info_file" 라는 변수에 저장
### 인코딩 관련 부분은 아직 잘 모름. 
#### open() 사용 시 경로에 주의할 점이 있다.
movie_info_file = open("movie.json", encoding='utf-8')

## json.load() 메소드를 이용하여 open 한 파일을 가공하여 "movie_info" 라는 변수에 저장.
movie_info = json.load(movie_info_file)
```