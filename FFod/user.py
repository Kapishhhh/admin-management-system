class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role

    def update_profile(self, users, passwords):
        new_name = input("Enter new name: ")
        new_password = input("Enter new password: ")
        self.name = new_name
        passwords[self.user_id] = new_password
        for user in users:
            if user.user_id == self.user_id:
                user.name = new_name
        print("Profile updated successfully.")
