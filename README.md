# GyphiH

GyphiH is an API to retrieve Gyphis from a list of locations. This Django based API get a ‘location’ and ‘limit’ as a “GET” parameters and return a list of Gyphis. The initial supplied ‘location’ will be used to get a list of similar locations (using Googlemaps APIs), then each location from the list will be query to get associated Gyphis (limited by the ‘limit’ parameter)

## Getting Started & Prerequisites
1.	Requirements:
a.	pip install django
b.	pip install djangorestframework
c.	pip install -U googlemaps
d.	API Keys for both googlemaps and Gyph – create a ‘secret.txt’ file inside ‘api’ folder. The
Secret file should resemble:
{
    "GOOGLE_API": "API_KEY",
    "GYPHI_API": "API_KEY"
}
 Following the requirements, the backend can be launch using Django framework development server – manage.py runserver command.
```
Give examples
```
The project contains a single API (GET request) of the form-  http://address:port/api/v1/gyphi/location/limit/ - where “location” and “limit” are the parameters. Location is of type string (limit to 25 character) and limit is a number.

The GET request will return the following response structure
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
of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
