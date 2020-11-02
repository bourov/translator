# put your python code here
year = int(input())

ndiv4 = year % 4  # not divisible by 4
ndiv100 = year % 100
ndiv400 = year % 400

print("Ordinary" if ndiv4 or (not ndiv100 and ndiv400) else "Leap")
