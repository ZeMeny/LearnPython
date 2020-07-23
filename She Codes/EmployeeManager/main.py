import utils



def main():
    print("this is a employee management program, what do you wish to do?")
    print("#1 add a new employee")
    print("#2 remove an employee")
    print("#3 import employees list from file")
    print("#4 remove employees list from file")
    print("#5 print a monthly report")
    print("#6 generate employee attendance report")
    print("#7 mark attendance")
    print("#8 print all employees")

    while True:
        user_input = input()
        try:
            if user_input == '1':
                utils.addNewEmployee()
            elif user_input == '2':
                utils.removeEmployee()
            elif user_input == '3':
                utils.addMultipleEmployees()
            elif user_input == '4':
                utils.removeMultipleEmployees()
            elif user_input == '5':
                utils.printMonthlyReport()
            elif user_input == '6':
                utils.generateMothnlyReport()
            elif user_input == '7':
                utils.markAttendance()
            elif user_input == '8':
                utils.printAll()
        except ValueError:
            print(f"An Error occurred:  {ValueError}")
            print("try again")
        finally:
            main()


if __name__ == '__main__':
    main()
