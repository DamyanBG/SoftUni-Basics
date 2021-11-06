import math

broi_topki = int(input())
cvqt = ''
tochki = 0
red_ball = 0
orange_ball = 0
yellow_ball = 0
white_ball = 0
black_ball = 0
other_ball = 0

for i in range(broi_topki):
    cvqt = input()
    if cvqt == 'red':
        tochki += 5
        red_ball += 1
    elif cvqt == 'orange':
        tochki += 10
        orange_ball += 1
    elif cvqt == 'yellow':
        tochki += 15
        yellow_ball += 1
    elif cvqt == 'white':
        tochki += 20
        white_ball += 1
    elif cvqt == 'black':
        tochki = math.floor(tochki/2)
        black_ball += 1
    else:
        other_ball += 1

print(f"Total points: {tochki:}")
print(f"Red balls: {red_ball}")
print(f"Orange balls: {orange_ball}")
print(f"Yellow balls: {yellow_ball}")
print(f"White balls: {white_ball}")
print(f"Other colors picked: {other_ball}")
print(f"Divides from black balls: {black_ball}")