from django.shortcuts import render
from django.db import connections
import requests
import json

from utils.dependencies_my import session_get, decode_nested_json_async
from .filter import MySpisokFilter
from django.http import JsonResponse
from datetime import datetime
import time
from django.conf import settings
# Create your views here.
LINK_FAST_API = settings.LINK_FAST_API


def decode_nested_json(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = decode_nested_json(value)
    elif isinstance(data, list):
        for i, value in enumerate(data):
            data[i] = decode_nested_json(value)
    elif isinstance(data, str):
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return data
    return data

from django.shortcuts import render
from .models import MySpisok

async def java_find_title(request):

    # if request.method == 'GET':
    #     query = request.GET.get('query')
    #     # dict_find = {}
    #     response_result = requests.get(f'http://127.0.0.1:8080/find/title?query={query}')
    #     dict_find = decode_nested_json(response_result.json()['result'])
    #     print(dict_find)
    #     return JsonResponse(dict_find, safe=False)

    if request.method == 'GET':
        # url_query = str(request.get_full_path)[str(request.get_full_path).find('?'):]
        # print(url_query, '\n\n\n\n\n\n\n')
        persons_filter = request.GET.getlist('person')
        query = request.GET.get('query')
        genre_id = request.GET.get('genre_id')
        country_id = request.GET.get('country_id')
        rate_to = request.GET.get('rate_to')
        rate_from = request.GET.get('rate_from')
        year_to = request.GET.get('year_to')
        year_from = request.GET.get('year_from')
        params = {}
        params['query'] = query
        params['genre_id']   = genre_id   if genre_id != '' else ''
        params['country_id'] = country_id if country_id != '' else ''
        params['rate_to']    = rate_to    if rate_to != '' else ''
        params['rate_from']  = rate_from  if rate_from != '' else ''
        params['year_to']    = year_to    if year_to != '' else ''
        params['year_from']  = year_from  if year_from != '' else ''
        params['persons']    = ''       if len(persons_filter) == 0 else ','.join(persons_filter)
        params['count_persons'] = len(persons_filter)
        response_result = await session_get(f'{LINK_FAST_API}/find/title', params=params)

        dict_find = response_result['ses_json']['result']
        return JsonResponse(dict_find ,safe=False)

def java_find_person(request):
    print("Person")
    if request.method == 'GET':
        query = request.GET.get('query')
        # dict_find = {}
        response_result = requests.get(f'{LINK_FAST_API}/find/person?query={query}')
        dict_find = decode_nested_json(response_result.json()['result'])
        return JsonResponse(dict_find, safe=False)

def find_main(request):
    query = request.GET.get('query')
    response_result = requests.get(f'{LINK_FAST_API}/find/title?query={query}')
    dict_find = {}
    if response_result.status_code == 200:
        dict_find['titles'] = decode_nested_json(response_result.json()['result'])
        return render(request, 'find_page/titles_list.html', dict_find | {'find_search':True, 'now_year': datetime.now().year})

    # return render(request, 'find_page/main_page.html')

async def find_mini(request):
    query = request.GET.get('query')
    print(query)
    start_time = time.time()
    response_result = await session_get(f'{LINK_FAST_API}/find/mini?query={query}')
    print(f"\n\n\n\nfind_mini {time.time() - start_time}\n\n\n\n")
    if response_result['status'] == 200:
        dict_find = response_result['ses_json']['result']
        return JsonResponse(dict_find, safe=False)