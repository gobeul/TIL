# prim 알고리즘
MST 를 구하는 알고리즘의 방법중 하나로 하나의 정점에서 연결된 간성들 중에 하나씩 선택해가며 MST를 만들어 가는 방식

1. 임의 정점에서 출발
2. 현재 정점과 인점하는 정점들 둥의 최소 비용의 간선이 존재하는 정점을 선택
3. 모든 정점이 선택될때까지 1, 2 를 반복

서로소인 2개의 집합을 유지한다.
1. MST를 만들기 위해 선택된 정점들
2. 선택되지 않은 정점들

우선 순위 큐를 사용하지 않은 prime 알고리즘 같은 경우 시간복잡도가 O(N^2) 으로 느리다..!<br>

사실 MST 의 대표적 인 알고리즘은 prim 이 아니라 Kruskal 알고리즘인데<br>
이 친구는 시간복잡도가 O(ElogE) 로 준수한 편이다

### prim 코드 예시
```python

# 입력 예시
'''
5 6 # 노드 개수, 간선 개수
1 2 3 # 출발노드, 도착 노드, 가중치
1 3 7
2 3 1
3 4 4
2 5 2
5 4 2
'''

def prim(start, V):  # MST 가중치의 합을 리턴하는 함수. 1~V 번 노드인 경우
    key = [INF] * (V + 1)  # key[i] i가 MST에 연결되는 비용, 초기값 무한대
    key[1] = 0 # 임의로 선택한 1번 노드 (start == 1)
    MST = [0] * (V + 1) # 방문처리 (visited)
    pi = [0] * (V + 1) # pi의 idx번호(노드)에 연결된 정점은 pi[index] 이다 라는 뜻

    for _ in range(V):  # 모든 정점이 MST에 포함될 때 까지
        # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
        u = 0 # 최소인 노드번호(인덱스) 찾기
        minV = INF

        for i in range(1, V + 1):
            if MST[i] == 0: # 방문하지 않은 값이라면
                if key[i] < minV: # 최소값인지 확인후 저장
                    u = i
                    minV = key[i]
        MST[u] = 1  # u 번 노드를 방문처리

        for v in range(V + 1):  # u에 인접인 v에 대해
            if MST[v] == 0 and adj[u][v] != 0: # v 노드가 방문도 안했고, u 노드와 연결되어 있다면(인접행렬의 값이 0 이 아니라면)
                if key[v] > adj[u][v]:  # u를 이용해 기존보다 더 작은 비용으로 MST에 연결된다면
                    key[v] = adj[u][v] # 갱신
                    pi[v] = u  # v는 u와 연결해서 MST에 포힘될 예정

    return sum(key[start:])  # MST 가중치의 합 리턴


V, E = map(int, input().split())
INF = 10000
# 인접행렬
adj = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w  #  무방향 그래프에서 MST 구성

print(prim(1, V))  # 노드 시작 번호 1인 경우(코드 주석의 예시)
```