class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    def print_name(self):
        return self.__name

# _name  Protected variable        