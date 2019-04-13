import numpy as np


def queensAttack(n, k, r_q, c_q, obstacles):
    a = np.zeros((n, n), dtype=int)
    r_q -= 1
    c_q -= 1
    a[r_q][c_q] = 1
# add obstacles as 2 val
# add selected as 3 val
    loopcnt = 0
    for x, y in obstacles:
        a[x-1, y-1] = 2
        loopcnt += 1
    # to left of queen
    for i in range(c_q, -1, -1):
        loopcnt += 1
        if a[r_q, i] == 2:
            break
        if a[r_q, i] == 1:
            continue

        a[r_q, i] = 3

    # to right of queen
    for i in range(c_q, n):
        loopcnt += 1
        if a[r_q, i] == 2:
            break
        if a[r_q, i] == 1:
            continue
        a[r_q, i] = 3

    # to up of queen
    for i in range(r_q, -1, -1):
        loopcnt += 1
        if a[i, c_q] == 2:
            break
        if a[i, c_q] == 1:
            continue
        a[i, c_q] = 3

    # to downn of queen
    for i in range(r_q, n):
        loopcnt += 1
        if a[i, c_q] == 2:
            break
        if a[i, c_q] == 1:
            continue
        a[i, c_q] = 3

    # to top left of queen
    i, j = r_q, c_q
    while True:
        loopcnt += 1
        i -= 1
        j -= 1
        if i < 0 or j < 0:
            break
        if a[i, j] == 2:
            break
        if a[i, j] == 1:
            continue
        a[i, j] = 3

    # to top right of queen
    i, j = r_q, c_q
    while True:
        loopcnt += 1
        i -= 1
        j += 1
        if i < 0 or j >= n:
            break
        if a[i, j] == 2:
            break
        if a[i, j] == 1:
            continue
        a[i, j] = 3
    # to bottom left of queen
    i, j = r_q, c_q
    while True:
        loopcnt += 1
        i += 1
        j -= 1
        if i >= n or j < 0:
            break
        if a[i, j] == 2:
            break
        if a[i, j] == 1:
            continue
        a[i, j] = 3

    # to bottom right of queen
    i, j = r_q, c_q
    while True:
        loopcnt += 1
        i += 1
        j += 1
        if i >= n or j >= n:
            break
        if a[i, j] == 2:
            break
        if a[i, j] == 1:
            continue
        a[i, j] = 3
    unique, counts = np.unique(a, return_counts=True)
    d = dict(zip(unique, counts))
    print("loop="+str(loopcnt))
    return d[3]


# print(queensAttack(4, 0, 4, 4, []))
print(queensAttack(100000 , 0, 4187, 5068, []))
obstacles = []
s = """5 5
4 2
2 3""".splitlines()
for _ in range(3):
    obstacles.append(list(map(int, s[_].rstrip().split())))

print(queensAttack(5, 3, 4, 3, obstacles))
