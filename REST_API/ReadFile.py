user_info.json
{
    "name": "Udemy user1",
    "email": "user1@example.com",
    "phone": "123-456-7890"
}

fileutils.py
import json

def update_user_info(file_name, name=None, email=None, phone=None):
    with open(file_name, 'r') as file:
        user_info = json.load(file)

    if name is not None:
        user_info['name'] = name
    if email is not None:
        user_info['email'] = email
    if phone is not None:
        user_info['phone'] = phone

    return user_info
