import json
import aiohttp
timeout = aiohttp.ClientTimeout(total=10)

async def session_get(query, params = {}):
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
            response_result = await session.get(query, params=params)
            return {'status': response_result.status,'ses_json':await response_result.json()}
    except (RuntimeError, aiohttp.ClientError) as e:
        print('ошибка', e)
    return {'status': 500, 'result': ''}


async def session_post(query, data={}):
    async with aiohttp.ClientSession(timeout=timeout) as session:
        response_result = await session.post(query, data=data)
    return response_result

async def session_patch(query, data={}):
    async with aiohttp.ClientSession(timeout=timeout) as session:
        response_result = await session.patch(query, data=data)
    return response_result

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

async def decode_nested_json_async(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = await decode_nested_json(value)
    elif isinstance(data, list):
        for i, value in enumerate(data):
            data[i] = await decode_nested_json(value)
    elif isinstance(data, str):
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return data
    return data