from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK
import json
import os

@api_view(['GET'])
def getGyphi(request, location, limit):
    #Grabing secrets from files (api key)
    path = os.path.dirname(os.path.abspath(__file__)) + '\secret.txt'
    with open(path, 'r') as file:
        jsonObject = json.loads(file.read())
    #Get locations list
    list = getPlaces(location, jsonObject['GOOGLE_API'])
    #Get Gyphi from location
    jsonArray = json.loads(getGifs(list, limit, jsonObject['GYPHI_API']))
    return Response(jsonArray, status=HTTP_200_OK)



import googlemaps
from urllib.request import urlopen


def getPlaces(value, key):
    """Get similar location according to an initial @param (value);
        Use Google Places API to retrieve information;
        Return a set of places;
        """
    gmaps = googlemaps.Client(key=key)
    geocode_result = gmaps.places_autocomplete(value)
    setPlace = set()
    for place in geocode_result:
        location = str(place['structured_formatting']['main_text'])
        setPlace.add(location)
    return setPlace


def getGifs(list, limit, key):
    """Get the matched Gyphis for item in @param list;
            Use Gyphi API to retrieve data;
            @param limit set max size for the result set;
            Return a JsonArray of the result set as follow [{"place": x, "status": y, "giphy": [{}]];
            """
    host = 'http://api.giphy.com'
    api_key = key
    path = '/v1/gifs/search?q={}&api_key={}&limit={}'
    jsonArray = []
    index = 0
    for place in list:
        jsonResponse = json.loads(
            urlopen(host + path.format(str(place).replace(' ', '+'), api_key, limit)).read().decode('utf-8'))
        jsonArray.append({'place': place, 'status': jsonResponse['meta']['status'], 'giphy': []})
        for gif in jsonResponse['data']:
            jsonObject = {}
            jsonObject['title'] = gif['title']
            jsonObject['images'] = gif['images']['original']['url']
            jsonArray[index]['giphy'].append(jsonObject)
        index += 1
    return json.dumps(jsonArray)