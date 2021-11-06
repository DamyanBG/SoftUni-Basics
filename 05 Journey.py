buidjet = float(input())
sezon = input()

if buidjet <= 100:
    print(f'Somewhere in Bulgaria')
    if sezon == 'summer':
        print(f'Camp - {buidjet*0.3:.2f}')
    else:
        print(f'Hotel - {buidjet*0.7:.2f}')
elif buidjet <= 1000:
    print(f'Somewhere in Balkans')
    if sezon == 'summer':
        print(f'Camp - {buidjet*0.4:.2f}')
    else:
        print(f'Hotel - {buidjet*0.8:.2f}')
elif buidjet > 1000:
    print(f'Somewhere in Europe')
    if sezon == 'summer':
        print(f'Hotel - {buidjet*0.9:.2f}')
    else:
        print(f'Hotel - {buidjet*0.9:.2f}')