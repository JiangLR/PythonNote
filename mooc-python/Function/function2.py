class Student():
    # name = ''
    # age = 0
    sum1 = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__class__.sum1 += 1
        print(self.__dict__)

    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)

    @staticmethod
    def add():
        print("this is a static method")
        print(Student.sum1)
