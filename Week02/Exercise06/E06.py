x, y, C = input().split()

n = int(x)
m = int(y)

table = []

for row in range(n):
    rows = input()
    table.append(rows)

adjCount = 0
otherColour = {}

dx4 = [+1, -1, 0, 0]
dy4 = [0, 0, +1, -1]

def inside(x, y):
    # if x < 0 or x >= n:
    #     return False
    # if y < 0 or y >= m:
    #     return False
    # return True
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False

for i in range(n):
    for j in range(m):
        if table[i][j] != C and table[i][j] != '.' and not (table[i][j] in otherColour):
            for k in range(4):
                x = i + dx4[k]
                y = j + dy4[k]
                if inside(x, y) and table[x][y] == C:
                    otherColour[table[i][j]] = True
                    adjCount += 1
                    break

print(adjCount)