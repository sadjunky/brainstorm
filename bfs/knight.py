

def neighbours(ax, ay):
    nb = []
    if ((ax - 2 > 0) and (ay + 1 < n)):
        nb.append((ax - 2, ay + 1))
    if ((ax - 2 > 0) and (ay - 1 > 0)):
        nb.append((ax - 2, ay - 1))
    if ((ax + 2 < m) and (ay + 1 < n)):
        nb.append((ax + 2, ay + 1))
    if ((ax + 2 < m) and (ay - 1 > 0)):
        nb.append((ax + 2, ay - 1))
    if ((ax + 1 < m) and (ay - 2 > 0)):
        nb.append((ax + 1, ay - 2))
    if ((ax + 1 < m) and (ay + 2 < n)):
        nb.append((ax + 1, ay + 2))
    if ((ax - 1 > 0) and (ay - 2 > 0)):
        nb.append((ax - 1, ay - 2))
    if ((ax - 1 > 0) and (ay + 2 < n)):
        nb.append((ax - 1, ay + 2))
    return nb


def explore(sx, sy, tx, ty):
    marker = [[0 for j in range(n)] for i in range(m)]
    marker[sx][sy] = 1

    queue = [(sx, sy)]
    while queue != []:
        (ax, ay) = queue.pop()
        for (nx, ny) in neighbours(ax, ay):
            if marker[nx][ny] == 0:
                marker[nx][ny] = 1
                queue.insert(0, (nx, ny))
    return marker[tx][ty]

n = 8
m = 8
print(explore(0, 0, 1, 1))
