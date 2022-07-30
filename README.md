# TestCompare ServiceMock: Supporting Functionality for Testing TestCompare #

_Flask code to create simulated APIs_ 

## Table of contents
* [Release Log](#release-log)
* [Gettng Started](#getting-started)
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

### NOT NEEDED force deploy the code on cloud run ###
```
#gcloud builds submit --tag gcr.io/compareme-325015/servicemock .
#gcloud beta run deploy --image gcr.io/compareme-325015/servicemock
```


## Testing ##
Basic info on testing

### Running unit tests ###
```
python -m unittest discover ./test -p '*.py'
```

## License

Copyright © 2021 [Anand Pant](https://bitbucket.org/anandpant/)
Released under the [MIT license](https://mit-license.org/).
