from utils import datetime_utils,math_utils,random_utils,uuid_utils,file_utils

# --------------- DATETIME MENU ---------------
def datetime_menu():
    while True:
        print("\nDate and Time Operations :")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        ch=input("Enter your choice : ")
        if ch=="1":
            datetime_utils.show_current_datetime()
        elif ch=="2":
            datetime_utils.date_difference()
        elif ch=="3":
            datetime_utils.format_date()
        elif ch=="4":
            datetime_utils.stopwatch()
        elif ch=="5":
            datetime_utils.countdown()
        elif ch=="6":
            break
        else:
            print("Invalid choice!")

# --------------- MATH MENU ---------------
def math_menu():
    while True:
        print("\nMathematical Operations :")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        ch=input("Enter your choice : ")
        if ch=="1":
            math_utils.factorial()
        elif ch=="2":
            p=float(input("Enter principal : "))
            r=float(input("Enter rate (%) : "))
            t=float(input("Enter time (years) : "))
            ci=math_utils.compound_interest(p,r,t)
            print("Compound Interest : ", round(ci, 2))
        elif ch=="3":
            math_utils.trigonometry()
        elif ch=="4":
            r=float(input("Enter radius : "))
            area=math_utils.area_circle(r)
            print("Area : ", round(area, 2))
        elif ch=="5":
            break
        else:
            print("Invalid choice!")

# --------------- RANDOM MENU ---------------
def random_menu():
    while True:
        print("\nRandom Data Generation :")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        ch=input("Enter your choice : ")
        if ch=="1":
            random_utils.random_number()
        elif ch=="2":
            random_utils.random_list()
        elif ch=="3":
            random_utils.random_password()
        elif ch=="4":
            random_utils.random_otp()
        elif ch=="5":
            break
        else:
            print("Invalid choice!")

# --------------- FILE MENU ---------------
def file_menu():
    while True:
        print("\nFile Operations :")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        ch=input("Enter your choice : ")
        if ch=="1":
            name=input("Enter filename : ")
            file_utils.create_file(name)
        elif ch=="2":
            name=input("Enter filename : ")
            data=input("Enter data : ")
            file_utils.write_file(name,data)
        elif ch=="3":
            name=input("Enter filename : ")
            file_utils.read_file(name)
        elif ch=="4":
            name=input("Enter filename : ")
            data=input("Enter data : ")
            file_utils.append_file(name,data)
        elif ch=="5":
            break
        else :
            print("Invalid choice!")

# --------------- MAIN MENU ---------------
def main_menu():
    while True:
        print("\n========================================") 
        print("Multi-Utility Toolkit")
        print("\n========================================") 
        print("1. Date and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        ch=input("Enter your choice : ")
        if ch=="1":
            datetime_menu()
        elif ch=="2":
            math_menu()
        elif ch=="3":
            random_menu()
        elif ch=="4":
            uuid_utils.generate_uuid()
        elif ch=="5":
            file_menu()
        elif ch=="6":
            mod=input("Enter module name (math, time, random etc) : ")
            try:
                module=__import__(mod)
                print("Attributes : ")
                print(dir(module))
            except:
                print("Module not found!")
        elif ch=="7":
            print("Thank You!")
            break
        else:
            print("Invalid choice!")

if __name__=="__main__":
    main_menu()