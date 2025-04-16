# Developer: @T6GIO
# Telegram: https://t.me/T6GIO
# GitHub: https://github.com/DevElsHazlY

import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        print(f"\nUser Info for @{username}:\n")
        print(f"Name: {data.get('name')}")
        print(f"Public Repositories: {data.get('public_repos')}")
        print(f"Followers: {data.get('followers')}")
        print(f"Following: {data.get('following')}")
        print(f"Location: {data.get('location')}")
        print(f"Bio: {data.get('bio')}")
        print(f"Profile URL: {data.get('html_url')}")
    else:
        print("❌ User not found or there was a connection issue.")

if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()
    if username:
        get_user_info(username)
    else:
        print("❗ You must enter a username.")
