[Device42](http://www.device42.com/) is a comprehensive data center management software.

This repository hosts a python script to easily input data to device42 appliance via APIs.


### Script Provided
-----------------------------
   * csv2d42apis.py : Reads a CSV file, matches columns to arguments for APIs and sends data to device42 via POST or PUT.


### Usage
-----------------------------

You will need to Change the following 2 sections in the script to match your environment and csv file columns.
This is assuming you have the csv file ready with data to send to device42.

1. Enter your device42 appliance url, credentials and the url for the API call.
    * `D42_API_URL` will be the d42 instance base url plus the api call url. API call urls available at: [http://docs.device42.com/api/](http://docs.device42.com/api/)
    * `D42_USERNAME` and `D42_PASSWORD` are self explanatory.
    * `API_METHOD` will be put or post, depending on the call. (As found in documentation linked above)
    * `CSV_FILE_NAME` will be the name of the csv file with data.
    * `DEBUG` can be changed to True or False, depending on how verbose you want the output to be.

2. Match the CSV columns to corresponding API argument(in function `changerow_to_api_args`).
    * CSV indexes are zero based.
    * e.g. `args = {'name': row_values[0], 'key': row_values[1]}` assumes first column is name and second column is key.
    * use `if row_values[x]` if the given field might be empty for certain rows.

Once the file is ready, you can execute it. In the end, it will print all the rows that are added in `added` and all the rows that failed  in `notadded`. `notadded` will have the reason for the fail as well.