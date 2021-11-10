def isbn_10(isbn):
    ctrlsum = 0
    for index, num in enumerate(isbn[:-1]):
        ctrlsum += (index + 1) * int(num)

    return ctrlsum % 11 == int(isbn[-1])

def isbn_13(isbn):
    ctrlsum = 0
    for index, num in enumerate(isbn[:-1]):
        waga = 1 if index % 2 == 0 else 3
        ctrlsum += waga * int(num)

    ctrlsum = 10 - ctrlsum % 10
    return ctrlsum % 10 == int(isbn[-1])


def sprawdzanie_isbn(isbn):
    isbn = isbn.replace("-", "")
    isbn_length = len(isbn)
    if isbn_length == 10 or isbn_length == 13:
        if isbn_length == 10:
            if isbn_10(isbn):
               print('Ten ISBN-10 jest prawidłowy')
            else:
               print('Ten ISBN-10 nie jest prawidłowy')
        elif isbn_length == 13:
            if isbn_13(isbn):
                print('Ten ISBN-13 jest prawidłowy')
            else:
                print('Ten ISBN-13 nie jest prawidłowy')

    else:
        print("Prawidłowy kod ISBN musi mieć 10 lub 13 cyfr")


if __name__ == '__main__':
    sprawdzanie_isbn(input("Podaj numer ISBN: "))
    sprawdzanie_isbn("0-306-40615-2")
    sprawdzanie_isbn("978-3-16-148410-0")
    sprawdzanie_isbn("978-3-16-1480-0")
    sprawdzanie_isbn("938-3-16-142341-0")