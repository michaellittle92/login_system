from main import log_in_user, register_user, get_all_users
import sys

menu_items = ["1. read all users", "2. register new user", "3. log in", "Q. quit"]

def get_login_details():
    username = input("username: ")
    password = input("password: ")
    return username, password

while True:
    for item in menu_items:
        print(item)
    user_input = input("Selection: ").capitalize().strip()
    if user_input == "1":
        get_all_users()
    elif user_input == "Q":
       sys.exit()
    elif user_input == "2":
        username, password = get_login_details()
        register_user(username, password)
        print("user registered")
    elif user_input == "3":
        username, password = get_login_details()
        log_in_user(username, password)
    else:
        print("error, please try again.")


