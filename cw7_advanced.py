from geopy.geocoders import Nominatim
import json, math, sys

cities = ['Warsaw', "Kraków", "Gdansk", "New York", "San francisco", "Melbourne"]

data = [{'nazwa': 'Warsaw', 'dlugosc': 21.0067249, 'szerokosc': 52.2319581},
{'nazwa': 'Kraków', 'dlugosc': 19.9368564, 'szerokosc': 50.0619474},
{'nazwa': 'Gdansk', 'dlugosc': 18.62860883362069, 'szerokosc': 54.36119285},
{'nazwa': 'New York', 'dlugosc': -74.0060152, 'szerokosc': 40.7127281},
{'nazwa': 'San francisco', 'dlugosc': -122.419906, 'szerokosc': 37.7790262},
{'nazwa': 'Melbourne', 'dlugosc': 144.9631608, 'szerokosc': -37.8142176}]

def getCoordinates(cities):
    print("pobieranie danych...")
    geolocator = Nominatim(user_agent="locationapp")

    geo_data = []
    for city in cities:
        location = geolocator.geocode(city)
        geo_data_city = {}
        geo_data_city['nazwa'] = city
        geo_data_city['dlugosc'] = location.longitude
        geo_data_city['szerokosc'] = location.latitude
        geo_data.append(geo_data_city)
    return geo_data

def saveToFile(filename, data):
    print("zapisywanie danych")
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def readFile(filename):
    print("czytanie danych")
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    return data

def convertToMinsAndSecs(coordinates):
    degs = abs(int(coordinates))
    minsec = (abs(coordinates) - degs)*60
    mins = int(minsec)
    secs = int((minsec - mins)*60)
    return [degs, mins, secs, coordinates>0]

def beautifulPrinting(data):
    for city in data:
        long = convertToMinsAndSecs(city['szerokosc'])
        long_direction = "N" if long[3] else "S"
        lati = convertToMinsAndSecs(city['dlugosc'])
        lati_direction = "E" if lati[3] else "W"
        print(f"Współrzędne dla {city['nazwa']}: {long[0]}°{long[1]}\'{long[2]}{long_direction} szerokosc, {lati[0]}°{lati[1]}\'{lati[2]}{lati_direction} dlugosc")

def main():
    saveToFile('data.json',data)
    beautifulPrinting(readFile('data.json'))
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "geoapi":
             saveToFile('data.json', getCoordinates(cities))
             beautifulPrinting(readFile('data.json'))
    else:
        saveToFile('data.json', data)
        beautifulPrinting(readFile('data.json'))
