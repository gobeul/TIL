# 버블 정렬 _ Bubble sort

인접한 두개의 원소를 비교하며 자리를 계속 교환하는 방식으로 

시간복잡도는 O(n^2) 이다.

### 과정
1. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하며 맨 마지막까지 이동한다.
2. 1번 단계가 끝나면 가장 큰 원소가 마지막에 위치하게 된다.
3. 이를 반복한다.

### 구현
```python
def bubble(arr, n): # n은 리스트의 길이

    for i in range(n-1):
        
        for j in range(n-1-i): # 단계마다 비교할 개수가 1개씩 줄어든다.

            if arr[j] > arr[j+1]: # 왼쪽이 더 크면 자리 교환!
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
```