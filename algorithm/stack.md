# 자료구조 - 스택
선형구조의 자료구조이다.<br>
선형구조란 물건을 쌓아 올리듯 자료를 쌓아올린 형태의 자료구조로 자료간의 관계가 1대 1의 관계를 갖는다.<br>
자료구조란 자료를 (선형으로) 저장할 저장소로 배열을 사용할 수 있다.

저장소 자체를 스택이라고 하기도 한다.

스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.

마지막에 삽입한 자료를 가장 먼저 꺼내며 이를 후입선출(LIFO last-in-first-out)이라 한다.<br>
스택에서 마지막에 삽입된 원소의 위치를 top이라고 부른다.(정식은 SP stack pointer)

---
### 스택 관련 연산(함수가 아니라 보통부르는 명칭)
삽입 - 저장소에 자료를 저장함 PUSH 

삭제 - 저장소에서 자료를 꺼낸다. POP

스택이 공백인지 아닌지 확인하는 연산 - isEmpty `비어있다면 True`

스택의 top에 있는 item(원소)을 반환(확인)하는 연산 - peek

```python
s = [] # stack

## PUSH
def push(item):
  s.append(item) # 참고로 append 메소드는 좀 느림

## 느린 append 를 대체하는 방법
def push(item, size):
  global top
  top += 1
  if top == size:
    print("overflow!") # 디버깅 용
  else:
    stack[top] = item

size = 10 # 사이즈 크기는 문제에 요구하는 대로 // 모르겠으면 100만개..?
stack = [0] * size # append 가 좀 느려서 처음부터 스택사이즈를 정해주는 방법
top = -1 # 초기 탑 위치 공백 스택 자리. 포인터 느낌

push(10, size)

## POP
def pop():
  if len(s) == 0: # underflow, 디버깅용
    return
  else:
    return s.pop(-1) # == s.pop()
## pop 도 느리다?? 그래서 size를 정해놓았을때..!
def pop():
  global top
  if top == -1 :
    print("underflow")
    return 0
  else:
    top -= 1 # 먼저 포인터 이동하고 
    return stack[top+1] # 그위에 값 반환, push 를 진행하면 덮어 씌워지는 지우는 동작은 안해도 됨.
    # 리턴 때문에 포이터 이동후 위에꺼 뺐는데...
    # 함수정의 안해서 할꺼면 빼고 나서 포인터 이동해도됨. 이게 더 직관적이긴함

print(pop())

if top > -1: # pop()
  top -= 1
  print(stack[top+1])
```
---
### 스택구현시 고려사항
1차원배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다.

이를해결하기 위해 동적으로 크기를 할당하는 방법이 있다.(연결리스트)<br>
구현이 복잡하지만 메모리를 효율적으로 사용할 수 있다.

---
### Function call 재귀?
가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입 선출 구조로 스택과 같다.

---
### 스택을 이용한 후위 표기법
- ISP == 스택안에서 우선 순위
- ICP == 대조 대상(보통 스택안의 요소?)과의 우선순위
- `"("` == 무조건 스택에 쌓는다. (여는 괄호)
- `")"` == 등장하면 `"("` 가 나올 때까지 pop

> 스택을 이용하는게 목적이기 때문에 eval() 없이 구현해보자.

```python
str1 = "2+3*4/5"
stack = []
result = ""
for char in "*/+-()":
    # 연산자
    if not stack: # 스택에 아무것도 없다면
        stack.append(char)

    elif char == "(" : # 최고 우선 순위
        stack.append(char)

    elif char in "*/":
        while stack ans stack[-1] in "*/":
            result += stack.pop()
        stack.append(char)

    elif char in "+-":
        while stack and stack[-1] != "(" :
            result += stack.pop()
        stack.append(char)

    elif char == ")" :
      while stack and stack[-1] != "(" :
        result += stack.pop()
      stack.pop()

    # 피 연산자
    else:
      result += char
while stack:
  result += stack.pop()

```


```python
def my_eval():
  """
  1. word : 연산할 계산식(후위표기법)
  2. stack : 결과
  return stack
  """
    for char in word:
        if char not in "*/+-":
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == "+":
                stack.append(y + x)
            elif char == "-":
                stack.append(y - x)
            elif char == "*":
                stack.append(y * x)
            elif char == "/":
                stack.append(y / x)
    return stack[-1]
```