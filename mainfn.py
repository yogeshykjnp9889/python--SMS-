from Student import Student

def main():
    sms = Student()

    while True:
        print("===Student Management System of Library===")
        print("1. Add Student.")
        print("2. Update Student Data.")
        print("3. View Student via ID.")
        print("4. Display all students in list.")
        print("5. Delete Student based on ID.")

        choice = input("Enter your choice: ")

        if choice == '1':
            sms.Add_std()

        if choice == '2':
            sms.Upd_std()

        if choice == '3':
            sms.View_std()
        
        if choice == '4':
            sms.Disp_std()

        if choice == '5':
            sms.Del_Student()

if __name__ == "__main__":
    main()