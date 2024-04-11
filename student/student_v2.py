class Student:

    # คลาสแอททริบิวต์
    students = []

    def __init__(self, sid, sname, smajor):
        # แอททริบิวต์
        self.sid = sid
        self.sname = sname
        self.smajor = smajor
        self.sindex = len(Student.students)

        # เพิ่มวัตถุเข้าไปต่อท้าย students
        Student.students.append(self)

    def newstudent(self, sid, sname, smajor):
        """เพิ่มข้อมูลนักศึกษาใหม่"""
        new_student = Student(sid, sname, smajor)
        print(f"เพิ่มข้อมูลนักศึกษาใหม่ เรียบร้อยแล้ว: {new_student}")

    def searchstudent(self, sid):
        """ค้นหาข้อมูลนักศึกษาโดยใช้รหัสนักศึกษา"""
        for student in Student.students:
            if student.sid == sid:
                print(f"**ข้อมูลนักศึกษา**")
                print(f"รหัสนักศึกษา: {student.sid}")
                print(f"ชื่อนามสกุล: {student.sname}")
                print(f"สาขาวิชา: {student.smajor}")
                student.showinfo(student.sindex)
                return

        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {sid}")

    def updateinfo(self, sid, sname, smajor):
        """ปรับปรุงชื่อนามสกุล และสาขาวิชาของนักศึกษา"""
        for student in Student.students:
            if student.sid == sid:
                student.sname = sname
                student.smajor = smajor
                print(
                    f"$$$$$$$$$$$$$$$$$ปรับปรุงข้อมูลนักศึกษา เรียบร้อยแล้ว:$$$$$$$$$$$$$$$ ")
                student.showinfo(student.sindex)
                return

        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {sid}")

    def showinfo(self, index):
        """แสดงรายละเอียดข้อมูลนักศึกษา"""
        print(f"**ข้อมูลนักศึกษา**")
        print(f"รหัสนักศึกษา: {Student.students[index].sid}")
        print(f"ชื่อนามสกุล: {Student.students[index].sname}")
        print(f"สาขาวิชา: {Student.students[index].smajor}")

    def allstudent(self):
        """แสดงข้อมูลนักศึกษาทั้งหมด"""
        for student in Student.students:
            student.showinfo(student.sindex)


# สร้างวัตถุ และเรียกใช้เมธอดสำหรับคลาส Student

dpustudent = Student(None, None, None)

# เพิ่มข้อมูลนักศึกษาใหม่
dpustudent.newstudent(66123, "Somchai Jaidee", "ITDS")
dpustudent.newstudent(66157, "Manee Chaiyo", "ACC")
dpustudent.newstudent(66452, "Pawat Kongled", "LAW")

# แสดงข้อมูลนักศึกษาทั้งหมด
dpustudent.allstudent()

# ค้นหาข้อมูลนักศึกษา
dpustudent.searchstudent(66157)

# ปรับปรุงข้อมูลนักศึกษา
dpustudent.updateinfo(66452, "Supakorn Kongled", "ITDS")

# ค้นหาข้อมูลนักศึกษา
dpustudent.searchstudent(66452)
