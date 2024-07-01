from user import User

def read_users():
    users = []
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                user_id, name, role = line.strip().split(',')
                users.append(User(user_id, name, role))
    except FileNotFoundError:
        print("users.txt not found. Starting with an empty user list.")
    return users

def write_users(users):
    with open('users.txt', 'w') as file:
        for user in users:
            file.write(f"{user.user_id},{user.name},{user.role}\n")

def read_passwords():
    passwords = {}
    try:
        with open('passwords.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    user_id, password = parts
                    passwords[user_id] = password
                else:
                    print(f"Skipping improperly formatted line: {line.strip()}")
    except FileNotFoundError:
        print("passwords.txt not found. Starting with an empty password list.")
    return passwords

def write_passwords(passwords):
    with open('passwords.txt', 'w') as file:
        for user_id, password in passwords.items():
            file.write(f"{user_id},{password}\n")
