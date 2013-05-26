[Device42](http://www.device42.com/) is a comprehensive data center management software.

This repository hosts a python script to easily input data to device42 appliance via APIs.


### Script Provided
-----------------------------
   * csv2d42apis.py : Reads a CSV file, matches columns to arguments for APIs and sends data to device42 via POST or PUT.

### Requirement
-----------------------------
   * Python. Tested with python 2.7.x
   * If you don't have python installed already, you can download and install from: [http://www.python.org/download/releases/](http://www.python.org/download/releases/)


### Usage
-----------------------------

This sample script can be easily modified to read a comma-delimited csv file of data for any of the API's supported by device42 and documented at: [http://docs.device42.com/api/](http://docs.device42.com/api/).

Example script uses the API to add/update custom key/values for application components as documented at: [http://docs.device42.com/apis/application-component-custom-field-apis/](http://docs.device42.com/apis/application-component-custom-field-apis/)

1. From the documentation, determine which API call you need to use.

2. From the documentation of the API call, note the URL (e.g. /api/1.0/custom_fields/appcomp/) and the URL method (either PUT or POST).

3. From the documentation of the API call, identity the mandatory fields you must include and the optional fields you wish to include.

4. Create comma separated CSV file with following:
    * The header row (first line) values must match the API field names found in the documentation.
    * After the header row, there should be one row of values for each data record that you need to send to the device42 appliance.
    * Each line in the CSV file must have a value for each mandatory field.

5. You will need to Change lines 26-31 in the script to match your environment:
    * `D42_API_URL` will be the d42 instance base url plus the api call url that you found in the API documentation.
    * `D42_USERNAME` and `D42_PASSWORD` are self explanatory.
    * `API_METHOD` will be put or post, depending on the documentation for the particular API.
    * `CSV_FILE_NAME` will be the name of the csv file with data. (As created in Step #4)
    * `DEBUG` can be changed to True or False, depending on how verbose you want the output to be.

6. Once the file is ready, you can execute it. After the script completes, it will print two sections of information:  The 'added' section will show all the rows that were added successfully.  The `notadded` section will have any rows that failed and the reason for the failure.
