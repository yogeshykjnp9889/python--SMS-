import json
from tabulate import tabulate

dict_student = []

class Student:

    # Add Student.
    def Add_std(self):
        ID = int(input("Enter student ID: "))
        # If not, add the student
        name = input("Enter name of student: ")
        age = int(input("Enter age of student: "))
        city = input("Enter town/city of student: ")
        # Read the existing data from the file if it exists
        dict_student = [{"ID": ID, "Name": name, "Age": age, "City": city}]
        try:
            with open("data_sheet.json", "r") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is empty, initialize as an empty list
            existing_data = []

        # Append the new student data to the existing data
        existing_data.extend(dict_student)

        # Write the combined data back to the file
        with open("data_sheet.json", "w") as f:
            json.dump(existing_data, f, indent=4)
       


    # Update Student.
    def Upd_std(self):
        ID = int(input("Enter student ID: "))
        found = False
        with open("data_sheet.json", "r") as f:
            data = json.load(f)
            for student in data:
                if student['ID'] == ID:
                    found = True
                    print("<= Enter student details =>")
                    student['Name'] = input("Enter name of student: ")
                    student['Age'] = int(input("Enter age of student: "))
                    student['City'] = input("Enter town/city of student: ")
                    # Write the updated data back to the JSON file
                    with open("data_sheet.json", "w") as f_out:
                        json.dump(data, f_out, indent=4)
                    print(f"Student with ID {ID} updated successfully.")
                    break 
            if not found:
                print(f"ID: {ID} does not exist.")

    # View a specific Student via ID number.
    def View_std(self):
        ID = int(input("Enter student ID: "))
        found = False
        for student in dict_student:
            if student['ID'] == ID:
                found = True
                print(student)
                break
        if not found:
            print(f"ID: {ID} does not exist.")

    def Disp_std(self):
        try:
            with open("data_sheet.json", "r") as f:
                data = json.load(f)

            # Check if data is a list of dictionaries
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                if data:
                    print(tabulate(data, headers="keys", tablefmt="grid"))
                else:
                    print("No data found in the file.")
            else:
                print("The data format is incorrect. Expected a list of dictionaries.")
        except FileNotFoundError:
            print("The file does not exist.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the file.")


    # Add dict_student to a JSON file (append data correctly)
    def Del_Student(self):
        ID = int(input("Enter student ID: "))
        found = False
        with open("data_sheet.json", "r") as f:
            found = True
            data = json.load(f)
            for student in data:
                if student['ID'] == ID:
                    data.remove(student)
                    with open("data_sheet.json", "w") as f_out:
                        json.dump(data, f_out, indent=4)
                    print(f"Delete Student ID {ID} successfully.")
                    break 
            if not found:
                print(f"ID: {ID} does not exist.")