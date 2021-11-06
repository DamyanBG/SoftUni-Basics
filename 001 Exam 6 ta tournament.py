broi_dni_turnir = int(input())

result = ''
raised_money_day = 0
broi_pobedi = 0
broi_zagubi = 0
pobedni_dni = 0
zagubeni_dni = 0
raised_money = 0

for i in range(broi_dni_turnir):
    sport = input()
    raised_money_day = 0
    broi_pobedi = 0
    broi_zagubi = 0
    while sport != 'Finish':
        result = input()
        if result == 'win':
            raised_money_day += 20
            broi_pobedi += 1
        else:
            broi_zagubi += 1
        sport = input()
    if broi_pobedi > broi_zagubi:
        raised_money_day += raised_money_day*0.1
        pobedni_dni += 1
    else:
        zagubeni_dni += 1
    raised_money += raised_money_day

if pobedni_dni > zagubeni_dni:
    raised_money += raised_money*0.2
    print(f'You won the tournament! Total raised money: {raised_money:.2f}')
else:
    print(f'You lose the tournament! Total raised money: {raised_money:.2f}')