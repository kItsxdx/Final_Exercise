class Student:
    students = []  # Class attribute to store all students

    def __init__(self, sid, sname, smajor):
        self.sid = sid
        self.sname = sname
        self.smajor = smajor
        # Assign index based on current student list length
        self.sindex = len(Student.students)
        Student.students.append(self)  # Add student to the list

    def searchstudent(self, sid):
        """Searches for a student by ID and returns the student object if found"""
        for student in Student.students:
            if student.sid == sid:
                return student
        return None  # Return None if student not found

    def updateinfo(self, sid, sname, smajor):
        """Updates a student's information based on ID"""
        student = self.searchstudent(sid)
        if student:
            student.sname = sname
            student.smajor = smajor

    def showinfo(self, index):
        """Prints student information based on index in the student list"""
        student = Student.students[index]
        print(f"Student id: {student.sid}")
        print(f"Student name: {student.sname}")
        print(f"Major: {student.smajor}")

    @classmethod
    def allstudents(cls):
        """Calls showinfo for all students in the list"""
        for i in range(len(cls.students)):
            cls.showinfo(i)


# Example usage
student1 = Student("123456", "John Doe", "Computer Science")
student2 = Student("654321", "Jane Doe", "Mathematics")

# Print all students
Student.allstudents()
print(f'test')
