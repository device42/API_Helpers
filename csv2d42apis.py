'''
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

############################################################################################
# csv file to api helper utility v2.1 that uploads data to device42 via REST APIs
# step 1: create csv file, comma separated, header row must match the arguments for the API call.
# step 2: Change lines 26-31
# step 3: Execute the script
############################################################################################
import urllib2
import urllib
import base64
import csv

##### Change Following lines to match your environment #####
### API URLS available at http://docs.device42.com/apis/ ###

D42_API_URL = 'https://your-d42-fqdn-or-ip/api/1.0/custom_fields/appcomp/'  # make sure to end in /
D42_USERNAME = 'your-d42-username-here'
D42_PASSWORD = 'your-d42-password-here'
API_METHOD = 'put'                                                          # whether you are doing a put or post call.
CSV_FILE_NAME = 'file_name.csv'                                             # name of the file with the values being uploaded
DEBUG = True                                                                # True or False. True for detailed info per call


def post(params):
    data = urllib.urlencode(params)
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(D42_USERNAME + ':' + D42_PASSWORD),
        'Content-Type': 'application/x-www-form-urlencoded'}
    req = urllib2.Request(D42_API_URL, data, headers)
    if DEBUG:
        print '---REQUEST---', req.get_full_url()
    if DEBUG:
        print req.headers
    if DEBUG:
        print req.data
    if API_METHOD == 'put':
        req.get_method = lambda: 'PUT'
    try:
        urllib2.urlopen(req)
        return True, ''
    except urllib2.HTTPError, httperror:
        error_response = httperror.read()
        if DEBUG:
            print httperror.code, error_response
        return False, error_response


def to_ascii(string):  # not used in example, but provided incase you would need to convert certain values to ascii
    """remove non-ascii characters"""
    if isinstance(string, basestring):
        return string.encode('ascii', 'ignore')
    else:
        return str(string)


def changerow_to_api_args(row_values, header_row):
    args = {}
    for i, heading in enumerate(header_row):
        if row_values[i]:
            args.update({heading.strip().lower(): row_values[i].strip()})
    return args


def read_csv_and_call_api_function(filename):
    notadded = []
    added = []
    with open(filename, 'rb') as csvfile:
        readline = csv.reader(csvfile)
        header_row = readline.next()
        for i in readline:
            if i:
                try:
                    args = changerow_to_api_args(i, header_row)
                    added, msg = post(args)
                    if added:
                        added.append(i)
                    else:
                        notadded.append(i + [' ', msg])
                except Exception, err:
                    notadded.append(i + [str(err), ])
    print 'notadded %s' % notadded
    print 'added %s' % added


read_csv_and_call_api_function(CSV_FILE_NAME)
