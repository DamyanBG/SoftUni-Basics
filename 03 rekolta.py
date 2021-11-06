import math

kvadratiLoze = int(input())
grozdenakvadrat = float(input())
nujniLitriVino = int(input())
broi_rabotnici = int(input())

obshto_grozde = kvadratiLoze*grozdenakvadrat
vino = 0.4*obshto_grozde/2.5

if vino < nujniLitriVino:
    print(f'It will be a tough winter! More {math.floor(nujniLitriVino-vino)} liters needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(vino)} liters.')
    ostavashto = vino-nujniLitriVino
    nachovek = ostavashto/broi_rabotnici
    print(f'{math.floor(ostavashto)} liters left -> {math.floor(nachovek)} liters per person.')