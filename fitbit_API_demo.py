import requests, json, datetime
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas
import config
from pprint import pprint

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

""" --- Example output --- 
{'activities-heart': [{'customHeartRateZones': [],
                       'dateTime': 'today',
                       'heartRateZones': [{'caloriesOut': 59.79114,
                                           'max': 99,
                                           'min': 30,
                                           'minutes': 56,
                                           'name': 'Out of Range'},
                                          {'caloriesOut': 0,
                                           'max': 138,
                                           'min': 99,
                                           'minutes': 0,
                                           'name': 'Fat Burn'},
                                          {'caloriesOut': 0,
                                           'max': 168,
                                           'min': 138,
                                           'minutes': 0,
                                           'name': 'Cardio'},
                                          {'caloriesOut': 0,
                                           'max': 220,
                                           'min': 168,
                                           'minutes': 0,
                                           'name': 'Peak'}],
                       'value': '65.95'}],
 'activities-heart-intraday': {'dataset': [{'time': '22:51:00', 'value': 63},
                                           {'time': '22:53:00', 'value': 64},
                                           {'time': '22:54:00', 'value': 66},
                                           {'time': '22:55:00', 'value': 63},
                                           {'time': '22:56:00', 'value': 63},
                                           {'time': '22:57:00', 'value': 63},
                                           {'time': '22:58:00', 'value': 64},
                                           {'time': '22:59:00', 'value': 65},
                                           {'time': '23:00:00', 'value': 63},
                                           {'time': '23:01:00', 'value': 60},
                                           {'time': '23:02:00', 'value': 66},
                                           {'time': '23:03:00', 'value': 64},
                                           {'time': '23:04:00', 'value': 57},
                                           {'time': '23:05:00', 'value': 58},
                                           {'time': '23:06:00', 'value': 62},
                                           {'time': '23:07:00', 'value': 55},
                                           {'time': '23:08:00', 'value': 65},
                                           {'time': '23:09:00', 'value': 68},
                                           {'time': '23:10:00', 'value': 70},
                                           {'time': '23:11:00', 'value': 68},
                                           {'time': '23:12:00', 'value': 64},
                                           {'time': '23:13:00', 'value': 72},
                                           {'time': '23:14:00', 'value': 70},
                                           {'time': '23:15:00', 'value': 71},
                                           {'time': '23:16:00', 'value': 70},
                                           {'time': '23:17:00', 'value': 67},
                                           {'time': '23:18:00', 'value': 62},
                                           {'time': '23:19:00', 'value': 64},
                                           {'time': '23:20:00', 'value': 76},
                                           {'time': '23:21:00', 'value': 78},
                                           {'time': '23:22:00', 'value': 72},
                                           {'time': '23:23:00', 'value': 78},
                                           {'time': '23:24:00', 'value': 76},
                                           {'time': '23:25:00', 'value': 76},
                                           {'time': '23:26:00', 'value': 77},
                                           {'time': '23:27:00', 'value': 76},
                                           {'time': '23:28:00', 'value': 82},
                                           {'time': '23:29:00', 'value': 76},
                                           {'time': '23:30:00', 'value': 66},
                                           {'time': '23:31:00', 'value': 65},
                                           {'time': '23:32:00', 'value': 69},
                                           {'time': '23:33:00', 'value': 63},
                                           {'time': '23:34:00', 'value': 62},
                                           {'time': '23:35:00', 'value': 65},
                                           {'time': '23:36:00', 'value': 63},
                                           {'time': '23:37:00', 'value': 62},
                                           {'time': '23:38:00', 'value': 62},
                                           {'time': '23:39:00', 'value': 62},
                                           {'time': '23:40:00', 'value': 59},
                                           {'time': '23:41:00', 'value': 61},
                                           {'time': '23:42:00', 'value': 56},
                                           {'time': '23:43:00', 'value': 61},
                                           {'time': '23:44:00', 'value': 60},
                                           {'time': '23:45:00', 'value': 59},
                                           {'time': '23:46:00', 'value': 63},
                                           {'time': '23:47:00', 'value': 61}],
                               'datasetInterval': 1,
                               'datasetType': 'minute'}}
   Time_Data  Heart_Rate_Data
0   22:51:00               63
1   22:53:00               64
2   22:54:00               66
3   22:55:00               63
4   22:56:00               63
5   22:57:00               63
6   22:58:00               64
7   22:59:00               65
8   23:00:00               63
9   23:01:00               60
10  23:02:00               66
11  23:03:00               64
12  23:04:00               57
13  23:05:00               58
14  23:06:00               62
15  23:07:00               55
16  23:08:00               65
17  23:09:00               68
18  23:10:00               70
19  23:11:00               68
20  23:12:00               64
21  23:13:00               72
22  23:14:00               70
23  23:15:00               71
24  23:16:00               70
25  23:17:00               67
26  23:18:00               62
27  23:19:00               64
28  23:20:00               76
29  23:21:00               78
30  23:22:00               72
31  23:23:00               78
32  23:24:00               76
33  23:25:00               76
34  23:26:00               77
35  23:27:00               76
36  23:28:00               82
37  23:29:00               76
38  23:30:00               66
39  23:31:00               65
40  23:32:00               69
41  23:33:00               63
42  23:34:00               62
43  23:35:00               65
44  23:36:00               63
45  23:37:00               62
46  23:38:00               62
47  23:39:00               62
48  23:40:00               59
49  23:41:00               61
50  23:42:00               56
51  23:43:00               61
52  23:44:00               60
53  23:45:00               59
54  23:46:00               63
55  23:47:00               61"""