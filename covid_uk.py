#from uk_covid19 import Cov19API
from requests import get
from json import dumps
import json


ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
AREA_TYPE = "nation"
AREA_NAME = "england"

filters = [
    'areaType=overview'
]

structure = {
    "date":"date",
    "areaName":"areaName",
    "areaCode":"areaCode",
    "newCasesByPublishDate":"newCasesByPublishDate",
    "cumCasesByPublishDate":"cumCasesByPublishDate",
    "newDeaths28DaysByDeathDate":"newDeaths28DaysByDeathDate",
    "cumDeaths28DaysByDeathDate":"cumDeaths28DaysByDeathDate"
}


api_params = {
    "filters": str.join(";", filters),
    "structure": dumps(structure, separators=(",", ":")),
    "latestBy": "cumCasesByPublishDate"
}


formats = [
    "json",
    "xml",
    "csv"
]


def covid_uk():
    api_params["format"] = "json"
    response = get(ENDPOINT, params=api_params, timeout=10)
    json_data = response.content.decode()
    covid_dict = json.loads(json_data)
    result = covid_dict
    c_date = str(covid_dict['data'][0]['date'])
    c_area = str(covid_dict['data'][0]['areaName'])
    c_new_cases = str(covid_dict['data'][0]['newCasesByPublishDate'])
    c_cumulative_cases = str(covid_dict['data'][0]['cumCasesByPublishDate'])
#    c_new_deaths = str(covid_dict['data'][0]['newDeaths28DaysByDeathDate'])
#    c_cumulative_deaths = str(covid_dict['data'][0]['cumDeaths28DaysByDeathDate'])
    result = '<h3>COVID19, dane dla Wielkiej Brytanii</h3>'
    result = result + '<p>Data: ' + c_date + '</p>'
    result = result + '<p>Obszar: ' + c_area + '</p>'
    result = result + '<p>Liczba nowych zachorowan (dzienna): ' + c_new_cases + '</p>'
    result = result + '<p>Liczba dotychczasowych zachorowan (kumulacja): ' + c_cumulative_cases + '</p>'
    result = result + '<br><br><span>by latitude99</span>'
    return result


#print(covid_obj())




#{'length': 1, 'maxPageLimit': 1, 'data': [{'date': '2020-08-23',
#                                           'areaName': 'United Kingdom',
#                                           'areaCode': 'K02000001',
#                                           'newCasesByPublishDate': 1041,
#                                           'cumCasesByPublishDate': 325642,
#                                           'newDeaths28DaysByDeathDate': None,
#                                           'cumDeaths28DaysByDeathDate': None}]}