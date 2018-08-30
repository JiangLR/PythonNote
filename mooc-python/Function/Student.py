from parent import Human


class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)
        self.name = name
        self.age = age

    def dohomework(self):
        super(Student, self).dohomework()
        print("english homework")


student1 = Student("ZUCC", "JiangLR", 20)
student1.dohomework()
