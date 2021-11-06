import math

h = float(input())
w = float(input())

buira_na_red = math.floor((w*100-100)/70)
redove = math.floor(h*100/120)

buira =buira_na_red*redove-3

print(buira)
