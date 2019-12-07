from os import system, name
from datetime import time


availableCourses = []
studentsEnrolled = []
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Admin:
    #admin username and password
    username = ""
    password = ""
    
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def setPassword(self, newPassword, enteredPassword):
        if enteredPassword != self.password:
            print("Wrong password entered.")
        else:
            self.password = newPassword
            print("Password changed successfully.")

    def createCourse(self, crsCode, crsName, crsWeight, reqs, maxStuds, hrStart, minStart, hrEnd, minEnd):
        availableCourses.append(Course(crsCode, crsName, crsWeight, maxStuds, reqs, hrStart, minStart, hrEnd, minEnd))

    def removeCourse(self, reqCourse):
        bFound = int(0)
        for x in availableCourses:
            if reqCourse == x.courseCode:
              availableCourses.remove(x)
              bFound = int(1)
            else:
                pass
        return bFound

    def viewCourses(self):
        print(">>>>>> View All Courses <<<<<<")
        for x in availableCourses:
            print("Course Name: ", x.courseName)
            print("Course Code: ", x.courseCode)
            print("Course Weight: ", x.courseWeight)
            print("Start Time: ", x.start_time, "End Time: ", x.end_time)
            print("====================================================")

class Student:
    # username and password
    username = ""
    password = ""
    maxUnits = int(21)
    courseList = []
    currUnits = int(0)
    currClasses = int(0)
    prioEnrollment = False #doesn't really matter for now 

    def __init__(self, name, password):
        self.username = name
        self.password = password

    def setPassword(self, newPassword, enteredPassword):
        if enteredPassword != self.password:
            print("Wrong password entered.")
        else:
            self.password = newPassword
            print("Password changed successfully.")

    def addCourse(self, course):
        bVal = int(0)
        crsReq = None
        for x in availableCourses:
            if(course == x.courseCode):
                bVal = int(1)
                crsReq = x
        if bVal is 1:
            crsWeight = crsReq.courseWeight
            crsEnrolled = crsReq.currEnrolled
            crsMax = crsReq.maxStudents
            if crsWeight + self.currUnits <= self.maxUnits and crsEnrolled < crsMax:
                self.courseList.append(crsReq)
                self.currUnits += crsWeight
                self.currUnits += 1
                crsReq.currEnrolled += int(1)
                
            else:
                print("You're adding too many courses!")
        else:
            pass
        return bVal       
    def removeCourse(self, courseReq):
        self.courseList.remove(courseReq)
    
    def changeMaxUnits(self, newMax):
        if newMax >= 12:
            self.maxUnits = newMax
        else:
            print("Higher value, please.")

class Course:
    #course code and course name
    courseCode = int(0)
    courseName = ""
    courseWeight = int(3)
    preReqs = []
    preReqTo = []
    currEnrolled = int(0)
    maxStudents = int(45)

    start_time = time(hour = 0, minute = 0)
    end_time = time(hour = 1, minute = 30)

    def __init__(self, crsCode, crsName, crsWeight, maxStuds, reqs, hrStart, minStart, hrEnd, minEnd):
        self.courseCode = crsCode
        self.courseName = crsName
        self.courseWeight = crsWeight
        self.preReqs = reqs
        self.maxStudents = maxStuds
        self.start_time = time(hour = hrStart, minute = minStart)
        self.end_time = time(hour = hrEnd, minute = minEnd)

    def changeWeight(self, newWeight):
        self.courseWeight = newWeight

def findReq(admin, currCourse):
    clear()
    reqExit = False
    preReqs = []
    while reqExit is False:
        clear()
        print(">>>>>> Adding Pre-Requisites <<<<<<")
        print("[1] Add a pre-requisite to this course.")
        print("[2] Remove a pre-requisite to this course.")
        print("[3] View all pre-requisites")
        print("[3] Done.")
        reqChoice = int(input("Your Choice: "))

        if reqChoice is 1:
            admin.viewCourses()
            reqCourse = input("Enter course code of the pre-requisite: ")
            bFound = int(0)
            for x in availableCourses:
                if x.courseCode == reqCourse and len(availableCourses) != 0 and currCourse != reqCourse:
                    preReqs.append(x)
                    bFound == int(1)
            if bFound is 1:
                input("Pre-requisite is added! Press enter to continue.")
            else:
                input("Pre-requisite does not exist. Press enter to continue")

        elif reqChoice is 2:
            for x in preReqs:
                print("Course Name: ", x.courseName)
                print("Course Code: ", x.courseCode)
                print("Course Weight: ", x.courseWeight)
                print("Start Time: ", x.start_time, "End Time: ", x.end_time)
                print("====================================================")
            
            reqRemove = input("Enter course code of the pre-requisite to remove: ")
            bFound = 0
            for x in preReqs:
                if reqRemove == x.courseName:
                    preReqs.remove(x)
                    bFound = 1
            if bFound is 1:
                input("Pre-requisite is removed! Press enter to continue.")
            else:
                print("Pre-requisite does not exist. Press enter to continue")


        elif reqChoice is 3:
            for x in preReqs:
                print("Course Name: ", x.courseName)
                print("Course Code: ", x.courseCode)
                print("Course Weight: ", x.courseWeight)
                print("====================================================")
        elif reqChoice is 4:        
            reqExit = True
        else:
            pass
        
        if reqExit is True:
            break

    return preReqs

def viewAllCourses():
    clear()
    print(">>>>>> View All Courses <<<<<<")
    for x in availableCourses:
        print("Course Name: ", x.courseName)
        print("Course Code: ", x.courseCode)
        print("Course Weight: ", x.courseWeight)
        print("Start Time: ", x.start_time, "End Time: ", x.end_time)
        print("====================================================")

def viewEnrolled(student):
    clear()
    print(">>>>>> View All Courses <<<<<<")
    for x in student.courseList:
        print("Course Name: ", x.courseName)
        print("Course Code: ", x.courseCode)
        print("Course Weight: ", x.courseWeight)
        print("Start Time: ", x.start_time, "End Time: ", x.end_time)
        print("====================================================")

def asAdmin(admin):
    clear()
    preReqs = []
    bExit = False

    while bExit is False:
        clear()
        print(">>>>>> Admin Menu <<<<<<")
        print("[1] Create a Course.")
        print("[2] Remove a Course.")
        print("[3] View All Courses.")
        print("[4] Back to Main Menu.")
        nChoice = int(input("Your Choice: "))

        if nChoice is 1:
            crsCode = input("Course Code: ")
            crsName = input("Course Name: ")
            maxStudents = int(input("Max Students: "))
            crsWeight = int(input("Course Weight: "))
            hrStart = int(input("From (Hour): "))
            minStart = int(input("From (Minute): "))
            hrEnd = int(input("To (Hour): "))
            minEnd = int(input("To (Minute): "))

            preReqs = findReq(admin, crsName)

            clear()
            print(">>>>>> Course Details <<<<<<")
            print("Course Code: ", crsCode)
            print("Course name: ", crsName)
            print("Max Students: ",  maxStudents)
            print("Course Weight: ", crsWeight)
            print("Start: ", hrStart,minStart)
            print("End: ", hrEnd, minEnd)

            admin.createCourse(crsCode, crsName, crsWeight, preReqs, maxStudents, hrStart, minStart, hrEnd, minEnd)
            input("Added successfully! Press Enter to continue.")
            pass
        elif nChoice is 2:
            admin.viewCourses()
            reqCourse = input("Enter Course Code to remove: ")
            bVal = admin.removeCourse(reqCourse)
            #won't throw an error since it can remove none
            if bVal is 1:
                input("Removed successfully! Press Enter to continue.")
            else:
                input("Course does not exist.")

        elif nChoice is 3:
            clear()
            admin.viewCourses()

            input("Press Enter to Continue.")
        elif nChoice is 4:
            bExit = True
        else:
            pass


def asStudent(student):
    clear()
    bExit = False
    while bExit is False:
        print(">>>>>> Student Menu <<<<<<")
        print("[1] Add a Course.")
        print("[2] Drop a Course.")
        print("[3] View Available Courses.")
        print("[4] View Enrolled Courses.")
        print("[5] Exit.")
        nChoice = int(input("Your Choice: "))

        if nChoice is 1:
            courseReq = input("Enter Desired Course (Code): ")
            bFound = student.addCourse(courseReq)
            
            if bFound is 1:
                
                input("Successfuly added! Press enter to continue.")
            else:
                input("Course does not exist. Press enter to continue.")
        elif nChoice is 2:
            viewEnrolled(student)
            courseReq = input("Enter Course to Drop (Code): ")
            crsDel = None
            bFound = int(0)
            for x in student.courseList:
                if courseReq == x.courseCode:
                    bFound = int(1)
                    crsDel = x
            if bFound is 1:
                student.removeCourse(crsDel)
                input("Successfully removed! Press enter to continue.")
            else:
                input("Course does not exist. Press enter to continue.")             
        elif nChoice is 3:
            viewAllCourses()
            input("Press enter to continue.")
        elif nChoice is 4:
            viewEnrolled(student)
            input("Press enter to continue.")
        elif nChoice is 5:
            bExit = True
        else:
            pass

bExit = False
nChoice = int(0)

admin = Admin("admin", "password")
#main menu
while True:
    clear()
    print(">>>>>> Welcome to Animo.Sys <<<<<<")
    print("[1] Sign-in as Admin")
    print("[2] Sign-in as Student")
    print("[3] Create a Student Account")
    print("[4] Exit.")
    nChoice = int(input("Your Choice: "))
    
    if nChoice is 1:
        adminReq = input("Enter admin username: ")
        passReq = input("Enter admin password: ")
        if(passReq == admin.password and adminReq == admin.username):
            asAdmin(admin)
        else:
            clear()
            input("Something doesn't match. Press enter to go back to the main menu.")
            pass
    elif nChoice is 2:
        studentName = input("Enter username: ")
        studentPass = input("Enter password: ")
        stud = None
        bFound = int(0)
        for x in studentsEnrolled:
            if x.username == studentName and x.password == studentPass:
                stud = x
                bFound = int(1)
        if bFound is 1:
            asStudent(stud)
        else:
            input("Something doesn't match. Try again.")
    elif nChoice is 3:
        clear()
        bConfirmed = False
        while bConfirmed is False:
            clear()
            print(">>>>>> Create a Student Account <<<<<<")
            studUsername = input("Enter Desired Username: ")
            studPass = input("Enter Desired Password: ")
            confirmPass = input("Please Confirm Password: ")

            if(studPass == confirmPass):
                studentsEnrolled.append(Student(studUsername, studPass))
                clear()
                input("Account made successfully! Press enter to go back to the main menu.")
                bConfirmed = True
            else:
                clear()
                input("Passwords don't match! Press enter to try again")
           
    elif nChoice is 4:
        bExit = True
    else:
        pass

    if bExit is True:
        break