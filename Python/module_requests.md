### requests 웹서버에서 데이터 값을 받아올때 사용됨
---
### 기초

설치 : (터미널) pip install requests

```python
import requests

url = "데이터 받을 주소"
response = requests.get(url).json()
```
requests.get()으로 주소를 받고<br>
json()으로 데이터를 vscode에서 볼 수 있도록 가공해준다.

---
### 실습
### 로또번호 데이터 값 요청하기

```python
import requests

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021"
response = requests.get(url).json()
print(response)

>> 출력값 
{'totSellamnt': 101960162000, 'returnValue': 'success', 'drwNoDate': '2022-06-25', 'firstWinamnt': 2108962250, 'drwtNo6': 45, 'drwtNo4': 24, 'firstPrzwnerCo': 12, 'drwtNo5': 29, 'bnusNo': 16, 'firstAccumamnt': 25307547000, 'drwNo': 1021, 'drwtNo2': 15, 'drwtNo3': 17, 'drwtNo1': 12}

```

- 값이 딕셔너리형태로 주어진다. => 딕셔너리의 여러 메소드들을 적용할 수 있음.



