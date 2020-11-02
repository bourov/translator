n = int(input())

tns = [print(tn ** 2) for _ in range(n) if not (tn := int(input())) % 7]
