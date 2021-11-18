def commonpart(list1, list2):
    res = []
    for i in list1:
        for j in list2:
            if i == j:
                res.append(i)
    return res

def both(list1, list2):
    res = []
    for i in list1:
        if i not in res:
            res.append(i)

    for i in list2:
        if i not in res:
            res.append(i)
    return res

def difference(list1, list2):
    res = []
    for i in list1:
        reapets = False
        for j in list2:
            if i == j:
                reapets = True
        if not reapets:
            res.append(i)
            reateps = False
    return res

def convertToList(text):
    return text[1:-1].split(',')

def collection_operations(math_operation):
    if '*' in math_operation:
        list1 = convertToList(math_operation.split('*')[0])
        list2 = convertToList(math_operation.split('*')[1])
        print(commonpart(list1, list2))
    elif '+' in math_operation:
        list1 = convertToList(math_operation.split('+')[0])
        list2 = convertToList(math_operation.split('+')[1])
        print(both(list1, list2))
    elif '-' in math_operation:
        list1 = convertToList(math_operation.split('-')[0])
        list2 = convertToList(math_operation.split('-')[1])
        print(difference(list1, list2))

if __name__ == '__main__':
    def check_coll(coll):
        if coll[0] == "[" and coll[-1] == "]":
            numbers = convertToList(coll.strip())
            for number in numbers:
                if not number.isdigit():
                    return False
            return True
        else:
            return False
    operation = input("Podaj operacje: ")
    if operation[0] == '[' and operation[-1] == ']':
        if '*' in operation:
            if '+' not in operation and '-' not in operation:
                if check_coll(operation.split('*')[0]) and check_coll(operation.split('*')[1]):
                    collection_operations(operation)
                else:
                    print('Podano nieprawidlowe dane')
            else:
                print('Podano nieprawidlowe dane')
        elif '+' in operation:
            if '*' not in operation and '-' not in operation:
                if check_coll(operation.split('+')[0]) and check_coll(operation.split('+')[1]):
                    collection_operations(operation)
                else:
                    print('Podano nieprawidlowe dane')
            else:
                print('Podano nieprawidlowe dane')
        elif '-' in operation:
            if '+' not in operation and '*' not in operation:
                if check_coll(operation.split('-')[0]) and check_coll(operation.split('-')[1]):
                    collection_operations(operation)
                else:
                    print('Podano nieprawidlowe dane')
            else:
                print('Podano nieprawidlowe dane')
        else:
            print('Podano nieprawidlowe dane')
    else:
        print('Podano nieprawidlowe dane')
    collection_operations('[2,3,4]*[2,3]')
    collection_operations('[2,3,4]+[2,3]')
    collection_operations('[2,3,4]-[2,3]')
