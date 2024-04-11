class Student:
    def __init__(self, sid: int, sname: str, smajor: str, sindex: str) -> None:
        self.student_id = sid
        self.student_name = sname
        self.student_major = smajor
        self.student_index = sindex


students = []


def newstudent(sid, sname, smajor):
    student = Student(sid, sname, smajor)
    students.append(student)
    print(student)

    def searchstudent(sid):
