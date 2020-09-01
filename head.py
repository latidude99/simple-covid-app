import requests
import json
from demjson import decode
from datetime import datetime
from datetime import timedelta
from uk_covid19 import Cov19API


#x = requests.get('https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation;areaName=england&structure={%22date%22:%22date%22,%22areaName%22:%22areaName%22,%22areaCode%22:%22areaCode%22,%22newCasesByPublishDate%22:%22newCasesByPublishDate%22,%22cumCasesByPublishDate%22:%22cumCasesByPublishDate%22,%22newDeaths28DaysByDeathDate%22:%22newDeaths28DaysByDeathDate%22,%22cumDeaths28DaysByDeathDate%22:%22cumDeaths28DaysByDeathDate%22}')
#x = requests.head('https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation&structure={"name":"areaName"}')

#print(x.headers)

#with open('tmp/head_single.json', 'r') as json_file_single:
#    data = json_file_single.read()#.replace('\'', '\"')
#    head = json.loads(data)
#    head = decode(data)

#print(head['Last-Modified'])



#print(json.dumps(head['head'][0], indent=4, sort_keys=True))

#HEAD_URL = 'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation&structure={"name":"areaName"}'
#head = requests.head(HEAD_URL)
    #print(head)
    #print(head.headers)
    #head_decoded = decode(head)

# head.headers['Last-Modified']
#print(head.headers['Last-Modified'])

#print(json.dumps(x.json(), indent=4, sort_keys=True))

release_timestamp = Cov19API.get_release_timestamp()
release_time = str(datetime.fromisoformat(release_timestamp.strip("Z")).replace(microsecond=0))
current_time = str(datetime.now().replace(microsecond=0))
print(release_time)
print(current_time)

#diff = current_time - current_time
#print(diff.min)

format = '%Y-%m-%d %H:%M:%S'
d1 = datetime.strptime(current_time, format)
d2 = datetime.strptime(release_time, format)
delta = d1 - d2

print(delta.total_seconds())



#datetime.fromisoformat(release_timestamp.strip("Z")).strftime("%d.%m.%Y %H:%M:%S")
















