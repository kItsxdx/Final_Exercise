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

# 1. ฟังก์ชันสำหรับลบข้อมูลนักเรียน

   def delstudent(self, sid):
        """Deletes a student from the list based on ID"""
        student = self.searchstudent(sid)
        if student:
            student_index = student.sindex
            del Student.students[student_index]
            # Update student indexes after deletion
            for student in Student.students[student_index:]:
                student.sindex -= 1


# ตัวอย่างการใช้งาน
    delstudent("123456")


# 2. ฟังก์ชันสำหรับเรียงลำดับข้อมูลนักเรียน
def sortbyname(self):
    """Sorts the student list by name"""
    Student.students.sort(key=lambda student: student.sname)


def sortbymajor(self):
    """Sorts the student list by major"""
    Student.students.sort(key=lambda student: student.smajor)


# ตัวอย่างการใช้งาน
sortbyname()
sortbymajor()

 
# 3. ฟังก์ชันสำหรับบันทึกข้อมูลนักเรียนไปยังไฟล์
def savetofile(self, filename):
    """Saves the student list to a CSV file"""
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Student ID", "Name", "Major"])
        for student in Student.students:
            writer.writerow([student.sid, student.sname, student.smajor])


# ตัวอย่างการใช้งาน
savetofile("students.csv")


# 4. ฟังก์ชันสำหรับโหลดข้อมูลนักเรียนจากไฟล์
def loadfromfile(self, filename):
    """Loads the student list from a CSV file"""
    with open(filename, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip header
        for row in reader:
            Student(row[0], row[1], row[2])


# ตัวอย่างการใช้งาน
loadfromfile("students.csv")
