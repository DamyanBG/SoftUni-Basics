cena_bagaj_nad_20 = float(input())
kilogrami_bagaj = float(input())
dni_do_pytuwane = int(input())
broi_bagaji = int(input())

cena_bagaj = 0

if kilogrami_bagaj < 10:
    cena_bagaj = cena_bagaj_nad_20*0.2
elif 10 <= kilogrami_bagaj <= 20:
    cena_bagaj = cena_bagaj_nad_20*0.5
else:
    cena_bagaj = cena_bagaj_nad_20

if dni_do_pytuwane > 30:
    cena_bagaj += cena_bagaj*0.1
elif 7 <= dni_do_pytuwane <= 30:
    cena_bagaj += cena_bagaj*0.15
else:
    cena_bagaj += cena_bagaj*0.4

total = cena_bagaj*broi_bagaji

print(f'The total price of bags is: {total:.2f} lv.')