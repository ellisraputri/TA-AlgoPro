from Course import Course
from Student import Student
import matplotlib.pyplot as plt

courses=[]
students=[]

def AddCourse(course_code, title, lecturer, major, max_capacity, current_enrolled):
    if courses==[]:
        course = Course(course_code, title, lecturer, major, max_capacity, current_enrolled)
        courses.append(course)
        print("Course successfully added")
    else:
        for course1 in courses:
            if(course1.getCourseCode() == course_code):
                print('Course code has already existed')
                break
            else:
                course = Course(course_code, title, lecturer, major, max_capacity, current_enrolled)
                courses.append(course)
                print("Course successfully added")
                break


def AddStudent(student_id, name, courses_enrolled, student_major):
    if students == []:
        student = Student(student_id, name, courses_enrolled, student_major)
        students.append(student)
        print("Student successfully added")
    else:
        for student1 in students:
            if(student1.getStudentId() != student_id):
                print('Student ID has already existed')
                break
            else:
                student = Student(course_code, title, lecturer, major, max_capacity, current_enrolled)
                students.append(student)
                print("Student successfully added")
                break
            

#to check if the course exists or not
def checkCourse(course_code):
    if courses==[]:
        return "none"
    for course in courses:
        if(course.getCourseCode() == course_code):
            return course
        else:
            return "none"


#to check if the student exists or not
def checkStudent(student_id):
    if students ==[]:
        return "none"
    for student in students:
        if(student.getStudentId() == student_id):
            return student
        else:
            return "none"


#to check if the student is already in course or not
def checkStudentinCourse(course_check, student_id):
    for id in course_check.students:
        if id == student_id:
            return False
    return True


#to display graph
def displayGraph():
    course_name = []
    course_student = []
    course_max=[]
    for course in courses:
        course_name.append(course.getTitle())
        course_student.append(course.getCurrentEnrolled())
        course_max.append(course.getMaxCapacity())

    plt.plot(course_name, course_student, 'o-')       
    plt.plot(course_name, course_max, '--')
    plt.title('Course Graph')
    plt.xlabel('Course Name')
    plt.ylabel('Number of Students')

    plt.legend(['Current Number Enrolled','Max Capacity'])
    plt.grid(True)
    plt.show()



#main function
user_input=True
while(user_input):
    user_input1 = input("Do you want to still in the system? (Y/N) ")
    while(user_input1.lower()!='y' and user_input1.lower()!='n'):
        user_input1 = input("Do you want to still in the system? (Y/N) ")
    if(user_input1.lower() =='y'):
        user_input = True
    else:
        user_input = False
        break

    x=input("Welcome. What do you want to do? \n1.Add course \n2.Add student \
        \n3.Print course details \n4.Print student information \n5.Check course available slot \
        \n6.Enroll student to a course \n7.Display graph \n")

    while(x!='1' and x!='2' and x!='3' and x!='4' and x!='5' and x!='6' and x!='7'):
        x=input("Please re-input your choice. \n1.Add course \n2.Add student \
        \n3.Print course details \n4.Print student information \n5.Check course available slot \
        \n6.Enroll student to a course \n7.Display graph \n")

    if(x=='1'):
        course_code = input("Enter course code: ")
        title = input("Enter course title: ")
        lecturer = input("Enter course lecturer: ")
        major = input("Enter major for the course: ")
        max_capacity = int(input("Enter course maximum capacity: "))
        current_enrolled = int(input("Enter course current enrolled students: "))
        while(max_capacity < current_enrolled):
            current_enrolled = int(input("Re-Enter course current enrolled students: "))
        result = AddCourse(course_code, title, lecturer, major, max_capacity, current_enrolled)

    elif (x=='2'):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        courses_enrolled = int(input("Enter student's number of course enrolled: "))
        student_major = input("Enter student major: ")
        AddStudent(student_id, name, courses_enrolled, student_major)

    elif(x=='3'):
        course_code = input("Enter code of the course you want to print: ")
        check_result= checkCourse(course_code)
        if (check_result=="none"):
            print("Course not found")
        else:
            check_result.courseDetails()
    
    elif(x=='4'):
        student_id = input("Enter ID of the student you want to print: ")
        check = checkStudent(student_id)
        if (check=='none'):
            print("Student not found")
        else:
            check.studentDetails()
    
    elif(x=='5'):
        course_code = input("Enter the code of the course you want to check availability for: ")
        check_result = checkCourse(course_code)
        if (check_result=='none'):
            print("Course not found")
        else:
            check_result.checkAvailableSlot()
    
    elif(x=='6'):
        student_id = input("Enter ID of the student you want to enroll: ")
        course_code = input("Enter the code of the course you want to enroll: ")
        student_check = checkStudent(student_id)      
        course_check = checkCourse(course_code)        

        if (student_check=="none"):
            print("Student not found")
            
        else:
            if (course_check=="none"):
                print("Course not found")
                
            else:
                student_in_course = checkStudentinCourse(course_check, student_id)    
                if(student_in_course == False):
                    print(f"{student_check.getName()} is already in {course_check.getTitle()}")
                else:
                    major = student_check.getStudentMajor()
                    course_check.enrollStudent(major, student_check.getName())
    
    elif(x=='7'):
        displayGraph()