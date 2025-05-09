class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        try:
            if student_id in self.students:
                raise ValueError("Student ID already exists.")
            self.students[student_id] = name
            print(f"Added student: {name} (ID: {student_id})")
        except ValueError as e:
            print("Error:", e)

    def remove_student(self, student_id):
        try:
            if student_id not in self.students:
                raise ValueError("Student ID not found.")
            name = self.students.pop(student_id)
            print(f"Removed student: {name} (ID: {student_id})")
        except ValueError as e:
            print("Error:", e)

    def search_student(self, student_id):
        try:
            if student_id not in self.students:
                raise ValueError("Student not found.")
            print(f"Student found: {self.students[student_id]} (ID: {student_id})")
        except ValueError as e:
            print("Error:", e)


# Interactive user input
def main():
    sms = StudentManagementSystem()

    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Show All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            try:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                sms.add_student(student_id, name)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "2":
            try:
                student_id = int(input("Enter Student ID to remove: "))
                sms.remove_student(student_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "3":
            try:
                student_id = int(input("Enter Student ID to search: "))
                sms.search_student(student_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "4":
            if sms.students:
                print("\nAll Students:")
                for sid, name in sms.students.items():
                    print(f"ID: {sid}, Name: {name}")
            else:
                print("No students found.")
        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
