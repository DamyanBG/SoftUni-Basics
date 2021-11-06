ime_aviokompaniq = input()
broi_bileti_vuzrastni = int(input())
broi_detski_bileti = int(input())
netna_cena_vuzrasten = float(input())
cena_taksa_obslujwane = float(input())

netna_cena_detski = netna_cena_vuzrasten*0.3

cena_vyzrasten = netna_cena_vuzrasten+cena_taksa_obslujwane
cena_detski = netna_cena_detski+cena_taksa_obslujwane

total_cost = (broi_bileti_vuzrastni*cena_vyzrasten) + (cena_detski*broi_detski_bileti)

pechalba = total_cost*0.2

print(f'The profit of your agency from {ime_aviokompaniq} tickets is {pechalba:.2f} lv.')