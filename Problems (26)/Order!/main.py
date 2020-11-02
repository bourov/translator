list_num = [int(input()) for _ in range(3)]

print(all(i < j for i, j in zip(list_num, list_num[1:])))
