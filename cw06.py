# -*- coding: utf-8 -*-
"""
Oczekiwane działanie programu:
    1. Program wczytuje dostarczony plik tekstowy dane.txt.
    2. Następuje zliczenie sum liczb z każdej linii pliku.
    3. Program zapisuje czytelny dla czlowieka plik wynikowy outfile.txt
       zawierający obliczone sumy liczb dla kolejnych wierszy z pliku wejsciowego.
    4. Obliczone sumy są także wypisywane na konsoli.

Niestety, program zawiera błędy - znajdź i popraw je. Wszystkie chwyty dozwolone.
"""

import os


students = [
    {
        'imie': 'Json',
        'nazwisko': 'Statham',
        'indeks': '000000',
        'grades': [['PELP1', 2], ['PRM1T', 5]],
    },
    {
        'imie': 'Json',
        'nazwisko': 'Statham',
        'indeks': '000111',
        'grades': [['ANL1T', 2], ['WDT', 5]],
    },
]

""" Wywołanie funkcji odbywa się pod "if main"
print("Uruchomienie programu")

filename = "dane.txt"
file=open('dane.txt', "r")

print("Wczytano plik")
"""

# Funkcja zwraca liczby zawarte w kolejnych wierszach pliku o nazwie wskazanej
# w argumencie.
# Wartosci są zwracane w postaci zagnieżdżonej listy liczb:
#   każda linijka jest reprezentowana przez listę liczb, a te listy są elementami listy zbiorczej
def read_from_file(filename):
    file = open(filename, "r") #otwieramy plik po nazwie podanej w argumencie funkcji a nie zapisanej "na twardo"
    lines = []
    for line in file:
        line = line.strip().split(sep=" ") #usunięcie zanku końca linii + liczby podrozdzielane są spacją a nie przecinkiem użycie nazwy line zamiast line_
        lines.append(line) # dopisanie nowej listy do listy list
    return lines # zwaracam tablicę zawierającą sumy z wszystkich linii a nie ostatnią sumę z ostatniej linii
    file.close()


# Funkcja zwraca sumę liczb dostarczonych w postaci listy liczb
def count_sum_in_line(line):
    sum = 0
    for number in line:
        sum += int(number) # zliczam sumę a nie iloraz liczb z poszczególnych linii
    return sum


# Funkcja zwraca listę sum dla kolejnych list liczb dostarczonych w argumencie
def count_sums(lines):
    sums=[] # sums będzie przechowywało dane jednowymiarowe (bez kluczy same wartości) czyli używam tablicy a nie słownika
    for line in lines:
        line_sum = count_sum_in_line(line)
        sums.append(line_sum)
    return sums


# Funkcja zapisuje do pliku o wskazanej nazwie liczby z kolejnych elementów dostarczonej listy
def save_to_file(filename, data):
    #os.remove(filename)    # usun poprzednia wersje pliku
    with open(filename, "w") as file: #użycie trybu "w" pozwala na aktualizowanie pliku bez konieczności usuwania go
        i = 0
        for d in data:
            i += 1 #nr kolejnej linii musi zosatć za karzbym razem zwiękoszony o jeden aby odpowiadał nr wiersza, dla którego policzono sumę
            print(f"Sum in line {i}: {d}", file=file)
            print(f"Sum in line {i}: {d}") # wykorzystuje drugiego printa aby wypisać te same dane do konsoli

# Writer
def writer():
    file=open('liczby.dat', "w")
    max_i = 10
    max_j = 20
    for i in range(max_i):
        for j in range(max_j):
            value = i*max_j+j
            file.write(str(value)+" ")
        file.write("\n")
    file.close()


if __name__=="__main__":
    print("Wczytuje dane z pliku")
    #writer() użycie funkcji writer nie jest konieczne podobnie jak słownika z danymi o studentach
    lines = read_from_file("dane.txt") # nazwa podanego pliku wejściowego ma inną nazwę
    sums = count_sums(lines)
    save_to_file("outfile.txt", sums) # podanie przy wywołaniu funkcji odpowiedniej nazwy pliku wejściowego zamiastodwołania się do wartości pustej zmiennej
    #print(sums) wykorzystuje printa w innym miejscu do wypisania danych w konsoli dla użytkownika
