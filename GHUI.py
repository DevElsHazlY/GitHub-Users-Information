# المطور: @T6GIO
# Telegram: https://t.me/T6GIO
# GitHub: https://github.com/DevElsHazlY

import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        print(f"\nمعلومات المستخدم @{username}:\n")
        print(f"الاسم: {data.get('name')}")
        print(f"عدد الريبو: {data.get('public_repos')}")
        print(f"عدد المتابعين: {data.get('followers')}")
        print(f"يتابع: {data.get('following')}")
        print(f"الموقع: {data.get('location')}")
        print(f"النبذة: {data.get('bio')}")
        print(f"رابط البروفايل: {data.get('html_url')}")
    else:
        print("❌ لم يتم العثور على المستخدم أو هناك مشكلة بالاتصال.")

if __name__ == "__main__":
    username = input("اكتب اسم المستخدم على GitHub: ").strip()
    if username:
        get_user_info(username)
    else:
        print("❗ يجب إدخال اسم مستخدم.")