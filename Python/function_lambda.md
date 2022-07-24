# lambda
` lambda {parmter} : 표현식 `
이름이 없는 함수로 익명함수라고도 불린다.<br>
return 문을 가질 수 없다.<br>
너무 간단한 함수이기에 일회용 함수를 쓰거나 할 때 사용한다.

```python
def plus(x, y):
    return x+y

lambda_puls = lambda x, y : x+y

print(plus(2, 3))
>> 5
print(lambda_puls(2, 3))
>> 5
```