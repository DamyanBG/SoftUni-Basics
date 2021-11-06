cena_ekskurziq = float(input())
broi_puzeli = int(input())
broi_gov_kukli = int(input())
broi_mecheta = int(input())
broi_minioni = int(input())
broi_kamioncheta = int(input())

total = broi_puzeli*2.6+broi_gov_kukli*3+broi_mecheta*4.1+broi_minioni*8.2+broi_kamioncheta*2

broi_igrachki = broi_puzeli+broi_gov_kukli+broi_mecheta+broi_minioni+broi_kamioncheta

if broi_igrachki >= 50:
    total = total-(total*0.25)

pechalba = total-(total*0.1)

if pechalba >= cena_ekskurziq:
    print(f'Yes! {pechalba-cena_ekskurziq:.2f} lv left.')
else:
    print(f'Not enough money! {cena_ekskurziq-pechalba:.2f} lv needed.')