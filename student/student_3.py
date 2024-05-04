#student.py
#https://www.geeksforgeeks.org/student-management-system-in-python/
class Student:
    #class attribute
    students = []
    def __init__(self,sid:str=None,sname:str=None,smajor:str=None) -> None:
        self.sid = sid
        self.sname = sname
        self.smajor = smajor
        self.sindex = None
    
    def newstudent(self,sid:str,sname:str,smajor:str):
        newstudent = Student(sid,sname,smajor)
        Student.students.append(newstudent)
    
    def searchstudent(self,sid:str):
        for i in range(len(Student.students)):
            if Student.students[i].sid == sid:
                print('---- Searching Student Info ----')
                self.showinfo(i)
                self.sindex = i
                break
    def updateinfo(self,sid:str,sname:str,smajor:str):
        self.searchstudent(sid)
        Student.students[self.sindex].sname = sname
        Student.students[self.sindex].smjor = smajor
        print('---- Updating Student Info ----')
        self.showinfo(self.sindex)

    def showinfo(self,index:int):
        print(f'Student id: {Student.students[index].sid}')
        print(f'Student name: {Student.students[index].sname}')
        print(f'Major: {Student.students[index].smajor}')
    
    def allstudent(self):
        print('---- All Students ----')
        for i in range(len(Student.students)):
            self.showinfo(i)
            print('------------------')

if __name__ == '__main__':
    dpustudent = Student()
    dpustudent.newstudent('66123','Somchai Jaidee','ITDS')
    dpustudent.newstudent('66157','Manee Chaiyo','ACC')
    dpustudent.newstudent('66452','Pawat Kongled','LAW')
    dpustudent.allstudent()
    dpustudent.searchstudent('66157')
    dpustudent.updateinfo('66452','Supakorn Kongled','ITDS')
