'''
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

##############################################
# csv file to api helper utility
# create csv, match the column values with arguments in changerow_to_api_args function call
# and upload data to device42 via REST APIs
##############################################
import types
import urllib2
import urllib
import base64
import csv

##### Change Following lines to match your environment #####
d42url = 'https://your-d42-url-here'
urluser = 'your-d42-username-here'
urlpass = 'your-d42-password-here'

def post(url, method, params):
    result = ''
    try:
        data= urllib.urlencode(params)
        headers = {
            'Authorization' : 'Basic '+ base64.b64encode(urluser + ':' + urlpass),
            'Content-Type' : 'application/x-www-form-urlencoded'
        }

        req = urllib2.Request(url, data, headers)

        print '---REQUEST---',req.get_full_url()
        print req.headers
        print req.data

        if method == 'put': req.get_method = lambda: 'PUT'

        reponse = urllib2.urlopen(req)

        print '---RESPONSE---'
        print reponse
        result = str(reponse.read())
    except Exception, Err:
        print '-----EXCEPTION OCCURED-----'
        print str(Err)
    return result

def to_ascii(s): #not used in example, but provided incase you would need to convert certain values to ascii
    """remove non-ascii characters"""
    if type(s) == types.StringType:
        return s.encode('ascii','ignore')
    else:
        return str(s)


def changerow_to_api_args(row_values):
    #map each row value to corresponding API argument.
    #row index starts from zero.
    #change this to match your CSV column values to API arguments to map to.
    #following example is for application component custom key pair values.
    #csv file columns are: application component name, key, value, value2, show on chart, notes
    #mapping index would be:  0                     , 1    , 2,     3,      4,              5
    #in this example, since row_values[0] and row_values[1] are required, we would raise exception if these are empty.
    if not row_values[0] or not row_values[1]: raise Exception('Required Parameter Missing')
    #create a dictionary from values, that can be passed to api call.
    args = {'name': row_values[0], 'key': row_values[1]}
    if row_values[2]: args.update({'value': row_values[2]})
    if row_values[3]: args.update({'value2': row_values[3]})
    if row_values[4]: args.update({'show_on_chart': row_values[4]})
    if row_values[5]: args.update({'notes': row_values[5]})
    return args

def read_csv_parse_and_call_api_function(filename):
    #API url. Checks if there is ending / in the original url.
    if d42url[:-1] == '/':
        API_URL = d42url + 'api/1.0/custom_fields/appcomp/'
    else:
        API_URL = d42url + '/api/1.0/custom_fields/appcomp/'
    API_METHOD = 'put' #whether you are doing a put or post call.
    notadded = []
    added = []
    with open(filename, 'rb') as csvfile:
        ReadLine = csv.reader(csvfile)

        ReadLine.next() #skip the header row.
        for i in ReadLine:
            if i != []:
                try:
                    args = changerow_to_api_args(i)
                    post(API_URL, API_METHOD, args)
                    added.append(i)
                except Exception, Err:
                    notadded.append(i+[str(Err),])
    print 'notadded %s' % notadded
    print 'added %s' % added

read_csv_parse_and_call_api_function('file_name.csv') #the actual call with the csv file name.
