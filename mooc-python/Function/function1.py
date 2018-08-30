class Student():
    # name = ''
    # age = 0
    sum1 = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__class__.sum1 += 1
        print(self.__dict__)

    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)


class Printer():

    def func(self):
        print("name:" + self.name)
        print("age:" + str(self.age))
