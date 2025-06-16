from asgiref.sync import sync_to_async
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from utils.dependencies_my import *

LINK_FAST_API = settings.LINK_FAST_API


async def title_show(request, title_id):
    user = await request.auser()
    user_id = user.id

    response_result = await session_get(f"{LINK_FAST_API}/title/{title_id}?user_id={user_id}")
    result = response_result['ses_json']
    dict_render = result['result'] | {'user_id': user_id, 'user_auth': True if user_id else False}

    render_async = sync_to_async(render, thread_sensitive=True)
    return await render_async(request, 'title/show.html', dict_render)

    # return render(request, 'universe/basre.html')
    # user_id = request.user.id
    # start_req = time.time()
    # response_result = requests.get(f'{LINK_FAST_API}/title/{title_id}?user_id={user_id}')
    # # print("\n\n\n\n\n Запрос: ",time.time()-start_req)
    # print(datetime.datetime.now())
    # if response_result.status_code == 200:
    #     time_start = time.time()
    #     dict_title = decode_nested_json(json.loads(response_result.json()['result']))
    #     # print('Разархивация',time.time()-time_start, '\n\n\n\n')
    #     dict_render = dict_title | {'user_id': user_id, 'user_auth': request.user.is_authenticated}
    #     return render(request, 'title/show.html', dict_render)


# try:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f"{LINK_FAST_API}/title/{title_id}?user_id={user_id}") as response:
#             if response.status != 200:
#                 # Обработка ошибки HTTP
#                 return render(request, 'error.html', {'error': 'Failed to fetch data'})
#
#             abc = await response.json()
#             abcd = await decode_nested_json_async(abc['result'])
#             print(abcd)
#
#             return render(request, 'title/show.html', {'dict_title': abcd})
#
# except Exception as e:
#     # Обработка других ошибок
#     print(f"Error: {e}")
#     return render(request, 'error.html', {'error': str(e)})

async def save_rating(request, title_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        rating = int(data['rating']) + 1
        user = await request.auser()
        user_id = user.id
        result = await session_post(f'{LINK_FAST_API}/title/rate?id_object={title_id}&id_user={user_id}&rate={rating}')
        return JsonResponse({'status': 'ok'})



async def save_pin(request, title_id):
    if request.method == 'POST':
        user = await request.auser()
        user_id = user.id
        result = await session_post(f'{LINK_FAST_API}/title/pinit?object_id={title_id}&type_object=0&user_id={user_id}')
        return JsonResponse({'status': 'ok'})

async def delete_pin(request, title_id):
    if request.method == 'POST':
        user = await request.auser()
        user_id = user.id
        result = await session_post(f'{LINK_FAST_API}/title/pinout?object_id={title_id}&type_object=0&user_id={user_id}')
        return JsonResponse({'status': 'ok'})

async def save_favorite(request, title_id):
    if request.method == 'POST':
        user = await request.auser()
        user_id = user.id
        result = await session_post(f'{LINK_FAST_API}/title/favoriteit?object_id={title_id}&type_object=0&user_id={user_id}')
        print("favorite_it")
        return JsonResponse({'status': 'ok'})
async def delete_favorite(request, title_id):
    if request.method == 'POST':
        user = await request.auser()
        user_id = user.id
        result = await session_post(f'{LINK_FAST_API}/title/favoriteout?object_id={title_id}&type_object=0&user_id={user_id}')
        print("favorite_out")
        return JsonResponse({'status': 'ok'})

async def save_review(request, title_id):
    if request.method == 'POST':
        user = await request.auser()
        user_id = user.id
        data = json.dumps(json.loads(request.body) | {'user_id': user_id})
        result = await session_post(f'{LINK_FAST_API}/title/{title_id}/save/review', data=data)
        return JsonResponse({'status': 'ok'})

async def show_reviews(request, title_id):
    page = int(request.GET.get('page'))
    response_result = await session_get(f'{LINK_FAST_API}/title/{title_id}/reviews?page={page}')
    if response_result['status'] == 200:
        dict_title_reviews = response_result['ses_json']['result']
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, "title/title_reviews.html", dict_title_reviews | {'page_up': page + 1, 'page_down': page - 1})
