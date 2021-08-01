import sys
# from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
ice = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    i1, i2 = map(int, input().split())
    ice[i1 - 1][i2 - 1] = True
    ice[i2 - 1][i1 - 1] = True

result = 0

# case) combinations
# for i in combinations(range(n), 3):
#     if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
#         continue
#     result += 1

# case) in operator
# for i in range(n - 2):
#     for j in range(i + 1, n - 1):
#         for k in range(j + 1, n):
#             if j not in ice[i] and k not in ice[i] and k not in ice[j]:
#                 result += 1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1

print(result)
