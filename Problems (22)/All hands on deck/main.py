face_values = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
deck = [int(face_values.get(i := input(), i)) for _ in range(6)]
print(sum(deck) / 6)
