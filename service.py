# Endpoint
# https://api.coronavirus.data.gov.uk/v1/data

from uk_covid19 import Cov19API
import requests
from datetime import datetime
import json
#from demjson import decode
from update import Update
from comment import Comment
from CovidData import CovidData

HEAD_URL = 'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation&structure={"name":"areaName"}'
LAST_MODIFIED = 'Last-Modified'

LATEST_BY_NEW_CASES = "newCasesByPublishDate"
UK = [
    'areaType=overview',
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
    return head.headers[LAST_MODIFIED]

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


def convert_update_to_obj():
    uk = []
    json_list_uk = Update.data_json_uk['data']
    for d in json_list_uk:
        covid_data_obj = CovidData(d['date'],
                                   d['areaName'],
                                   d['newCasesByPublishDate'],
                                   d['cumCasesByPublishDate'],
                                   d['newDeaths28DaysByDeathDate'],
                                   d['cumDeaths28DaysByDeathDate'])
        uk.append(covid_data_obj)

    en = []
    sco = []
    wa = []
    ni = []
    json_list = Update.data_json['data']
    for d in json_list:
        covid_data_obj = CovidData(d['date'],
                                   d['areaName'],
                                   d['newCasesByPublishDate'],
                                   d['cumCasesByPublishDate'],
                                   d['newDeaths28DaysByDeathDate'],
                                   d['cumDeaths28DaysByDeathDate'])
        if d['areaName'] == 'England':
            en.append(covid_data_obj)
        if d['areaName'] == 'Scotland':
            sco.append(covid_data_obj)
        if d['areaName'] == 'Wales':
            wa.append(covid_data_obj)
        if d['areaName'] == 'Northern Ireland':
            ni.append(covid_data_obj)

    covid_data_list = [uk, en, sco, wa, ni]
    return covid_data_list

def get_nations_data():
    current_update = read_last_update()

    if Update.last_update == '' or  Update.last_update != current_update:
        api_all_nation = Cov19API(filters=ALL_NATIONS, structure=CASES_AND_DEATHS_NATION)
        api_uk_overview = Cov19API(filters=UK, structure=CASES_AND_DEATHS_NATION)
        Update.data_json = api_all_nation.get_json()
        Update.data_json_uk = api_uk_overview.get_json()
        api_all_nation.get_json(save_as="tmp\data_all_nation.json")
        Update.last_update = current_update
        release_timestamp = Cov19API.get_release_timestamp()
        Update.release_date = datetime.fromisoformat(release_timestamp.strip("Z")).strftime("%d.%m.%Y %H:%M:%S")
        print(datetime.now())
        print(Update.release_date)
    return convert_update_to_obj()


def create_comment(request):
    time = datetime.strptime(str(datetime.now().replace(microsecond=0)), '%Y-%m-%d %H:%M:%S')
    text = request.form['comment']
    url = request.remote_addr
    comment = Comment(time,
                      'Anonymous',
                      url,
                      text,
                      'no',
                      'no')
    print(comment)
    return comment



















#api_all_nation = Cov19API(filters=ALL_NATIONS, structure=CASES_AND_DEATHS_NATION)
#Update.data_json = api_all_nation.get_json()
#x = convert_update_to_obj()
#print(x[0])



#api_all_nation = Cov19API(filters=ALL_NATIONS, structure=CASES_AND_DEATHS_NATION)
#list = api_all_nation.get_json()['data']
#print(list[0])
#print(api_all_nation.get_json())
#print(json.dumps(api_all_nation.get_json()['data'][0], indent=4, sort_keys=True))


# api_england_alltimes = Cov19API(filters=england_only, structure=cases_and_deaths)
# api_all_latest = Cov19API(filters=all_nations, structure=cases_and_deaths, latest_by="newCasesByPublishDate")
# api_london_region_latest = Cov19API(filters=all_nations, structure=cases_and_deaths_nation, latest_by="newCasesByPublishDate")

# data = api_london_region_latest.get_json()

# api_timestamp = api_all_latest.last_update
#release_timestamp = Cov19API.get_release_timestamp()  # static method

# print(api_timestamp)
#print(release_timestamp)

#print(json.dumps(Update.data_json['data'][0], indent=4, sort_keys=True))

