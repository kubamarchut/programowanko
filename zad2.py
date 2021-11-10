def czytaj_plik(nazwa_pliku, nazwa_pliku_wyj):
    dane = []

    f = open(nazwa_pliku, "r")
    for index, line in enumerate(f.read().replace('.\n', '.').replace('\n', '.').split('.')):
        line = line.strip()
        if len(line) > 0:
            dane.append(str({'klucz': index+1, 'Z': oblicz_zlozonosc(line)}) + '\r\n')

    f.close()
    f = open(nazwa_pliku_wyj, "w+")
    f.writelines(dane)
    f.close()

def czy_twarde(slowo):
    samogloski = ['a', 'ą', 'e', 'ę', 'y', 'u', 'i', 'o', 'ó']
    liczba_samo = 0
    liczba_nast_spol = 0
    for letter in slowo:
        if letter.lower() in samogloski:
            liczba_samo += 1
            liczba_nast_spol = 0
        else:
            liczba_nast_spol += 1
            if liczba_nast_spol == 3:
                return True

    # print(liczba_samo, len(slowo) - liczba_samo)
    return len(slowo) - liczba_samo > liczba_samo

def oblicz_zlozonosc(zdanie):
    liczba_t = 0
    liczba_m = 0
    for word in zdanie.split():
        if czy_twarde(word):
            liczba_t += 1
        else:
            liczba_m += 1
    #print(liczba_m, liczba_t)
    return 5*liczba_t + 3*liczba_m

if __name__ == '__main__':
    czytaj_plik("zdania.txt", "wyj.txt")