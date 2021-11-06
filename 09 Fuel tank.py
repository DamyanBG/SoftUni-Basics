tip_gorivo = input()
kolichestvo_gorivo = float(input())
klubna_karta = input()

if tip_gorivo == 'Gas':
    if klubna_karta == 'Yes':
        cost = kolichestvo_gorivo*0.85
        if kolichestvo_gorivo < 20:
            print(f'{cost:.2f} lv.')
        elif 20 <= kolichestvo_gorivo <= 25:
            print(f'{cost*0.92:.2f} lv.')
        else:
            print(f'{cost*0.9:.2f} lv.')
    else:
        cost = kolichestvo_gorivo * 0.93
        if kolichestvo_gorivo < 20:
            print(f'{cost:.2f} lv.')
        elif 20 <= kolichestvo_gorivo <= 25:
            print(f'{cost * 0.92:.2f} lv.')
        else:
            print(f'{cost * 0.9:.2f} lv.')
elif tip_gorivo == 'Diesel':
    if klubna_karta == 'Yes':
        cost = kolichestvo_gorivo*2.21
        if kolichestvo_gorivo < 20:
            print(f'{cost:.2f} lv.')
        elif 20 <= kolichestvo_gorivo <= 25:
            print(f'{cost*0.92:.2f} lv.')
        else:
            print(f'{cost*0.9:.2f} lv.')
    else:
        cost = kolichestvo_gorivo * 2.33
        if kolichestvo_gorivo < 20:
            print(f'{cost:.2f} lv.')
        elif 20 <= kolichestvo_gorivo <= 25:
            print(f'{cost * 0.92:.2f} lv.')
        else:
            print(f'{cost * 0.9:.2f} lv.')
elif tip_gorivo == 'Gasoline':
    if klubna_karta == 'Yes':
        cost = kolichestvo_gorivo*2.04
        if kolichestvo_gorivo < 20:
            print(f'{cost:.2f} lv.')
        elif 20 <= kolichestvo_gorivo <= 25:
            print(f'{cost*0.92:.2f} lv.')
        else:
            print(f'{cost*0.9:.2f} lv.')
    else:
        cost = kolichestvo_gorivo * 2.22
        if kolichestvo_gorivo < 20:
            print(f'{cost:.2f} lv.')
        elif 20 <= kolichestvo_gorivo <= 25:
            print(f'{cost * 0.92:.2f} lv.')
        else:
            print(f'{cost * 0.9:.2f} lv.')