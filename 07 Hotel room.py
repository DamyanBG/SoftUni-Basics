mesec = input()
broi_noshtuvki = int(input())

price_studio = 0
price_apartament = 0

if mesec == 'May' or mesec == 'October':
    price_studio = 50
    price_apartament = 65
elif mesec == 'June' or mesec == "September":
    price_studio = 75.20
    price_apartament = 68.70
elif mesec == 'July' or mesec == 'August':
    price_studio = 76
    price_apartament = 77

cost_studio = broi_noshtuvki*price_studio
cost_apartament = broi_noshtuvki*price_apartament

if 7 < broi_noshtuvki <= 14 and (mesec == 'May' or mesec == 'October'):
    cost_studio = cost_studio*0.95
elif broi_noshtuvki > 14:
    if mesec == 'May' or mesec == 'October':
        cost_studio = cost_studio*0.7
    elif mesec == 'June' or mesec == 'September':
        cost_studio = cost_studio*0.8

if broi_noshtuvki > 14:
    cost_apartament = cost_apartament*0.9

print(f'Apartment: {cost_apartament:.2f} lv.')
print(f'Studio: {cost_studio:.2f} lv.')