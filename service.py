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


def convert_update_to_obj():
    id = 0
    uk = []
    json_list_uk = Update.data_json_uk['data']
    for d in json_list_uk:
        covid_data_obj = CovidData(id,
                                   d['date'],
                                   d['areaName'],
                                   d['newCasesByPublishDate'],
                                   d['cumCasesByPublishDate'],
                                   d['newDeaths28DaysByDeathDate'],
                                   d['cumDeaths28DaysByDeathDate'])
        replace_none_with_nodata(covid_data_obj)
        id = id + 1
        uk.append(covid_data_obj)

    en_id = 0
    sco_id = 0
    wa_id = 0
    ni_id = 0
    en = []
    sco = []
    wa = []
    ni = []
    json_list = Update.data_json['data']
    for d in json_list:
        covid_data_obj = CovidData(id,
                                   d['date'],
                                   d['areaName'],
                                   d['newCasesByPublishDate'],
                                   d['cumCasesByPublishDate'],
                                   d['newDeaths28DaysByDeathDate'],
                                   d['cumDeaths28DaysByDeathDate'])

        if d['areaName'] == 'England':
            covid_data_obj.id = en_id
            replace_none_with_nodata(covid_data_obj)
            en_id = en_id + 1
            en.append(covid_data_obj)
        if d['areaName'] == 'Scotland':
            covid_data_obj.id = sco_id
            replace_none_with_nodata(covid_data_obj)
            sco_id = sco_id + 1
            sco.append(covid_data_obj)
        if d['areaName'] == 'Wales':
            covid_data_obj.id = wa_id
            replace_none_with_nodata(covid_data_obj)
            wa_id = wa_id + 1
            wa.append(covid_data_obj)
        if d['areaName'] == 'Northern Ireland':
            covid_data_obj.id = ni_id
            replace_none_with_nodata(covid_data_obj)
            ni_id = ni_id + 1
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
        #print(datetime.now())
        #print(Update.release_date)
        Update.data_obj_list = convert_update_to_obj()
        print('inside service.get_nations_data()')
    return Update.data_obj_list


def create_comment(request):
    time = datetime.strptime(str(datetime.now().replace(microsecond=0)), '%Y-%m-%d %H:%M:%S')
    text = request.form['comment']
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        url = request.environ['REMOTE_ADDR']
    else:
        url = request.environ['HTTP_X_FORWARDED_FOR']
    comment = Comment(time, 'anonymous', url, text, 'no', 'no')
    #print(comment)
    return comment


def replace_none_with_nodata(covid_data_obj):
    #if covid_data_obj.id < 30:
    if covid_data_obj.new_cases is None:
        covid_data_obj.new_cases = 'no data'
    if covid_data_obj.total_cases is None:
        covid_data_obj.total_cases = 'no data'
    if covid_data_obj.new_deaths is None:
        covid_data_obj.new_deaths = 'no data'
    if covid_data_obj.total_deaths is None:
        covid_data_obj.total_deaths = 'no data'
    return covid_data_obj
















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

