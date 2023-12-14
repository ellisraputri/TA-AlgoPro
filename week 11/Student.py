class Student:
    def __init__(self, student_id, name, courses_enrolled, student_major):
        self.__student_id = student_id
        self.__name = name
        self.__course_enrolled = courses_enrolled
        self.__student_major = student_major

        f = open("mystudent.txt", 'at')	
        f.write(f"\nStudent Details: \nStudent ID:{self.__student_id}      \
              \nName: {self.__name}  \nCourse Enrolled: {self.__course_enrolled}    \
              \nStudent Major: {self.__student_major}")
        f.close()
    
    #get function
    def getStudentId(self):
        return self.__student_id
    def getName(self):
        return self.__name
    def getCourseEnrolled(self):
        return self.__course_enrolled
    def getStudentMajor(self):
        return self.__student_major
    
    #set function
    def setStudentId(self, student_id):
        self.__student_id = student_id
    def setName(self, name):
        self.__name = name
    def setCourseEnrolled (self, courses_enrolled):
        self.__course_enrolled = courses_enrolled
    def setStudentMajor(self, student_major):
        self.__student_major = student_major

    def studentDetails(self):
        print(f"Student Details: \nStudent ID:{self.__student_id}      \
              \nName: {self.__name}  \nCourse Enrolled: {self.__course_enrolled}    \
              \nStudent Major: {self.__student_major}")
