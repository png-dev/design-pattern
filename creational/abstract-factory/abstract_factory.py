from abc import ABC, abstractmethod
from sys import platform


class Button(ABC):

    @abstractmethod
    def paint(self):
        pass


class LinuxButton(Button):
    def paint(self):
        return 'Render a button in a Linux style.'


class WindowsButton(Button):
    def paint(self):
        return 'Render a button in a Windows style'


class MacOSButton(Button):
    def paint(self):
        return 'Render a button in a MacOS style'


if __name__ == '__main__':

    def abstract_factory():
        if platform == 'linux':
            factory = LinuxButton
        elif platform == 'darwin':
            factory = MacOSButton
        else:
            factory = WindowsButton
        return factory


    button = abstract_factory()
    result = button().paint()
    print(result)
