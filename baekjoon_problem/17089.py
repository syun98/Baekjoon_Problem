import sys

input = sys.stdin.readline

n, m = map(int, input().split())
frd = [[False for _ in range(n)] for _ in range(n)]     # 친구 여부
cnt = [0 for _ in range(n)]                             # 친구 수
for i in range(m):
    i1, i2 = map(int, input().split())
    frd[i1 - 1][i2 - 1] = True
    frd[i2 - 1][i1 - 1] = True
    cnt[i1 - 1] += 1
    cnt[i2 - 1] += 1
result = 12001

for i in range(n):
    for j in range(i + 1, n):
        if not frd[i][j]:                       # A와 B가 친구가 아닌 경우
            continue
        for k in range(j + 1, n):
            if not frd[i][k] or not frd[j][k]:  # A와 C 또는 B와 C가 친구가 아닌 경우
                continue
            result = min(result, cnt[i] + cnt[j] + cnt[k] - 6)

if result == 12001:
    print(-1)
else:
    print(result)
