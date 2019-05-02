import requests
import json
from apikeys import w_apikey

class weatherInstance():
    def __init__(self, q = 'mansoura, egypt'):
        self.q = q
        try:
            payload = {
                        'q': f'{self.q}',
                        'key': w_apikey,
                        'format': 'json'
                        }
            self.data = requests.get('http://api.worldweatheronline.com/premium/v1/weather.ashx', params=payload)
            self.datas = self.data.json()
        except Exception as e:
            print(e)
            print(self.data.url)

    def check(self):
        try:
            print(self.datas['data']['request'][0]['query'])
        except KeyError as k:
            if (self.datas['data']['error'][0]['msg'] == 'Unable to find any matching weather location to the query submitted!'):
                print("Wrong location city dude xD")
                return False
            print(self.datas)
        except Exception as e:
            print(e)
            print(self.data.url)

    def checkCurrent(self):
        self.check()
        print(self.datas['data']['current_condition'][0]['temp_C'],
                self.datas['data']['current_condition'][0]['uvIndex'])
    def checkToday(self):
        self.check()
        print(self.datas['data']['weather'][0]['maxtempC'],
                self.datas['data']['weather'][0]['mintempC'],
                self.datas['data']['weather'][0]['uvIndex'],)
instance1 = weatherInstance('damietta' + ', egypt')
instance2 = weatherInstance()
instance3 = weatherInstance('alexandria' + ', egypt')
instance1.checkToday()
instance2.checkToday()
instance3.checkCurrent()

# api_token = 'your_api_token'
# api_url_base = 'https://api.digitalocean.com/v2/'
# http://api.worldweatheronline.com/premium/v1/weather.ashx?q=mansoura,+egypt&key=47a17e6806304beb86d331211921&format=json
# print(datas['current_condition'])
#
# JSON{}
#     data{}
#         request[0]{}
#             type
#             query
#         current_condition[0]{}
#             observation_time
#             temp_C
#             weatherIconUrl[0]{}
#                 value
#             humidity
#             cloudcover
#             uvIndex
#         weather[0~13]
#             maxtempC
#             mintempC
#             uvIndex
#             hourly[0~7]{}
#                 temp_C
#                 weatherIconUrl[0]{}
#                     value
#                 humidity
#                 cloudcover
#                 uvIndex
