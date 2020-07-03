import requests, json, datetime
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas
import config
from pprint import pprint

# more info on the sdk here- https://dev.fitbit.com/

CLIENT_ID = getattr(config, 'FITBIT_CLIENT_ID', 'default value if not found')
ACCESS_TOKEN = getattr(config, 'FITBIT_ACCESS_TOKEN', 'default value if not found')
REFRESH_TOKEN = getattr(config, 'FITBIT_REFRESH_TOKEN', 'default value if not found')
REDIRECT_URI = getattr(config, 'FITBIT_REDIRECT_URI', 'default value if not found')
GRANT_TYPE = getattr(config, 'FITBIT_GRANT_TYPE', 'default value if not found')
CODE = getattr(config, 'FITBIT_CODE', 'default value if not found')
TOKEN_ENDPOINT = getattr(config, 'FITBIT_TOKEN_ENDPOINT', 'default value if not found')
headers = getattr(config, 'FITBIT_headers', 'default value if not found')

def get_token(code):
        data = {"clientId":CLIENT_ID,
                "grant_type":GRANT_TYPE,
                "redirect_uri": REDIRECT_URI,
                "code": CODE}
        pprint(requests.post(TOKEN_ENDPOINT, headers=headers, data=data).json())

def refresh_token(ref_token):
        data = {"grant_type":"refresh_token",
                "refresh_token":ref_token}
        endpoint = "https://api.fitbit.com/oauth2/token"
        pprint(requests.post(url=endpoint, data=data, headers=headers).json())

def personal():
        headers = {"Authorization":"Bearer "+ACCESS_TOKEN}
        url = "https://api.fitbit.com/1/user/-/profile.json"
        pprint(requests.get(url=url, headers=headers).json())

def activities():
        headers = {'Authorization': 'Bearer ' +ACCESS_TOKEN}
        url = 'https://api.fitbit.com/1/user/-/activities/date/today.json'
        pprint(requests.get(url=url, headers=headers).json())

def get_heart_rate_data():
        # example endpoints
        #url = 'https://api.fitbit.com/1/user/[user-id]/activities/heart/date/[base-date]/[end-date].json'
        #url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/today/1min.json'

        # format dates/times I might use to get different sets of Heart Rate data 
        yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
        yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
        today = str(datetime.datetime.now().strftime("%Y%m%d"))
        base_date = yesterday2
        headers = {'Authorization': 'Bearer ' +ACCESS_TOKEN}
        NOW_HOUR = int(str(datetime.datetime.now().time()).split(':')[0])
        NOW_MIN = int(str(datetime.datetime.now().time()).split(':')[1])
        PAST_HOUR = NOW_HOUR-1

        # Handle the midnight case by capping it to 0
        if PAST_HOUR < 0:
                PAST_HOUR = 0

        # format the endpoint url
        url='https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min/time/' + str(PAST_HOUR) +':' + str(NOW_MIN) +'/' +str(NOW_HOUR) +':'+ str(NOW_MIN)+'.json'
        
        # issue the request 
        r = requests.get(url=url, headers=headers).json()

        # pretty print the json to console
        pprint(r)

        # interested in the heart rate data set
        data_set = r['activities-heart-intraday']['dataset']

        # build two lists to store time and heart rate (HR from here out) data 
        time=[]
        hr=[]
        line_ctr = 0
        for line in data_set:
                time.append(line['time'])
                hr.append(line['value'])

        # set up the data on a Pandas data frame 
        Data = {'Time_Data': time, 'Heart_Rate_Data': hr}
        df = DataFrame(Data,columns=['Time_Data', 'Heart_Rate_Data'])

        # show the data set
        print (df)

        # convert the time so it can be graphed
        df['Time_Data'] = pandas.to_datetime(df['Time_Data'])
        df.plot(x='Time_Data', y ='Heart_Rate_Data', kind = 'line')
        
        # show graph 
        plt.show()

        return [time, hr]


get_heart_rate_data()

