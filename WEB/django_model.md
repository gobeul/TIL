# 장고 모델 사용하기

```python

# 1. models.Model 의 상속을 받는 클래스 정의
## 1-1 클래스의 이름은 보통 앱이름에서 's'빼고 쓰는??
class {클래스 이름}(models.Model) 
# 2. DB 필드 사용
    title = models.CharField(max_length=10) # DB 필드 사용 예시

```