import json
import os

students = {}

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_role(self):
        return "Person"

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone})"

class Student(Person):
    def __init__(self, student_id, name, email, phone):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.subjects = {}  # key: subject name, value: Course object

    def get_role(self):
        return "Student"

    def add_subject(self, subject_name):
        """Step 10: Add a subject, preventing duplicates."""
        if subject_name in self.subjects:
            print(f"Subject '{subject_name}' already exists for this student.")
            return False
        self.subjects[subject_name] = Course(subject_name)
        print(f"Subject '{subject_name}' added.")
        return True

    def record_score(self, subject_name, score):
        """Step 11: Record a score for a subject."""
        if subject_name not in self.subjects:
            print(f"Subject '{subject_name}' not found for this student.")
            return False
        try:
            self.subjects[subject_name].grade.score = score
        except ValueError as e:
            print(f"Invalid score: {e}")
            return False
        return True

    def calculate_average(self):
        """Step 12: Calculate the average of all recorded scores."""
        recorded = [
            course.grade.score
            for course in self.subjects.values()
            if course.grade.score is not None
        ]
        if not recorded:
            return 0.0
        return sum(recorded) / len(recorded)

    @staticmethod
    def calculate_grade(score):
        """Step 8: Grading logic based on a fixed scale."""
        if score is None:
            return "N/A"
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def display_report(self):
        """Step 13: Display an individual student report."""
        print("\n" + "=" * 45)
        print(f"STUDENT REPORT: {self.name} (ID: {self.student_id})")
        print("=" * 45)
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print("-" * 45)

        if not self.subjects:
            print("No subjects registered.")
        else:
            print(f"{'Subject':<20}{'Score':<10}{'Grade':<10}")
            print("-" * 45)
            for subject_name, course in self.subjects.items():
                score = course.grade.score
                score_display = score if score is not None else "N/A"
                grade = self.calculate_grade(score)
                print(f"{subject_name:<20}{str(score_display):<10}{grade:<10}")

        average = self.calculate_average()
        overall_grade = self.calculate_grade(average if self.subjects else None)
        print("-" * 45)
        print(f"Average Score: {average:.2f}")
        print(f"Overall Status: {overall_grade}")
        

class Teacher(Person):
    def __init__(self, name, email, phone, staff_id, department):
        super().__init__(name, email, phone)
        self.staff_id = staff_id
        self.department = department

    def get_role(self):
        return "Teacher"


class Grade:
    """Represents a score/grade record. Step 7: encapsulation of score."""

    def __init__(self):
        self.__score = None  # private-style attribute

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Score must be a number.")
        if not (0 <= value <= 100):
            raise ValueError("Score must be between 0 and 100.")
        self.__score = value


class Course:
    """Represents a subject taken by a student."""

    def __init__(self, name):
        self.name = name
        self.grade = Grade()

def register_student():
    student_id = input("Enter student ID: ").strip()
    if student_id in students:
        print(f"A student with ID '{student_id}' already exists.")
        return

    name = input("Enter student name: ").strip()
    email = input("Enter student email: ").strip()
    phone = input("Enter student phone: ").strip()

    student = Student(student_id, name, email, phone)
    students[student_id] = student
    print(f"Student '{name}' registered successfully with ID '{student_id}'.")



def add_subject():
    student_id = input("Enter student ID: ").strip()
    student = students.get(student_id)
    if not student:
        print(f"No student found with ID '{student_id}'.")
        return

    subject_name = input("Enter subject name to add: ").strip()
    student.add_subject(subject_name)

def record_score():
    student_id = input("Enter student ID: ").strip()
    student = students.get(student_id)
    if not student:
        print(f"No student found with ID '{student_id}'.")
        return

    if not student.subjects:
        print("This student has no subjects yet. Add a subject first.")
        return

    subject_name = input("Enter subject name: ").strip()
    if subject_name not in student.subjects:
        print(f"Subject '{subject_name}' not found for this student.")
        return
    score_input = input("Enter score (0-100): ").strip()
    try:
        score = float(score_input)
    except ValueError:
        print("Invalid input. Score must be a number.")
        return

    if student.record_score(subject_name, score):
        print(f"Score {score} recorded for '{subject_name}'.")



def show_report():
    student_id = input("Enter student ID:").strip()
    student = students.get(student_id)
    if not student:
        print(f"No student found with ID  '{student_id}'. ")
        return
    student.display_report()


def search_student():
    query = input("Search by ID or name: ").strip().lower()

    if query in students:
        matches = [students[query]]
    else:
        matches = [
            s for s in students.values()
            if query in s.name.lower()
        ]

    if not matches:
        print("No matching students found.")
        return

    print(f"\nFound {len(matches)} matching student(s):")
    for s in matches:
        print(f"  ID: {s.student_id} | Name: {s.name} | Email: {s.email}")
    print()

def remove_student():
    student_id = input("Enter student ID to remove: ").strip()
    student = students.get(student_id)
    if not student:
        print(f"No student found with ID '{student_id}'.")
        return

    confirm = input(f"Are you sure you want to remove '{student.name}' (ID: {student_id})? (y/n): ").strip().lower()
    if confirm == "y":
        del students[student_id]
        print(f"Student '{student_id}' removed.")
    else:
        print("Removal cancelled.")


def display_all_students():
    if not students:
        print("No students registered yet.")
        return

    print(f"\n{'ID':<10}{'Name':<20}{'Subjects':<10}{'Average':<10}")
    print("-" * 50)
    for student in students.values():
        avg = student.calculate_average()
        print(f"{student.student_id:<10}{student.name:<20}{len(student.subjects):<10}{avg:<10.2f}")
    print()


def demonstrate_polymorphism():
    print("\n--- Polymorphism Demo ---")
    sample = [
        Person("Generic Person", "generic@example.com", "000-000-0000"),
        Student("DEMO01", "Demo Student", "demo.student@example.com", "111-111-1111"),
        Teacher("Demo Teacher", "demo.teacher@example.com", "222-222-2222", "T001", "Computer Science"),
    ]
    for person in sample:
        print(f"{person.name} -> get_role(): {person.get_role()}")


DATA_FILE = "students_data.json"


def save_data():
    data = {}
    for sid, student in students.items():
        data[sid] = {
            "name": student.name,
            "email": student.email,
            "phone": student.phone,
            "subjects": {
                name: course.grade.score
                for name, course in student.subjects.items()
            },
        }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to '{DATA_FILE}'.")


def load_data():
    if not os.path.exists(DATA_FILE):
        print("No saved data file found.")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    students.clear()
    for sid, info in data.items():
        student = Student(sid, info["name"], info["email"], info["phone"])
        for subject_name, score in info["subjects"].items():
            student.add_subject(subject_name)
            if score is not None:
                student.record_score(subject_name, score)
        students[sid] = student
    print(f"Data loaded from '{DATA_FILE}'.")

def main():
    menu = """

   STUDENT MANAGEMENT SYSTEM

1. Register Student
2. Add Subject
3. Record Score
4. Display Student Report
5. Search Student
6. Remove Student
7. Display All Students
8. Demonstrate Polymorphism
9. Save Data
10. Load Data
0. Exit

"""
    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            add_subject()
        elif choice == "3":
            record_score()
        elif choice == "4":
            show_report()
        elif choice == "5":
            search_student()
        elif choice == "6":
            remove_student()
        elif choice == "7":
            display_all_students()
        elif choice == "8":
            demonstrate_polymorphism()
        elif choice == "9":
            save_data()
        elif choice == "10":
            load_data()
        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
