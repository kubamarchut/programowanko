import json
#from random import randint # - potrzebny do generowania studentów

"""
student = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "nrIndeksu": "382102",
    "sredniaOcen": 3.5,
    "pary": [("MEPI", 5),
             ("PELP1", 3),
             ("ANLI", 3),
             ("WDT", 3),
             ("ALGT", 3),
             ("TECY", 4)]
}
"""
students = [
    {
        "imie": "Jakub",
        "nazwisko": "Nowak",
        "nrIndeksu": "801069",
        "sredniaOcen": 4.333333333333333,
        "pary": [
            ("MEPI", 5),
            ("PELP1", 3),
            ("ANLI", 3),
            ("WDT", 3),
            ("ALGT", 3),
            ("TECY", 4),
        ],
    },
    {
        "imie": "Paweł",
        "nazwisko": "Rosłon",
        "nrIndeksu": "309057",
        "sredniaOcen": 3.3333333333333335,
        "pary": [
            ("MEPI", 5),
            ("PELP1", 3),
            ("ANLI", 3),
            ("WDT", 3),
            ("ALGT", 3),
            ("TECY", 4),
        ],
    },
    {
        "imie": "Alicja",
        "nazwisko": "Kwiatowska",
        "nrIndeksu": "466630",
        "sredniaOcen": 3.3333333333333335,
        "pary": [
            ("MEPI", 5),
            ("PELP1", 3),
            ("ANLI", 3),
            ("WDT", 3),
            ("ALGT", 3),
            ("TECY", 4),
        ],
    },
    {
        "imie": "Eustachy",
        "nazwisko": "Kwaśniewski",
        "nrIndeksu": "209101",
        "sredniaOcen": 3.1666666666666665,
        "pary": [
            ("MEPI", 5),
            ("PELP1", 3),
            ("ANLI", 3),
            ("WDT", 3),
            ("ALGT", 3),
            ("TECY", 4),
        ],
    },
    {
        "imie": "Julia",
        "nazwisko": "Niewiadomska",
        "nrIndeksu": "190490",
        "sredniaOcen": 3.1666666666666665,
        "pary": [
            ("MEPI", 5),
            ("PELP1", 3),
            ("ANLI", 3),
            ("WDT", 3),
            ("ALGT", 3),
            ("TECY", 4),
        ],
    },
]


"""
#funkcja do generowania listy słowników o studentach

def generateStudents(student):
    students = [];
    for i in range(5):
        next_student = student.copy();
        next_student["imie"] = input("Podaj imie studenta: ")
        next_student["nazwisko"] = input("Podaj nazwisko studenta: ")
        next_student["nrIndeksu"] = str(randint(100000, 999999))

        marks = []
        new_pairs = []
        for pairs in next_student["pary"]:
            new_mark = randint(2, 5)
            marks.append(new_mark)
            new_pairs.append((pairs[0], new_mark))


        next_student["sredniaOcen"] = sum(marks) / len(marks)
        students.append(next_student)

    print(students)

generateStudents(student)
"""

def printStudent(nrIndeksu, lst):
    current_student = lst[0]
    for student in lst:
        if student["nrIndeksu"] == nrIndeksu:
            current_student = student
            break

    print("\nInforamcje o studencie:")
    print("\tImie:", current_student["imie"])
    print("\tNazwisko:", current_student["nazwisko"])
    print("\tŚrednia:", current_student["sredniaOcen"])
    print("\tOceny:")
    for mark in current_student["pary"]:
        print("\t\t", mark[0] + ":", mark[1])

def printAllStudents(lst):
    for student in lst:
        printStudent(student["nrIndeksu"], lst)

def saveStudentsToFile(filename):
    with open(filename, 'w') as file:
        json.dump(students, file)

def readStudentsFromFile(filename):
    with open(filename, "r") as read_file:
        data = json.load(read_file)

    return data

if __name__ == '__main__':
    printStudent("309057", students)
    printAllStudents(students)
    saveStudentsToFile("bazastudentow.json")
    printAllStudents(readStudentsFromFile("bazastudentow.json"))
