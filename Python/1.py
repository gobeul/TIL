def sum_1(n):
    return n+1

def bridge(n, m):
    a = m-n
    if a == 0:
        return 1
    elif a == 1:
        return n + 1
    total = [0]*31
    total_b = [0]*31
    total_b[a] = 1
    cnt = 0
    while cnt != n:
        for i in range(1, 31):
            if total_b[i] != 0:
                for j in range(total_b[i]):
                    z = list(map(sum_1, total[:i]))
                    total[:i] = z[::]
                total[i] = total_b[i]
        total_b = total.copy()
        
        cnt += 1
    
    return sum(total)

t = int(input())
for t in range(t):
    n, m = map(int, input().split())
    print(bridge(n,m))


