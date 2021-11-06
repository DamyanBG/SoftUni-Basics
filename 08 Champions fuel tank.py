tip_gotivo = input()
litri_v_rezervoar = float(input())

if tip_gotivo == 'Diesel':
    if litri_v_rezervoar >= 25:
        print(f'You have enough diesel.')
    else:
        print(f'Fill your tank with diesel!')
elif tip_gotivo == 'Gasoline':
    if litri_v_rezervoar >= 25:
        print(f'You have enough gasoline.')
    else:
        print(f'Fill your tank with gasoline!')
elif tip_gotivo == 'Gas':
    if litri_v_rezervoar >= 25:
        print(f'You have enough gas.')
    else:
        print(f'Fill your tank with gas!')
else:
    print(f'Invalid fuel!')
