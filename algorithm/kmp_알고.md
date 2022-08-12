# KMP 알고리즘 (개념정도만 이해하자)
문자열의 중복되는 부분이 있다면 그만큼 연산을 줄이자는 취지.

패턴의 몇번째 인덱스에서 일치가 되지 않았는지에 따라서 되돌아가는 인덱스가 달라짐. ( 매칭에 실패했을 때 돌아갈 곳을 계산한다.)

패턴에 중복되는 부분이 없다면 브루트 포스하고 같다???

### 구현
```python

# 중계 리스트 구현하기...!
# T : target / P : pattern

def pre_precess(P): # 사전에 중복되는 부분 구하기.
    lps = [0] *len(P)
    j = 0

    for i in range(1, len(P)):

        if P[i] == P[j]:
            lps[i] = j +1
            j += 1

        else:
            j = 0
            if P[i] == P[j] :
                lps[i] = j+1
                j += 1
    return lps

P = "abcdabcf"
print(pre_precess(P))
>> [0, 0, 0, 0, 1, 2, 3, 0]

# KMP 알고리즘 구현하기
T = "abcdabeeababcdabcef"
P = "eaba"
def KMP(T, P):
    lps = pre_precess(P)

    position = -1 # 실패했다고 가정

    # i = target을 순회하는 인덱스
    # j = pattern 을 순회하는 인덱스

    i = 0
    j = 0

    while i< len(T):
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            #값이 다른데 j != 0일때 i 자리는 유지한테로 j만 이동해서 비교 시작
            if j != 0:
                j = lps[j-1]

            else: # 값은 다른디 j = 0 일때 => i 를 한칸 이동후 다시 진행.
                i += 1

        if j == len(P):
            position = i - j
            break
    return position
    
position = KMP(T, P)

print(position)
>> 7
```