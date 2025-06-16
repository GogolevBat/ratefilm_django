from datetime import datetime
import aiohttp
from django.http import JsonResponse
from django.shortcuts import render, redirect
from asgiref.sync import sync_to_async

import requests
from django.conf import settings
import time
import random

from utils.dependencies_my import *

LINK_FAST_API = settings.LINK_FAST_API




def title_show(request, title_id):
    user_id = request.user.id
    response_result =  requests.get(f'{LINK_FAST_API}/title/{title_id}?user_id={user_id}')
    # print(response_result.status_code)
    if response_result.status_code == 200:
        dict_title =  decode_nested_json(json.loads(response_result.json()['result']))
        return render(request, 'title/show.html', dict_title)


async def title_wshow(request, title_id):
    user = await request.auser()
    user_id = user.id
    async with aiohttp.ClientSession() as session:
        response_result = await session.get(f"{LINK_FAST_API}/title/{title_id}?user_id={user_id}")
        result = await response_result.json()
        dict_render = (await decode_nested_json_async(result['result'])) | {'user_id': user_id, 'user_auth': True if user_id else False}
    render_async = sync_to_async(render, thread_sensitive=True)
    return await render_async(request, 'title/show.html', dict_render)
async def index(request):
    print(f"\n\n\n\n\n{datetime.now().strftime('%y:%m:%D %H-%M-%S')} menu\n\n\n\n\n")
    user = await request.auser()
    user_id = user.id

    if request.GET.get('update'):
        response_result = await session_get(f'{LINK_FAST_API}/menu/{user_id}/update')
        return redirect('/')

    render_async = sync_to_async(render, thread_sensitive=True)
    response_result = await session_get(f'{LINK_FAST_API}/menu/{user_id}')
    if response_result['status'] == 200:
        result = response_result['ses_json']

        # print(result)
        data_menu = result['result'] | {'is_menu':True}
                           # ' await decode_nested_json_async(result[')result'])
        random.shuffle(data_menu['contents_for_menu'])
        print()
        return await render_async(request, 'main_menu/basement.html', data_menu)
    return await render_async(request, 'main_menu/basement.html')



def index_old(request):
    print(f"\n\n\n\n\n{datetime.now().strftime('%y:%m:%D %H-%M-%S')} menu\n\n\n\n\n")
    user_id = request.user.id
    start_req = time.time()
    if request.GET.get('update'):
        time_st = time.time()
        response_result = requests.get(f'{LINK_FAST_API}/menu/{user_id}/update')
        # print(f"\n\n\nредирект {time.time() - time_st}\n\n\n")
        return redirect('/')
    response_result = requests.get(f'{LINK_FAST_API}/menu/{user_id}')
    # print("\n\n\n\n\n Запрос: ",time.time()-start_req)

    if response_result.status_code == 200:
        time_start = time.time()
        # print(response_result.json())
        data_menu = decode_nested_json(response_result.json()['result'])
        # print('Разархивация',time.time()-time_start, '\n\n\n\n')

        # print(data_menu['person_test'])
        # print(data_menu['titles_on_user_top_genre'])
        # print(data_menu['contents_for_menu'])
        random.shuffle(data_menu['contents_for_menu'])

        return render(request, 'main_menu/basement.html', data_menu | {'is_menu':True})
    return render(request, 'main_menu/basement.html')

async def add_content_on_menu(request):
    user = await request.auser()
    user_id = user.id
    response_result = await session_get(f'{LINK_FAST_API}/menu/add/content/{user_id}')
    if response_result['status'] == 200:
        data_menu = response_result['ses_json']['result']
        return JsonResponse(data_menu)

#"<h4 style='text-align: center'>Hello World!</h4>"

async def about(request):
    render_async = sync_to_async(render, thread_sensitive=True)
    return await render_async(request, 'main_menu/about.html')

def main_page(request):
    from django.db import connections
    kp_con = connections['Kinopoisk_db']
    with kp_con.cursor() as cursor:
        cursor.execute(f"""select name, photo, enname, age, sex, growth from persons where id = 0 """)
        res_person = cursor.fetchall()

async def pined(request):
    # request.GET("")
    user = await request.auser()
    user_id = user.id
    response_result = await session_get(f'{LINK_FAST_API}/menu/showpin?user_id={user_id}')
    # print(response_result.status_code)
    if response_result['status'] == 200:
        dict_title = {'titles': response_result['ses_json']['result']}
        dict_render = dict_title
        # print(dict_render)
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'main_menu/pined_page.html', dict_render)

async def viewed(request):
    # request.GET("")
    user = await request.auser()
    user_id = user.id
    response_result = await session_get(f'{LINK_FAST_API}/menu/viewed?user_id={user_id}')
    # print(response_result.status_code)
    if response_result['status'] == 200:
        dict_title = {'titles': response_result['ses_json']['result']}
        dict_render = dict_title
        # print(dict_render)
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'main_menu/viewed_page.html', dict_render)

async def favorited(request):
    # request.GET("")
    user = await request.auser()
    user_id = user.id
    response_result = await session_get(f'{LINK_FAST_API}/menu/favorited?user_id={user_id}')

    if response_result['status'] == 200:
        dict_title = {'titles': response_result['ses_json']['result']}
        dict_render = dict_title

        # print(dict_render)
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'main_menu/favorite_page.html', dict_render)

