class Student:
    students = []  # Class attribute to store all students

    def __init__(self, sid, sname, smajor):
        self.sid = sid
        self.sname = sname
        self.smajor = smajor
        # Assign index based on current student list length
        self.sindex = len(Student.students)

        Student.students.append(self)  # Add student to the list

    def newstudent(self, sid, sname, smajor):
        """add new student information"""
        new_student = Student(sid, sname, smajor)
        print(
            f"add new student information already completed:{new_student}")

    def searchstudent(self, sid):
        """Searches for a student by ID and returns the student object if found"""
        for student in Student.students:
            if student.sid == sid:
                print(f"*****Information Student*****")
                print(f"ID Student:{student.sid}")
                print(f"Name Student:{student.sname}")
                print(f"Major:{student.smajor}")
                student.showinfo(student.sindex)
                return

        # Return None if student not found
        print(f"Could not find student information with ID :{sid}")

    def updateinfo(self, sid, sname, smajor):
        """Updates a student's information based on ID"""
        for student in Student.students:
            if student.sid == sid:
                student.sname = sname
                student.smajor = smajor
                print(
                    f"$$$$$$$$$$$Update student information already completed$$$$$$$$$$")
                student.showinfo(student.sindex)
                return
        print(f"Could not find student information with ID: {sid}")

    def showinfo(self, index):
        """Prints student information based on index in the student list"""
        print(f"*******Student Information*******")
        print(f"Student id: {Student.students[index].sid}")
        print(f"Student name: {Student.students[index].sname}")
        print(f"Major: {Student.students[index].smajor}")

    def allstudent(self):
        """Calls showinfo for all students in the list"""
        for student in Student.students:
            student.showinfo(student.sindex)


# Example usage
dpustudent = Student(None, None, None)

# add student information
dpustudent.newstudent(66123, "Somchai Jaidee", "ITDS")
dpustudent.newstudent(66157, "Manee Chaiyo", "ACC")
dpustudent.newstudent(66452, "Pawat Kongled", "LAW")

# Print all students
dpustudent.allstudent()

# search student information
dpustudent.searchstudent(66257)

# update student informayion
dpustudent.updateinfo(66452, "Supakorn Kingkong", "ITDsss")

# search student information
dpustudent.searchstudent(66452)
