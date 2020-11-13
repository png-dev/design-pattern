import copy


class Student(object):

    def __init__(self, name: str = 'PNG', age: int = 10):
        self.name = name
        self.age = age

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    student1 = Student('Phong', 23)
    print(student1.name)
    student2 = student1.clone()
    print(student2.name)
