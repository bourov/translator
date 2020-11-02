# put your python code here
year = int(input())

div4 = not year % 4
div100 = not year % 100
div400 = not year % 400

print("Leap" if div4 and not div100 or div400 else "Ordinary")
