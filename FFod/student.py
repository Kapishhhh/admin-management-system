from user import User

class Student(User):
    def view_grades(self):
        with open('grades.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == self.user_id:
                    print(f"Grades: {data[1:]}")
                    return
        print("No grades found.")

    def view_eca(self):
        with open('eca.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == self.user_id:
                    print(f"ECA: {data[1:]}")
                    return
        print("No ECA details found.")
