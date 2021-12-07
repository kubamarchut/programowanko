import json

def readJson(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    return data

def filterDict(dict, var, val):
    newDict = {}
    for item in dict:
        if dict[item][var] == val:
            if len(list(newDict)) > 0:
                newIndex = list(newDict)[-1] + 1
            else:
                newIndex = 0
            newDict[newIndex] = dict[item]
    return newDict

def convertToMinsAndSecs(coordinates):
    degs = abs(int(coordinates))
    minsec = (abs(coordinates) - degs)*60
    mins = int(minsec)
    secs = int((minsec - mins)*60)
    return "{}°{}\'{}\"".format(degs, mins, secs)

def formatCities(data):
    output = ""
    for item in data:
        city = data[item]
        lng = convertToMinsAndSecs(city["lng"])
        lng_direction = "N" if city["lng"] > 0 else "S"
        lat = convertToMinsAndSecs(city["lat"])
        lat_direction = "E" if city["lat"] > 0 else "W"
        output += "{}\n\tDlugosc:{:>18}{}\n\tSzerokość:{:>16}{}\n\tLiczba ludnosci:{:>11}\n".format(city["city"], lat, lat_direction, lng, lng_direction, city["population"])

    return output

def writeFile(filename, data):
    with open(filename, "w") as txt:
        txt.write(data)

def main():
    data = readJson("wc.json")
    data = filterDict(data, "country", "Poland")
    writeFile("wynik.txt", formatCities(data))

if __name__ == '__main__':
    main()
