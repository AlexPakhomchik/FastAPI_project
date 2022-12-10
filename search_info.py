from fastapi import APIRouter
import requests


search_info = APIRouter(prefix='/search_info', tags=['search_info'])


@search_info.get("/")
def date_number():
    return {'settings': {'search_info': 'str'}}


@search_info.get("/{search_query}")
def date_number(search_query: str):
    data = requests.get(f'https://images-api.nasa.gov/search?q={search_query}&year_start=2022').json()
    total_result = {}
    try:
        for i in range(len(data['collection']['items'])):
            if data['collection']['items'][i]['links'][0]['href'][-3:] == 'jpg':
                total_result[int(i)] = data['collection']['items'][i]['links'][0]['href']
    except KeyError:
        pass
    return total_result
