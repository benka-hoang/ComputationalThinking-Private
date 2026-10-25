# Codeforces 7B - Memory Manager

t, m = map(int, input().split())

mem = [0] * m
globalIndex = 0

def defragment():
    global mem
    non_zeros = [v for v in mem if v != 0]
    mem = non_zeros + [0] * (m - len(non_zeros))

def alloc(size):
    global globalIndex
    found_idx = -1
    # Look for the first contiguous block of `size` free bytes
    for i in range(m - size + 1):
        if all(mem[i + j] == 0 for j in range(size)):
            found_idx = i
            break

    if found_idx != -1:
        globalIndex += 1
        for j in range(size):
            mem[found_idx + j] = globalIndex
        print(globalIndex)
    else:
        print("NULL")

def erase(x):
    if x <= 0 or x not in mem:
        print("ILLEGAL_ERASE_ARGUMENT")
        return

    for i in range(m):
        if mem[i] == x:
            mem[i] = 0

for _ in range(t):
    parts = input().split()
    op = parts[0]
    if op == "defragment":
        defragment()
    elif op == "alloc":
        alloc(int(parts[1]))
    elif op == "erase":
        erase(int(parts[1]))
