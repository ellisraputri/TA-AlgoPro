from Course import Course
from Student import Student

courses=[]
students=[]

def AddCourse(course_code, title, lecturer, major, max_capacity, current_enrolled):
    course = Course(course_code, title, lecturer, major, max_capacity, current_enrolled)
    courses.append(course)

def AddStudent(student_id, name, courses_enrolled, student_major):
    student = Student(student_id, name, courses_enrolled, student_major)
    students.append(student)

#to check if the course exists or not
def checkCourse(title):
    if courses==[]:
        return ""
    for course in courses:
        if(course.getTitle() == title):
            return course
        else:
            return ""

#to check if the student exists or not
def checkStudent(name):
    if students ==[]:
        return ""
    for student in students:
        if(student.getName() == name):
            return student
        else:
            return ''

#to check if the student is already in course or not
def checkStudentinCourse(course_check, student_name):
    for name in course_check.students:
        if name == student_name:
            return False
    return True



user_input=True
while(user_input):
    user_input1 = input("Do you want to still in the system? (Y/N) ")
    while(user_input1.lower()!='y' and user_input1.lower()!='n'):
        user_input1 = input("Do you want to still in the system? (Y/N) ")
    if(user_input1 =='y'):
        user_input = True
    else:
        user_input = False
        break

    x=input("Welcome. What do you want to do? \n1.Add course \n2.Add student \
        \n3.Print course details \n4.Print student information \n5.Check course available slot \
        \n6.Enroll student to a course \n")

    while(x!='1' and x!='2' and x!='3' and x!='4' and x!='5' and x!='6'):
        x=input("Please re-input your choice. \n1.Add course \n2.Add student \
        \n3.Print course details \n4.Print student information \n5.Check course available slot \
        \n6.Enroll student to a course")

    if(x=='1'):
        course_code = input("Enter course code: ")
        title = input("Enter course title: ")
        lecturer = input("Enter course lecturer: ")
        major = input("Enter major for the course: ")
        max_capacity = int(input("Enter course maximum capacity: "))
        current_enrolled = int(input("Enter course current enrolled students: "))
        while(max_capacity < current_enrolled):
            current_enrolled = int(input("Re-Enter course current enrolled students: "))
        AddCourse(course_code, title, lecturer, major, max_capacity, current_enrolled)

    elif (x=='2'):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        courses_enrolled = int(input("Enter student's number of course enrolled: "))
        student_major = input("Enter student major: ")
        AddStudent(student_id, name, courses_enrolled, student_major)

    elif(x=='3'):
        course_title = input("Enter title of the course you want to print: ")
        check_result= checkCourse(course_title)
        if (check_result==''):
            print("Course not found")
        else:
            check_result.courseDetails()
    
    elif(x=='4'):
        student_name = input("Enter name of the student you want to print: ")
        check = checkStudent(student_name)
        if (check==''):
            print("Student not found")
        else:
            check.studentDetails()
    
    elif(x=='5'):
        course_title = input("Enter the title of the course you want to check availability for: ")
        check_result = checkCourse(course_title)
        if (check_result==''):
            print("Course not found")
        else:
            check_result.checkAvailableSlot()
    
    elif(x=='6'):
        student_name = input("Enter name of the student you want to enroll: ")
        course_title = input("Enter the title of the course you want to enroll: ")
        student_check = checkStudent(student_name)      
        course_check = checkCourse(course_title)        

        if (student_check==''):
            print("Student not found")
        else:
            if (course_check==''):
                print("Course not found")
            else:
                student_in_course = checkStudentinCourse(course_check, student_name)    
                if(student_in_course == False):
                    print(f"{student_name} is already in {course_title}")
                else:
                    major = student_check.getStudentMajor()
                    course_check.enrollStudent(major, student_name)