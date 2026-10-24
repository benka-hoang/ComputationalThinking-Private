# Codeforces 3A - Shortest path of the king

# Part 1: Read & Extract position into (x, y)
# Horizontal: 'a'-'h' converted using ord()
# Vertical: '1'-'8' converted to int
start = input().strip()
target = input().strip()

x1, y1 = ord(start[0]), int(start[1])
x2, y2 = ord(target[0]), int(target[1])

# Part 2: Calculate deltax and deltay
dx = x2 - x1
dy = y2 - y1

# Determine horizontal (L/R) and vertical (U/D) directions
h_dir = 'R' if dx > 0 else 'L'
v_dir = 'U' if dy > 0 else 'D'

abs_dx = abs(dx)
abs_dy = abs(dy)

# Total number of moves is max(abs_dx, abs_dy)
total_moves = max(abs_dx, abs_dy)
diag_moves = min(abs_dx, abs_dy)
straight_moves = total_moves - diag_moves

# Output minimum number of moves
print(total_moves)

# Diagonal (cross) moves first: min(deltax, deltay)
for _ in range(diag_moves):
    print(h_dir + v_dir)

# Straight moves for the remainder: from min + 1 to max(deltax, deltay)
straight_dir = h_dir if abs_dx > abs_dy else v_dir
for _ in range(straight_moves):
    print(straight_dir)
