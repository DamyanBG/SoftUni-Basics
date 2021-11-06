chisla = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

pall = 0

if chisla != 0:
    for i in range(chisla):
        number = int(input())
        if number < 200:
            p1 += 1
        elif number < 400:
            p2 += 1
        elif number < 600:
            p3 += 1
        elif number < 800:
            p4 += 1
        elif number >= 800:
            p5 += 1


    procenti1 = p1/chisla*100
    procenti2 = p2/chisla*100
    procenti3 = p3/chisla*100
    procenti4 = p4/chisla*100
    procenti5 = p5/chisla*100


    print('{:.2f}'.format(procenti1) + '%')
    print('{:.2f}'.format(procenti2) + '%')
    print('{:.2f}'.format(procenti3) + '%')
    print('{:.2f}'.format(procenti4) + '%')
    print('{:.2f}'.format(procenti5) + '%')
