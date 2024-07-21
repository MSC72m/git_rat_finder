import asyncio
import time
from get_data import get_followers, get_following
from actions import follow_user, unfollow_user, unfollow_rats, add_exception, remove_exception


async def main():
    followers = []
    following = []
    exceptions = []

    options = [
        "Enter 1 to get your follower list and print them in your terminal",
        "Enter 2 to get your following list and print them in your terminal",
        "Enter 3 to unfollow a user",
        "Enter 4 to follow a user",
        "Enter 5 to add users to the exception list",
        "Enter 6 to remove users from the exception list",
        "Enter 7 to unfollow GitHub rats",
        "Enter 8 to follow users who follow you but whom you don't follow",
        "Enter 9 or q to quit"
    ]
    username = input('Please enter your username: ')
    token = input('Please enter your GitHub access token: ')

    start = time.time()
    followers = await get_followers(username, token, followers)
    following = await get_following(username, token, following)
    finish = time.time()
    print(f"Time taken to fetch initial data: {finish - start} seconds")

    while True:
        for i, option in enumerate(options):
            print(f"{i + 1} - {option}")
        selected_option = input("Please enter the option you want: ")

        if selected_option == '1':
            for i in range(0, len(followers), 5):
                print(" | ".join(followers[i:i + 5]))
                print("--" * 38)
        elif selected_option == '2':
            for i in range(0, len(following), 5):
                print(" | ".join(following[i:i + 5]))
                print("--" * 38)
        elif selected_option == '3':
            user_to_unfollow = input("Please enter the user you want to unfollow: ")
            if user_to_unfollow not in exceptions:
                unfollowed = await unfollow_user(user_to_unfollow, token)
                if unfollowed:
                    print(f"Successfully unfollowed {user_to_unfollow}")
                else:
                    print(f"Failed to unfollow {user_to_unfollow}")
            else:
                print(f"{user_to_unfollow} is in your exception list.")
        elif selected_option == '4':
            user_to_follow = input("Please enter the user you want to follow: ")
            followed = await follow_user(user_to_follow, token)
            if followed:
                print(f"Successfully followed {user_to_follow}")
            else:
                print(f"Failed to follow {user_to_follow}")
        elif selected_option == '5':
            add_exception(exceptions)
            with open("exception.txt", "w") as file:
                for item in exceptions:
                    file.write(item + "\n")
            print("Exceptions updated.")
        elif selected_option == '6':
            remove_exception(exceptions)
        elif selected_option == '7':
            await unfollow_rats(token, following, followers, exceptions)
        elif selected_option == '8':
            for username in followers:
                if username not in following:
                    await follow_user(username, token)
                    print(f"Followed {username}")
        elif selected_option in ['9', 'q']:
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    asyncio.run(main())
