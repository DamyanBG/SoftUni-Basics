flowers = input()
broi_cwetq = int(input())
buidjet = int(input())

cost = 0

if flowers == 'Roses':
    cost = broi_cwetq*5
    if broi_cwetq > 80:
        cost = cost*0.9
elif flowers == 'Dahlias':
    cost = broi_cwetq*3.8
    if broi_cwetq > 90:
        cost = cost*0.85
elif flowers == 'Tulips':
    cost = broi_cwetq*2.8
    if broi_cwetq > 80:
        cost = cost*0.85
elif flowers == 'Narcissus':
    cost = broi_cwetq*3
    if broi_cwetq < 120:
        cost = cost*1.15
elif flowers == 'Gladiolus':
    cost = broi_cwetq*2.5
    if broi_cwetq < 80:
        cost = cost*1.2

if buidjet >= cost:
    print(f'Hey, you have a great garden with {broi_cwetq} {flowers} and {buidjet-cost:.2f} leva left.')
else:
    print(f'Not enough money, you need {cost-buidjet:.2f} leva more.')