n1 = int(input())
n2 = int(input())
operator = input()

resultat = 0


if n2 == 0 and (operator == '/' or operator == '%'):
    print(f'Cannot divide {n1} by zero')
else:
    if operator == '+':
        resultat = n1+n2
    elif operator == '-':
        resultat = n1-n2
    elif operator == '*':
        resultat = n1*n2
    elif operator == '/':
        resultat = n1/n2
    elif operator == '%':
        resultat = n1%n2


    if operator == '/':
        print(f'{n1} {operator} {n2} = {resultat:.2f}', end=' ')
    else:
        print(f'{n1} {operator} {n2} = {resultat}', end=' ')


    if operator == '+' or operator == '-' or operator == '*':
        if resultat % 2 == 0:
            print('- even')
        else:
            print('- odd')