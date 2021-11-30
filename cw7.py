from geopy.geocoders import Nominatim
import json

cities = ['Warsaw', "Kraków", "Gdansk", "New York", "San francisco", "Melbourne"]

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
        print(geo_data_city)
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

def beautifulPrinting(data):
    for city in data:
        minutes = city['szerokosc'] * 60 % 60
        seconds = city['szerokosc'] * 3600 % 3600
        print(f"Współrzędne dla {city['nazwa']}: {city['szerokosc']:.0f}°{minutes:.0f}\'{seconds:.0f}N szerokosc, {city['dlugosc']:.0f}°{city['dlugosc']:.2f}\'E dlugosc")

def main():
    saveToFile('data.json', getCoordinates(cities))
    beautifulPrinting(readFile('data.json'))
if __name__ == '__main__':
    main()
