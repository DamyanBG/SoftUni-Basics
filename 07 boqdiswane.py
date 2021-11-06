x = float(input())
y = float(input())
h = float(input())

stranichni_steni = 2*x*y-2*2.25
predna_zadna = x*x*2-2.4
obshto_steni = stranichni_steni+predna_zadna

zelena_boq = obshto_steni/3.4

pravoygylnik_pokriv = 2*x*y
triygylnik = 2*(x*h/2)

obshto_pokriv = pravoygylnik_pokriv+triygylnik
chervena_boq = obshto_pokriv/4.3

print(f'{zelena_boq:.2f}')
print(f'{chervena_boq:.2f}')