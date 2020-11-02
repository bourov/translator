from math import floor

grades = {5: 'F', 6: 'D', 7: "C", 8: 'B', 9: 'A'}

score = int(input())
max_score = int(input())

sr = floor(score * 10 / max_score)

sr = max(sr, 5)
sr = min(sr, 9)

print(grades[sr])
