plod = input()
set_size = input()
broi_poruchani_setove = int(input())

if plod == 'Watermelon':
    if set_size == 'small':
        cost = 56*2*broi_poruchani_setove
    elif set_size == 'big':
        cost = 28.7*5*broi_poruchani_setove
elif plod == 'Mango':
    if set_size == 'small':
        cost = 36.66*2*broi_poruchani_setove
    elif set_size == 'big':
        cost = 19.6*5*broi_poruchani_setove
elif plod == 'Pineapple':
    if set_size == 'small':
        cost = 42.1*2*broi_poruchani_setove
    elif set_size == 'big':
        cost = 24.8*5*broi_poruchani_setove
elif plod == 'Raspberry':
    if set_size == 'small':
        cost = 20*2*broi_poruchani_setove
    elif set_size == 'big':
        cost = 15.2*5*broi_poruchani_setove

if 400 <= cost <= 1000:
    final_price = cost-(cost*0.15)
    print(f'{final_price:.2f} lv.')
elif cost > 1000:
    final_price = cost/2
    print(f'{final_price:.2f} lv.')
else:
    print(f'{cost:.2f} lv.')