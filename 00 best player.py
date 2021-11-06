ime_igrach = input()
gol_maistor = ''
maistor_golove = 0
hattrick = False

while ime_igrach != 'END':

    broi_golove = int(input())
    if broi_golove > maistor_golove:
        gol_maistor = ime_igrach
        maistor_golove = broi_golove
        if broi_golove >= 3:
            hattrick = True
    if broi_golove >= 10:
        break
    ime_igrach = input()

print(f'{gol_maistor} is the best player!')

if hattrick:
    print(f'He has scored {maistor_golove} goals and made a hat-trick !!!')
else:
    print(f'He has scored {maistor_golove} goals.')
