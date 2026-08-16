Students = {
    "STDOO1": {"name": "Emma", "Score": 85},
    "STDOO2": {"name": "Ada", "Score": 72},
    "STDOO3": {"name": "johnpaul", "Score": 90}
}
while True:
    print("Student Result Mangement System")
    print("1. View all students ")
    print("2. Add a new student")
    print("3. update a students score")
    print("4. Delete a student")
    print("5. Search for a student")
    print("6. Display students who passed")
    print("7. display students Grades")
    print("0. exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        print("All Students")
        for std_id, info in Students.items():
            print(f"ID {std_id}  Name: {info['name']}  Score: {info['Score']}")

    elif choice == "2":
        std_id = input("Enter new student ID:").strip()
        if std_id in Students:
            print(f"Students ID '{std_id}' already exists.")
        else:
            name = input("Enter student name:").strip()
            score = float(input("Enter student score:"))

            Students.setdefault(std_id, {"name": name, "Score": score})
            print(f"Students'{name}' added.")

    elif choice == "3":
        std_id = input("Enter student ID to upgrade: ").strip()
        record = Students.get(std_id)
        if record is None:
            print(f"No student found with ID '{std_id}'. ")
        else:
            new_score = float(input(f"Enter new score for {record['name']}: "))
            record.update({"Score": new_score})
            print(f"score updated to {new_score}.")

    elif choice == "4":
        std_id = input("Enter student ID to delete: ").strip()
        removed = Students.pop(std_id, None)
        if removed is None:
            print(f"No student found with ID '{std_id}' .")
        else:
            print(f"Removed student '{removed['name']}' . ")

    elif choice == "5":
        std_id = input("Enter student ID to search").strip()
        record = Students.get(std_id)
        if record is None:
            print(f"No student found with ID '{std_id}' .")
        else:
            print(f"Found : {record['name']} Score: {record['Score']}")

    elif choice == "6":
        passed = {std_id: info for std_id,
                  info in Students.items() if info["Score"] >= 50}
        print("---- Passed Students(Score >= 50)-----")
        for std_id, info in passed.items():
            print(
                f"ID : {std_id}  Name: {info['name']} Score: {info['Score']}")

    elif choice == "7":
        grades = {
            std_id: (
                "A" if info["Score"] >= 70
                else "B" if info["Score"] >= 60
                else "C" if info["Score"] >= 50
                else "D" if info["Score"] >= 40
                else "F"
            )
            for std_id, info in Students.items()
        }
        print("-----Students Grades------")
        for std_id, grade in grades.items():
            print(f" ID: {std_id} "
                  f"Name:{Students[std_id]['name']} "
                  f"Grade:{grade}")

    elif choice == "0":
        print("Existing .Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
