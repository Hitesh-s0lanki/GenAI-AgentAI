try:
    result = 1/0
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    print("I m here")
finally:
    print("It is done")