from user import User
from student import Student  # Import Student class

class Admin(User):
    def register_user(self, users, passwords):
        user_id = str(len(users) + 1)
        name = input("Enter name: ")
        role = input("Enter role (admin/student): ")
        password = input("Enter password: ")
        
        if role == 'admin':
            new_user = Admin(user_id, name, role)
        else:
            new_user = Student(user_id, name, role)
        
        users.append(new_user)
        passwords[user_id] = password
        print(f"User {name} registered successfully.")

    def modify_user(self, users, passwords):
        user_id = input("Enter user ID to modify: ")
        for user in users:
            if user.user_id == user_id:
                new_name = input("Enter new name: ")
                new_password = input("Enter new password: ")
                user.name = new_name
                passwords[user_id] = new_password
                print(f"User {user_id} modified successfully.")
                return
        print("User not found.")

    def delete_user(self, users, passwords):
        user_id = input("Enter user ID to delete: ")
        for user in users:
            if user.user_id == user_id:
                users.remove(user)
                del passwords[user_id]
                print(f"User {user_id} deleted successfully.")
                return
        print("User not found.")
