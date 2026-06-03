class College:
    def college_name(self):
        print("SMVEC Engineering College")

class Student(College):
    def student_name(self):
        print("JOE")

obj = Student()

obj.college_name()
obj.student_name()

o/p:
SMVEC Engineering College
JOE
