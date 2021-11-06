gradusi = float(input())

if gradusi > 35:
    print('unknown')
elif gradusi >= 26:
    print('Hot')
elif gradusi >= 20.1:
    print('Warm')
elif gradusi >= 15:
    print('Mild')
elif gradusi >= 12:
    print("Cool")
elif gradusi >= 5:
    print("Cold")
else:
    print("unknown")