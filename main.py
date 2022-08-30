# importing modules
from console_color import *
from Student import Student

# creating database
students_database = []


# welcome screen
def welcome_screen():
    print(YELLOW, '**** Welcome To NIIT Student Management System ****')
    user_input = int(input('1. Add Student\n'
                           '2. View all student details\n'
                           '3. Search for student details\n'
                           '4. Delete Students Info\n'
                           '5. Update Student Info\n'
                           '6. About System\n'
                           '7. Exit Application\n\n'
                           'Please Provide Your Request : '))

    user_options(user_input)


# user options
def user_options(user_input):
    if user_input == 1:
        response = 'yes'
        while response == 'yes':
            student_info = add_student_info()
        user_ans = input(BLUE + 'Do you want to save info?(y/n) : ').lower()
        if user_ans == 'y':
            students_database.append(student_info)
            print(GREEN, f'{student_info.get_first_name()} '
                         f'{student_info.get_middle_name()} '
                         f'{student_info.get_last_name()} '
                         f'has been saved successfully')
        elif user_ans == 'n':
            user_ans = input('Are you sure you want to cancel?(y/n): ').lower()
            if user_ans == 'y':
                students_database.append(student_info)
            else:
                students_database.append(students_database)
        else:
            welcome_screen()
        response = input('Is There Another Student? (yes/no) ').lower()
        welcome_screen()

    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        pass
    elif user_input == 6:
        pass
    elif user_input == 7:
        close_program()
    else:
        invalid_request()


# about us function
def about_us():
    print(BLUE, '**** This System Keep Track Of Students Details *****')
    welcome_screen()


# close_program function
def close_program():
    print(BLUE, '**** Thanks You For  Using NIIT SMS, Hope To See You Again ****')
    exit(1)


# Invalid request function
def invalid_request():
    print(RED, 'Invalid request, Try Again!')
    welcome_screen()


# Add student info
def add_student_info():
    print(YELLOW, '**** Fill Details Below To Add Students ****', WHITE)
    sid = input('Provide Student ID: ')
    f_name = input('Provide First Name: ')
    l_name = input('Provide Last Name: ')
    m_name = input('Provide Middle Name:')
    dob = input('Provide Your Date Of Birth: DD/MM/YY ')
    course = input('Provide Course: ')
    period = input('Provide Period: ')

    # creating student object
    student_info = Student(sid, f_name, l_name, m_name, dob, course, period)
    return student_info


# calling functions

