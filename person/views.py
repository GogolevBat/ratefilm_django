from django.shortcuts import render
from django.http import JsonResponse
import json, time
import requests
from django.conf import settings
from asgiref.sync import sync_to_async

from utils.dependencies_my import *

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

async def person_show(request, person_id):
    user = await request.auser()
    user_id = user.id
    print(f'user id {user_id}')
    start_time = time.time()
    response_result = await session_get(f'{LINK_FAST_API}/person/{person_id}?user_id={user_id}')
    print(f"end {time.time() - start_time}")
    if response_result['status'] == 200:
        print("http 200")
        dict_person = response_result['ses_json']['result']
        # print(dict_person)
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'person/person_show.html', dict_person)

async def person_favorite_it(request, person_id):
    user = await request.auser()
    user_id = user.id
    if request.method == 'POST':
        response_result = await session_post(f'{LINK_FAST_API}/person/favoriteit/{person_id}?user_id={user_id}')
        print(response_result.status)
        if response_result.status == 200:
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False})


async def person_favorite_out(request, person_id):
    user = await request.auser()
    user_id = user.id
    if request.method == 'POST':
        response_result = await session_post(f'{LINK_FAST_API}/person/favoriteout/{person_id}?user_id={user_id}')
        print(response_result.status)
        if response_result.status == 200:
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False})


async def person_show_mini(request, person_id):

    response_result = await session_get(f'{LINK_FAST_API}/person/mini/{person_id}')
    if response_result['status'] == 200:
        dict_person = response_result['ses_json']['result']
        return JsonResponse(dict_person, safe=False)
