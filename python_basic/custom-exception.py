class Error(Exception):
    pass

class DobException(Error):
    pass

year = 2013
age = 2025 - year

try:
    if age <= 30 and age >= 20:
        print("The age is valid so you can apply for the exam")
    else:
        raise DobException
except DobException:
    print("Sorry your age is not within the range ")