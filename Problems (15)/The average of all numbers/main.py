# put your python code here
a = int(input())
b = int(input())

ns = [x for x in range(a, b + 1) if not x % 3]

print(sum(ns) / len(ns))
