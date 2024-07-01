from user import User
from admin import Admin
from student import Student
from file_handler import read_users, write_users, read_passwords, write_passwords

def main():
    users = read_users()
    passwords = read_passwords()
    
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        user = authenticate_user(username, password, users, passwords)
        if user:
            if user.role == 'admin':
                admin_dashboard(user, users, passwords)
            elif user.role == 'student':
                student_dashboard(user, users, passwords)
            break
        else:
            print("Invalid username or password. Please try again.")

def authenticate_user(username, password, users, passwords):
    for user in users:
        if user.name == username and passwords[user.user_id] == password:
            if user.role == 'admin':
                return Admin(user.user_id, user.name, user.role)
            elif user.role == 'student':
                return Student(user.user_id, user.name, user.role)
    return None

def admin_dashboard(admin, users, passwords):
    while True:
        print("\nAdmin Dashboard")
        print("1. Register User")
        print("2. Modify User")
        print("3. Delete User")
        print("4. Logout")
        
        choice = input("Enter choice: ")
        if choice == '1':
            admin.register_user(users, passwords)
        elif choice == '2':
            admin.modify_user(users, passwords)
        elif choice == '3':
            admin.delete_user(users, passwords)
        elif choice == '4':
            write_users(users)
            write_passwords(passwords)
            break
        else:
            print("Invalid choice. Please try again.")

def student_dashboard(student, users, passwords):
    while True:
        print("\nStudent Dashboard")
        print("1. View Grades")
        print("2. View ECA")
        print("3. Update Profile")
        print("4. Logout")
        
        choice = input("Enter choice: ")
        if choice == '1':
            student.view_grades()
        elif choice == '2':
            student.view_eca()
        elif choice == '3':
            student.update_profile(users, passwords)
        elif choice == '4':
            write_users(users)
            write_passwords(passwords)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
