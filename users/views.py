from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from asgiref.sync import sync_to_async

from utils.dependencies_my import session_get, session_post, session_patch
from .forms import LoginForm, RegisterForm
from django.conf import settings
from django.http import JsonResponse

import requests, json
LINK_FAST_API = settings.LINK_FAST_API



async def register_menu(request):
    user = await request.auser()
    user_id = user.id
    response_result = await session_get(f'{LINK_FAST_API}/user/userhash?user_id={user_id}')
    user_hash = response_result['ses_json']['result']
    # user_hash = json.loads(response_result.json()['result'])
    print(user_hash)
    return redirect(f"/accounts/profile/{user_hash}")


async def sign_up(request):
    print('sign_up')
    if request.method == 'GET':
        print('GET')

        form = RegisterForm()
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'users/registration.html', {'form': form})
    if request.method == 'POST':
        print('POST')
        form = RegisterForm(request.POST)
        is_valid = await sync_to_async(form.is_valid, thread_sensitive=True)()
        if is_valid:
            print('is valid')

            user = form.save(commit=False)
            user.username = user.username.lower()
            await sync_to_async(user.save)()

            # messages.success(request, 'You have singed up successfully.')
            await sync_to_async(login)(request, user)
            user = await request.auser()
            user_username = user.username
            user_id = user.id

            print("Регистрация", user_username, user_id)
            response_result = await session_post(f'{LINK_FAST_API}/account/new?user_id={user_id}&user_nickname={user_username}')
            if response_result.status == 200:
                print('захеширование')
            return redirect('home')
        else:
            print('is not valid')

            render_async = sync_to_async(render, thread_sensitive=True)
            return await render_async(request, 'users/registration.html', {'form': form, 'title': 'Логин не правельный или почта не имеет нормального формата, пароль может быть слишком коротким и лёгким'})


async def logout_view(request):
    await sync_to_async(logout)(request)
    return redirect('home')

async def sign_in(request):
    form = LoginForm(request.POST)
    is_valid = await sync_to_async(form.is_valid, thread_sensitive=True)()
    if is_valid:
        print('form valid')

        user = await sync_to_async(authenticate)(request, username=form.cleaned_data['username'].lower(), password=form.cleaned_data['password'])
        try:
            await sync_to_async(login)(request, user)
        except:
            render_async = sync_to_async(render, thread_sensitive=True)
            return await render_async(request, 'users/login.html', {'form': form, 'title': 'Логин или пароль не правильно введены'})

        return redirect('home')

    render_async = sync_to_async(render, thread_sensitive=True)
    return await render_async(request, 'users/login.html', {'form': form})

async def profile(request, profile_hash_user_id):
    # print(profile_hash_user_id)
    user = await request.auser()
    user_id = user.id

    response_result = await session_get(f'{LINK_FAST_API}/user/profile/{profile_hash_user_id}?user_id={user_id}')
    if response_result['status'] == 200:
        dict_profile = response_result['ses_json']['result']
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'users/user_window.html', dict_profile | {'profile_hash_user_id':profile_hash_user_id})

async def user_favorites(request, profile_hash_user_id):
    user = await request.auser()
    user_id = user.id
    response_result = await session_get(f'{LINK_FAST_API}/user/favorites/{profile_hash_user_id}')
    if response_result['status'] == 200:
        dict_user_favorites = response_result['ses_json']['result']
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'users/favorites.html', dict_user_favorites | {'profile_hash_user_id':profile_hash_user_id})

async def user_reviews(request, profile_hash_user_id):
    user = await request.auser()
    user_id = user.id
    page = int(request.GET.get('page'))

    response_result = await session_get(f'{LINK_FAST_API}/user/reviews/{profile_hash_user_id}?page={page}')
    if response_result['status'] == 200:
        dict_user_favorites = response_result['ses_json']['result']
        # print(dict_user_favorites)
        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'users/reviews.html', dict_user_favorites |
                      {'profile_hash_user_id':profile_hash_user_id, 'page_up':page+1, 'page_down':page-1})

async def user_review_show(request, profile_hash_user_id, movie_id):
    user = await request.auser()
    user_id = user.id
    response_result = await session_get(f'{LINK_FAST_API}/user/{profile_hash_user_id}/review/{movie_id}?user_id={user_id}')
    if response_result['status'] == 200:

        dict_user_review = response_result['ses_json']['result']

        render_async = sync_to_async(render, thread_sensitive=True)
        return await render_async(request, 'users/show_review.html', dict_user_review | {"user_auth":True if user_id else False})

async def user_reaction(request, profile_hash_user_id, movie_id):
    user = await request.auser()
    user_id = user.id
    response_result = await session_post(f'{LINK_FAST_API}/user/{profile_hash_user_id}/review/{movie_id}/reaction?type={request.GET.get('reaction')}&user_id={user_id}')
    if response_result.status == 200:
        return JsonResponse({"result":"ok"})

async def change_nickname(request):
    nickname = request.GET.get('nickname')
    user = await request.auser()
    user_id = user.id
    # print(nickname, user_id)
    response_result = await session_post(f'{LINK_FAST_API}/user/change/nickname?nickname={nickname}&user_id={user_id}')
    if response_result.status == 200:
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': False})

async def change_block(request):
    user = await request.auser()
    user_id = user.id
    response_result = await session_post(f'{LINK_FAST_API}/user/change/block?user_id={user_id}')
    if response_result.status == 200:
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': False})

async def change_review(request, profile_hash_user_id, movie_id):
    user = await request.auser()
    user_id = user.id
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)|{'user_id':user_id}
        response_result = await session_patch(f'{LINK_FAST_API}/user/{profile_hash_user_id}/review/{movie_id}/change/', data=json.dumps(data))
        return JsonResponse({'status': 'ok'})