from colorama import init, Fore, Style

# آماده‌سازی رنگ‌ها
init(autoreset=True)

# app.py
import json
import os

FILE = "students.json"

# بررسی اینکه فایل دیتابیس وجود دارد یا نه
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

# خواندن لیست دانشجویان
def load_students():
    with open(FILE, "r") as f:
        return json.load(f)

# ذخیره لیست دانشجویان
def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

# اضافه کردن دانشجو
def add_student():
    name = input("Name: ")
    age = input("Age: ")
    student = {"name": name, "age": age}
    students = load_students()
    students.append(student)
    save_students(students)
    print("Student added successfully!")

# دیدن لیست دانشجویان
# دیدن لیست دانشجویان به شکل جدول
def view_students():
    students = load_students()
    if not students:
        print("No students yet!")
    else:
        print("\n{:<5} {:<20} {:<5}".format("No.", "Name", "Age"))
        print("-" * 32)
        for i, s in enumerate(students, start=1):
            print("{:<5} {:<20} {:<5}".format(i, s['name'], s['age']))

# حذف دانشجو
def delete_student():
    students = load_students()
    view_students()
    if not students:
        return
    
    try:
        idx = int(input("Enter student number to delete: ")) - 1
        if 0 <= idx < len(students):
            confirm = input(f"Are you sure you want to delete {students[idx]['name']}? (y/n): ").lower()
            if confirm == 'y':
                removed = students.pop(idx)
                save_students(students)
                print(Fore.GREEN + f"Student {removed['name']} deleted successfully!" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "Deletion cancelled." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid number!" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Invalid input! Please enter a number." + Style.RESET_ALL)


# ویرایش دانشجو
def edit_student():
    students = load_students()
    view_students()
    if not students:
        return
    idx = int(input("Enter student number to edit: ")) - 1
    if 0 <= idx < len(students):
        name = input(f"New name ({students[idx]['name']}): ") or students[idx]['name']
        age = input(f"New age ({students[idx]['age']}): ") or students[idx]['age']
        students[idx] = {"name": name, "age": age}
        save_students(students)
        print(f"Student {name} updated successfully!")
    else:
        print("Invalid number!")

# جستجوی دانشجو بر اساس نام یا شماره
def search_student():
    students = load_students()
    if not students:
        print("No students yet!")
        return

    choice = input("Search by (1) Name or (2) Number? Enter 1 or 2: ")
    if choice == "1":
        name = input("Enter name to search: ").lower()
        found = [s for s in students if name in s['name'].lower()]
        if found:
            print("\n{:<5} {:<20} {:<5}".format("No.", "Name", "Age"))
            print("-" * 32)
            for i, s in enumerate(found, start=1):
                print("{:<5} {:<20} {:<5}".format(i, s['name'], s['age']))
        else:
            print("No students found with that name.")
    elif choice == "2":
        num = input("Enter student number: ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= len(students):
                s = students[num-1]
                print("\n{:<5} {:<20} {:<5}".format("No.", "Name", "Age"))
                print("-" * 32)
                print("{:<5} {:<20} {:<5}".format(num, s['name'], s['age']))
            else:
                print("Invalid student number.")
        else:
            print("Invalid input.")
    else:
        print("Invalid choice.")

# مرتب‌سازی دانشجویان بر اساس نام یا سن
def sort_students():
    students = load_students()
    if not students:
        print("No students yet!")
        return

    print("Sort by:")
    print("1. Name")
    print("2. Age")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        students.sort(key=lambda s: s['name'].lower())
    elif choice == "2":
        students.sort(key=lambda s: int(s['age']))
    else:
        print("Invalid choice!")
        return

    save_students(students)
    print("Students sorted successfully!")
    view_students()

# منو اصلی
def main():
    while True:
        print(Fore.CYAN + "\n=== Student Management System ===" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Sort Students")
        print("7. Exit" + Style.RESET_ALL)
        
        choice = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            sort_students()
        elif choice == "7":
            print(Fore.MAGENTA + "Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
