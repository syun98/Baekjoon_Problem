import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
camdir = [0, 4, 2, 4, 4, 1] # 카메라 종류별 분별 가능한 방향 수


def watch(idx, dir, office):
    if cam[idx][2] == 1:
        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir], y + dy[dir]

    elif cam[idx][2] == 2:
        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir], y + dy[dir]

        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir + 2], y + dy[dir + 2]

    elif cam[idx][2] == 3:
        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir - 1], y + dy[dir - 1]

        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir], y + dy[dir]

    elif cam[idx][2] == 4:
        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir - 2], y + dy[dir - 2]

        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir - 1], y + dy[dir - 1]

        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir], y + dy[dir]

    elif cam[idx][2] == 5:
        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir], y + dy[dir]

        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir + 1], y + dy[dir + 1]

        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir + 2], y + dy[dir + 2]

        x, y = cam[idx][0], cam[idx][1]
        while 0 <= x < n and 0 <= y < m and office[x][y] != 6:
            if office[x][y] == 0:
                office[x][y] = 7
            x, y = x + dx[dir + 3], y + dy[dir + 3]


def solve(cnt, off):
    global result

    if cnt == len(cam):
        temp = 0
        for i in range(n):
            temp += off[i].count(0)
        result = min(result, temp)
        return

    for i in range(camdir[cam[cnt][2]]):
        t_off = [item[:] for item in off]
        watch(cnt, i, t_off)
        solve(cnt + 1, t_off)


n, m = map(int, sys.stdin.readline().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = n * m

cam = []    # 카메라 위치 저장
for i in range(n):
    for j in range(m):
        if 0 < office[i][j] < 6:
            cam.append([i, j, office[i][j]])

solve(0, office)
print(result)
