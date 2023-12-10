class Course:
    def __init__(self,course_code, title, lecturer, major, max_capacity, current_enrolled):
        self.__course_code = course_code
        self.__title = title
        self.__lecturer = lecturer
        self.__major = major
        self.__max_capacity = max_capacity
        self.__current_enrolled = current_enrolled
        self.students=[]

        f = open("mycourse.txt", 'at')	
        f.write(f"\nCourse Details: \nCourse code:{self.__course_code}      \
              \nTitle: {self.__title}  \nLecturer: {self.__lecturer}    \
              \nCourse Major: {self.__major} \nMax Capacity: {self.__max_capacity}  \
              \nCurrent enrolled student: {self.__current_enrolled}.\n\n")
        f.close()
            
    #Get function
    def getCourseCode(self):
        return self.__course_code
    def getTitle(self):
        return self.__title
    def getLecturer(self):
        return self.__lecturer
    def getMajor(self):
        return self.__major
    def getMaxCapacity(self):
        return self.__max_capacity
    def getCurrentEnrolled(self):
        return self.__current_enrolled
    
    #Set function
    def setCourseCode(self, course_code):
        self.__course_code = course_code
    def setTitle(self, title):
        self.__title = title
    def setLecturer (self, lecturer):
        self.__lecturer = lecturer
    def setMajor(self, major):
        self.__major = major
    def setMaxCapacity(self, max_capacity):
        self.__max_capacity = max_capacity
    def setCurrentEnrolled(self, current_enrolled):
        self.__current_enrolled = current_enrolled
    
    #enroll student
    def enrollStudent(self, student_major, student_name):
        if(self.__major == student_major):
            if(self.__current_enrolled == self.__max_capacity):
                print("\nSorry, the course is already full")
            else:
                print(f"\nCongrats, {student_name}! You've been successfully enrolled!")
                self.setCurrentEnrolled(self.__current_enrolled + 1)
                self.students.append(student_name)

        else:
            print("\nSorry, your major is not aligned with this course")
    
    #display course details
    def courseDetails(self):
        print(f"\nCourse Details: \nCourse code:{self.__course_code}      \
              \nTitle: {self.__title}  \nLecturer: {self.__lecturer}    \
              \nCourse Major: {self.__major} \nMax Capacity: {self.__max_capacity}  \
              \nCurrent enrolled student: {self.__current_enrolled}.")
        

    #check available slot
    def checkAvailableSlot(self):
        if(self.__current_enrolled == self.__max_capacity):
            print(f"\nSorry course {self.__title} is already full")
        else:
            print(f"\nThe available slot for {self.__title} is {self.__max_capacity - self.__current_enrolled}")