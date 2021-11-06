stupki_vuvejdane = input()
obshto_stupki = 0

while stupki_vuvejdane != 'Going home':
    obshto_stupki += int(stupki_vuvejdane)
    if obshto_stupki >= 10000:
        break
    stupki_vuvejdane = input()


if stupki_vuvejdane == 'Going home':
    a = int(input())
    obshto_stupki += a

if obshto_stupki < 10000:
    print(f'{10000-obshto_stupki} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{obshto_stupki - 10000} steps over the goal!')