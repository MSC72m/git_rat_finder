import asyncio
import httpx


async def follow_user(username, token):
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/user/following/{username}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(url, headers=headers)
        except Exception as e:
            print(e)
    return response.status_code == 204


async def unfollow_user(username, token):
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/user/following/{username}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url, headers=headers)
        except Exception as e:
            print(e)
    return response.status_code == 204


async def unfollow_rats(token, following, followers, exceptions):
    async with httpx.AsyncClient() as client:
        for username in following:
            if username not in followers and username not in exceptions:
                headers = {'Authorization': f'token {token}'}
                url = f'https://api.github.com/user/following/{username}'
                try:
                    response = await client.delete(url, headers=headers)
                except Exception as e:
                    print(e)
                if response.status_code == 204:
                    print(f"Unfollowed {username}")


def add_exception(exceptions):
    exception_input = input("Enter the username(s) to add to the exception list (separated by spaces): ")
    new_exceptions = exception_input.split()
    exceptions.extend(new_exceptions)
    return exceptions


def remove_exception(exceptions):
    print("Current exception list:", exceptions)
    user = input("Enter the name of the user to remove from the exception list: ")
    if user in exceptions:
        exceptions.remove(user)
        print(f"Removed {user} from the exception list.")
    else:
        print(f"{user} not found in the exception list.")
