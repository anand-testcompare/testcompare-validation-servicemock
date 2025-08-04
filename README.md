# TestCompare ServiceMock: Supporting Functionality for Testing TestCompare #

Flask utilities for creating simulated APIs as part of the [TestCompare](https://testcompare.ai/) platform.

## Table of contents
* [Release Log](#release-log)
* [Getting Started](#getting-started)
* [Docker](#docker)
* [Testing](#testing)
* [License](#license)

## Release Log
* **Version 0.0.1 (latest)**  _- Inital public release_
  * Static REST POST and GET APIs
  * Update date by adding additional fields to the csv file

## Getting Started ##

### Install Dependencies ###
```
pip install -r requirements.txt
```

### Running the Code ###
```
python app.py
```

## Docker

Build and run the container locally:
```
docker build -t servicemock .
docker run -p 5000:5000 servicemock
```


## Testing ##
Basic info on testing

### Running unit tests ###
```
python -m unittest discover ./test -p '*.py'
```

## License

Copyright © 2025 TestCompare
Released under the [MIT license](https://mit-license.org/).
