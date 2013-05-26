[Device42](http://www.device42.com/) is a comprehensive data center management software.

This repository hosts a python script to easily input data to device42 appliance via APIs.


### Script Provided
-----------------------------
   * csv2d42apis.py : Reads a CSV file, matches columns to arguments for APIs and sends data to device42 via POST or PUT.

### Requirements
-----------------------------
   * Python. Tested with python 2.4-2.7.
   * If you don't have python installed already, you can download and install from: [http://www.python.org/download/releases/](http://www.python.org/download/releases/)


### Usage
-----------------------------

1. Create comma separated CSV file with following:
    * Header row values must match the API arguments.  API call arguments documented at: [http://docs.device42.com/api/](http://docs.device42.com/api/)
    * Add the data you need to send to device42 appliance.

2. You will need to Change the lines 26-31 in the script to match your environment:
    * `D42_API_URL` will be the d42 instance base url plus the api call url. API call urls available at: [http://docs.device42.com/api/](http://docs.device42.com/api/)
    * `D42_USERNAME` and `D42_PASSWORD` are self explanatory.
    * `API_METHOD` will be put or post, depending on the call. (As found in documentation linked above)
    * `CSV_FILE_NAME` will be the name of the csv file with data. (As created in Step #1)
    * `DEBUG` can be changed to True or False, depending on how verbose you want the output to be.

3. Once the file is ready, you can execute it. In the end, it will print all the rows that are added in `added` and all the rows that failed  in `notadded`. `notadded` will have the reason for the fail as well.

