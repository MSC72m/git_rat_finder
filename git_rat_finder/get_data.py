import httpx


async def get_followers(username, token, followers):
    headers = {"Authorization": f"token {token}"}
    params = {"page": 1, "per_page": 100}
    async with httpx.AsyncClient() as client:
        while True:
            url = f'https://api.github.com/users/{username}/followers'
            response = await client.get(url, headers=headers, params=params)
            if response.status_code != 200:
                raise ConnectionError('Connection error or was not able to retrieve data from the API')

            data = response.json()
            if not data:
                break

            followers.extend([follower['login'] for follower in data])
            params['page'] += 1
    return followers


async def get_following(username, token, following):
    headers = {'Authorization': f'token {token}'}
    params = {'page': 1, 'per_page': 100}
    async with httpx.AsyncClient() as client:
        while True:
            url = f'https://api.github.com/users/{username}/following'
            response = await client.get(url, headers=headers, params=params)
            if response.status_code != 200:
                raise ConnectionError('Connection error or was not able to retrieve data from the API')

            data = response.json()
            if not data:
                break

            following.extend([user['login'] for user in data])
            params['page'] += 1
    return following
