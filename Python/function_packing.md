# packing 과 unpacking

### packing
여러개의 데이터를 묶어서 변수에 넣는 것
` num = (1,2,3,4,5) # 패킹 `

### unpacking
시퀀스속의 요소들을 여러개의 변수에 나누어 할당하는 것.
`a, b, c, d, e = num # 언패킹`<br>

언패킹시에 변수 개수와 할당하고자 하는 요소가 동일 해야함.<br>
하지만 Asterisk(*)를 사용하면 달라도 가능하다.
```python
a, b *rest = num  
## rest = [3, 4, 5]

a, *rest, b = num
## rest = [2, 3, 4]
```