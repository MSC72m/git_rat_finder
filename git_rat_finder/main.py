import asyncio
import time
from get_data import get_followers, get_following
from actions import follow_user, unfollow_user, unfollow_rats, add_exception, remove_exception


async def main():
    followers = []
    following = []
    exceptions = []

    options = [
        "Show me my followers so I can bask in my popularity.",
        "Display who I'm stalking—uh, following—on this fine day.",
        "Unfollow a user—time to make some space in my social circle!",
        "Follow someone new—let’s expand my network of friends, shall we?",
        "Add users to the exception list—because everyone needs a VIP section.",
        "Remove users from the exception list—time to update my exclusive club!",
        "Unfollow GitHub 'rats'—say goodbye to those pesky freeloaders.",
        "Become a CHAD: follow those who follow me but I haven’t followed yet.",
        "or q: Quit—I'll just leave now and come back when I'm ready."
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
            print(f"{i + 1}: {option}")
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
            with open("../exception.txt", "w") as file:
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
        elif selected_option in ['9', 'q', "Q", "quit", "Quit"]:
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    asyncio.run(main())
