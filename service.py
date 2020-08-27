# Endpoint
# https://api.coronavirus.data.gov.uk/v1/data

from uk_covid19 import Cov19API
import requests
import json
from demjson import decode
from update import Update

HEAD_URL = 'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation&structure={"name":"areaName"}'
LAST_MODIFIED = 'Last-Modified'

LATEST_BY_NEW_CASES = "newCasesByPublishDate"
ENGLAND_ONLY = [
    'areaType=nation',
    'areaName=England'
]
ALL_NATIONS = [
    'areaType=nation',
]
LONDON_REGION = [
    'areaType=region',
    'areaName=Cambridge'
]
CASES_AND_DEATHS_NATION = {
    "date": "date",
    "areaName": "areaName",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
    "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate"
}
CASES_AND_DEATHS_REGION = {
    "date": "date",
    "newCasesBySpecimenDate ": "newCasesBySpecimenDate ",
    "cumCasesBySpecimenDate ": "cumCasesBySpecimenDate "
}

def read_last_update():
    head = requests.head(HEAD_URL)
    #print(head)
    #print(head.headers)
    #head_decoded = decode(head)
    return head.headers['Last-Modified']

def convert_update_to_dict():
    nations = [
        {
            'date': Update.last_update,
            'name': Update.data_json['data'][0]['areaName'],
            'new_cases': Update.data_json['data'][0]['newCasesByPublishDate'],
            'total_cases': Update.data_json['data'][0]['cumCasesByPublishDate'],
            'new_deaths': Update.data_json['data'][0]['newDeaths28DaysByDeathDate'],
            'total_deaths': Update.data_json['data'][0]['cumDeaths28DaysByDeathDate']
        },
        {
            'date': Update.last_update,
            'name': Update.data_json['data'][1]['areaName'],
            'new_cases': Update.data_json['data'][1]['newCasesByPublishDate'],
            'total_cases': Update.data_json['data'][1]['cumCasesByPublishDate'],
            'new_deaths': Update.data_json['data'][1]['newDeaths28DaysByDeathDate'],
            'total_deaths': Update.data_json['data'][1]['cumDeaths28DaysByDeathDate']
        },
        {
            'date': Update.last_update,
            'name': Update.data_json['data'][2]['areaName'],
            'new_cases': Update.data_json['data'][2]['newCasesByPublishDate'],
            'total_cases': Update.data_json['data'][2]['cumCasesByPublishDate'],
            'new_deaths': Update.data_json['data'][2]['newDeaths28DaysByDeathDate'],
            'total_deaths': Update.data_json['data'][2]['cumDeaths28DaysByDeathDate']
        },
        {
            'date': Update.last_update,
            'name': Update.data_json['data'][3]['areaName'],
            'new_cases': Update.data_json['data'][3]['newCasesByPublishDate'],
            'total_cases': Update.data_json['data'][3]['cumCasesByPublishDate'],
            'new_deaths': Update.data_json['data'][3]['newDeaths28DaysByDeathDate'],
            'total_deaths': Update.data_json['data'][3]['cumDeaths28DaysByDeathDate']
        }
    ]
    return nations

def get_nations_data():
    current_update = read_last_update()

    if Update.last_update == '' or  Update.last_update != current_update:
        api_all_nation_latest = Cov19API(filters=ALL_NATIONS, structure=CASES_AND_DEATHS_NATION,
                                            latest_by=LATEST_BY_NEW_CASES)
        Update.data_json = api_all_nation_latest.get_json()
        api_all_nation_latest.get_json(save_as="tmp\data_all_nation.json")
        Update.last_update = current_update
        #print(Update.last_update)
        #print(Update.data_json)

    print(convert_update_to_dict())
    return convert_update_to_dict()


#print(Update.data_json['data'][0])



# api_england_alltimes = Cov19API(filters=england_only, structure=cases_and_deaths)
# api_all_latest = Cov19API(filters=all_nations, structure=cases_and_deaths, latest_by="newCasesByPublishDate")
# api_london_region_latest = Cov19API(filters=all_nations, structure=cases_and_deaths_nation, latest_by="newCasesByPublishDate")

# data = api_london_region_latest.get_json()

# api_timestamp = api_all_latest.last_update
#release_timestamp = Cov19API.get_release_timestamp()  # static method

# print(api_timestamp)
#print(release_timestamp)

#print(json.dumps(Update.data_json['data'][0], indent=4, sort_keys=True))

