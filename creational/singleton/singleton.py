class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1, singleton2)
