## Variable length Arguments
## Positional and keywords arguments


## Positional 
def print_number(*args):
    for number in args:
        print(number, end=" ")
    print()

print_number(1, 2, 3, "hitesh")

## Keyword
def print_number(**kwargs):
    for key, value in kwargs.items():
        print(key, " -> ", value)

print_number(name="Hitesh", age=21)

