broi_dogrami = int(input())
vid_dograma = input()
poluchavane = input()
price = 0
total = 0

if broi_dogrami <10:
    print('Invalid order')
else:
    if vid_dograma == '90X130':
        price = 110
        if 30 < broi_dogrami <= 60:
            price -= price*0.05
        elif broi_dogrami > 60:
            price -= price*0.08
    elif vid_dograma == '100X150':
        price = 140
        if 40 < broi_dogrami <= 80:
            price -= price*0.06
        elif broi_dogrami > 80:
            price -= price*0.1
    elif vid_dograma == '130X180':
        price = 190
        if 50 < broi_dogrami <= 50:
            price -= price*0.07
        elif broi_dogrami > 50:
            price -= price*0.12
    elif vid_dograma == '200X300':
        price = 250
        if 25 < broi_dogrami <= 50:
            price -= price*0.09
        elif broi_dogrami > 50:
            price -= price*0.14

    total = broi_dogrami*price

    if poluchavane == 'With delivery':
        total += 60

    if broi_dogrami >= 100:
        total -= total*0.04

    print(f'{total:.2f} BGN')