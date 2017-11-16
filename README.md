# GyphiH

GyphiH is an API to retrieve Gyphis from a list of locations. This Django based API get a ‘location’ and ‘limit’ as “GET” parameters and return a list of Gyphis. The initial supplied ‘location’ will be used to get a list of similar locations (using Googlemaps APIs). Then locations from the list will be query to get associated Gyphis (using Gyphi APis andlimited by the ‘limit’ parameter)

## Getting Started & Prerequisites
1.	Requirements:
a.	DJANGO - pip install django,
b.	RESTFRAMEWORK - pip install djangorestframework,
c.	GOOGLEMAPS - pip install -U googlemaps, 
d.	ACQUIRING API KEYS -  for both googlemaps and Gyph – > one should create a ‘secret.txt’ file inside ‘api’ folder. The
Secret file should resemble:
```
{
    "GOOGLE_API": "API_KEY",
    "GYPHI_API": "API_KEY"
}
```
 Then the backend can be launch using Django framework development server –``` manage.py runserver``` command.


## GET request and response
The project contain a single API call (GET request) -  ``` http://address:port/api/v1/gyphi/location/limit/``` - where “location” and “limit” are parameters. Location is of type str (limit to 25 characters) and limit is of type int.

The GET request will return the following response structure
```
[
    {
        "place": "Washington Square South",
        "status": 200,
        "giphy": [
            {
                "title": "1962 GIF",
                "images": "https://media1.giphy.com/media/YCcfpIMkBLySc/giphy.gif"
            },
            {
                "title": "jumping good night GIF by Party Down South",
                "images": "https://media0.giphy.com/media/3oEdvbQ9SwvLaZTY40/giphy.gif"
            }
        ]
    }
]
```
