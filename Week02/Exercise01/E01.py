# Input 3 integers n, m, a
n, m, a = map(int, input().split())

# Calculate x for n
if n % a == 0:
    x = n // a
else:
    x = n // a + 1

# Calculate y for m
if m % a == 0:
    y = m // a
else:
    y = m // a + 1

ans = x * y

print(ans)