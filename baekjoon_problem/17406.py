import copy
import sys
from itertools import permutations

input = sys.stdin.readline


# 배열에 회전 연산을 수행하는 함수
def rotate(p, arr):
    result = 5001
    for pp in p:    # 연산 순서가 저장된 리스트 p
        r, c, ss = pp[0] - 1, pp[1] - 1, pp[2]
        for s in range(1, ss + 1):                  # 안쪽부터 바깥쪽으로 회전
            e = arr[r - s][c - s]                   # 가장 왼쪽, 가장 위 값 저장
            for x in range(r - s, r + s):           # 왼쪽 라인 아래로 한 칸 이동
                arr[x][c - s] = arr[x + 1][c - s]
            for y in range(c - s, c + s):           # 아래쪽 라인 왼쪽으로 한 칸 이동
                arr[r + s][y] = arr[r + s][y + 1]
            for x in range(r + s, r - s, -1):       # 오른쪽 라인 위로 한 칸 이동
                arr[x][c + s] = arr[x - 1][c + s]
            for y in range(c + s, c - s + 1, -1):   # 위쪽 라인 오른쪽으로 한 칸 이동
                arr[r - s][y] = arr[r - s][y - 1]
            arr[r - s][c - s + 1] = e               # 저장해 둔 e값을 위치에 저장

    for i in range(len(arr)):
        rowsum = sum(arr[i])
        result = min(result, rowsum)
    return result


n, m, k = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))
turn = list(list(map(int, input().split())) for _ in range(k))
result = 5001

for p in permutations(turn, k):
    temp = rotate(p, copy.deepcopy(a))
    result = min(result, temp)

print(result)
