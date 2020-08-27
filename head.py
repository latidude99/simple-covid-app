import requests
import json
from demjson import decode



#x = requests.head('https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation&structure={"name":"areaName"}')

#print(x.headers)

with open('tmp/head_single.json', 'r') as json_file_single:
    data = json_file_single.read()#.replace('\'', '\"')
#    head = json.loads(data)
    head = decode(data)

print(head['Last-Modified'])



#print(json.dumps(head['head'][0], indent=4, sort_keys=True))


