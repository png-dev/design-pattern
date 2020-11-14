from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self) -> None:
        self.name: str = ''

    @abstractmethod
    def factory_method(self):
        pass


class Student(Person):
    def factory_method(self):
        return Student()


class Teacher(Person):
    def factory_method(self):
        return Teacher()
