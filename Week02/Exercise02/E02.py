# In Python, a map is called a dictionary (dict).
# Note: Avoid naming the variable `map` because `map` is a built-in Python function.

# 1. Initialize an empty dictionary
my_map = {}

# # 2. Assign string keys to integer values
# my_map["abc"] = 2
# my_map["def"] = 5

# # 3. Accessing values
# print(my_map["abc"])  # Output: 2

# # 4. Check if a key exists
# if "abc" in my_map:
#     print("Found key 'abc' with value:", my_map["abc"])

# # 5. Using .get() with a default value (useful for counting)
# # If key doesn't exist, returns 0 instead of throwing KeyError
# count = my_map.get("xyz", 0)
# print(count)  # Output: 0

n = int(input())

course = list()
for i in range(n):
    s, num = input().split()
    num = int(num)
    my_map[s] = my_map.get(s, 0) + num
    course.append((s, my_map[s]))

candidate = {}
max_point = 0
winner = ""
for name in my_map:
    max_point = max(max_point, my_map[name])
for name in my_map:
    if my_map[name] == max_point:
        candidate[name] = 1
for i in range(n):
    if course[i][0] in candidate and course[i][1] >= max_point:
        winner = course[i][0]
        break

print(winner)