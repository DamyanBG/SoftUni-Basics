shirina = int(input())
duljina = int(input())
wzemane = 0

broi_parcheta = shirina*duljina

while broi_parcheta > 0:
    wzemane = input()
    if wzemane == 'STOP':
        break
    broi_parcheta -= int(wzemane)

if broi_parcheta >= 0:
    print(f'{broi_parcheta} pieces are left.')
else:
    print(f'No more cake left! You need {abs(broi_parcheta)} pieces more.')
