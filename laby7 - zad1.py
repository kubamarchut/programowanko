def czescWspolna(tab1, tab2):
    res = []
    for i in tab1:
        for j in tab2:
            if i == j:
                res.append(i)
    return res

def suma(tab1, tab2):
    res = []
    for i in tab1:
        if i not in res:
            res.append(i)

    for i in tab2:
        if i not in res:
            res.append(i)
    return res

def roznica(tab1, tab2):
    res = []
    for i in tab1:
        dontadd = False
        for j in tab2:
            if i == j:
                dontadd = True
        if not dontadd:
            res.append(i)
            dontadd = False
    return res

def zmienNaTablice(tekst):
    return tekst[1:-1].split(',')

def operacjeNaZbiorach(polecenie):
    if '*' in polecenie:
        tablica1 = zmienNaTablice(polecenie.split('*')[0])
        tablica2 = zmienNaTablice(polecenie.split('*')[1])
        print(czescWspolna(tablica1, tablica2))
    elif '+' in polecenie:
        tablica1 = zmienNaTablice(polecenie.split('+')[0])
        tablica2 = zmienNaTablice(polecenie.split('+')[1])
        print(suma(tablica1, tablica2))
    elif '-' in polecenie:
        tablica1 = zmienNaTablice(polecenie.split('-')[0])
        tablica2 = zmienNaTablice(polecenie.split('-')[1])
        print(roznica(tablica1, tablica2))

if __name__ == '__main__':
    operacjeNaZbiorach('[5,3,8]*[1,0,3]')
    operacjeNaZbiorach('[5,3,8]+[1,0,3]')
    operacjeNaZbiorach('[5,3,8]-[1,0,3]')
