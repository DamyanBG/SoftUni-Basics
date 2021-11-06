vuvejdane = input()
chislo = 0
deleniq_na_chislo = 0
sbor_neprosti = 0
sbor_prosti = 0

while vuvejdane != 'stop':
    chislo = int(vuvejdane)
    if chislo < 0:
        print('Number is negative.')
    elif chislo > 1:
        for i in range(1, chislo + 1):
            if chislo % i == 0:
                deleniq_na_chislo += 1
        if deleniq_na_chislo > 2:
            sbor_neprosti += chislo
        else:
            sbor_prosti += chislo
    else:
        sbor_neprosti += chislo
    deleniq_na_chislo = 0
    vuvejdane = input()

print(f'Sum of all prime numbers is: {sbor_prosti}')
print(f'Sum of all non prime numbers is: {sbor_neprosti}')