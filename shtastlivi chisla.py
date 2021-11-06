chislo_n = int(input())

for i in range(1, 10):
    for h in range(1, 10):
        if chislo_n % (i+h) == 0:
            for b in range(1, 10):
                for c in range(1, 10):
                    if chislo_n % (b+c) == 0:
                        if b+c == i+h:
                            print(f'{i}{h}{b}{c}', end=' ')
