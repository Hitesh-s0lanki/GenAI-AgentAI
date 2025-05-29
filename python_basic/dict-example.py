# Intro { key : value } pair " key are always unique"

##Creating dictionaries
empty_dict = {}
print(type(empty_dict))

empty_dict = dict()
print(type(empty_dict))

student = {"name":"hitesh", "age":21, "grade":24}
print(student)

# No Error state
student = {"name":"hitesh", "age":21, "grade":24, "name":"Niraj"}
print(student)

## accessing dict element
print(student['name'])

## get method in dict
print(student.get("class", 0))

## Putting func

def func():
    print("Hello")

def func2(word):
    print("Hello ", word)

dict_example = {
    "hello": func,
    "hello2": func2
}

dict_example["hello2"]("world")

# deleting the value from dict
del dict_example["hello2"]

print(dict_example)

## Dictionary method
keys = student.keys()
values = student.values()

print(keys, values)

items = student.items()
print(items)


## Shallow copy -> 
student_copy = student
student_copy["name"] = "kapil"
print(student)

student_copy = student.copy()
student_copy["name"] = "hitesh"
print(student)

## loop for iteration the dictionaries

for key, value in student.items():
    print(key, " -> ", value)


## Nested Dict
nested = {
    "student1":{
        "name":"Hitesh"
    },
    "student2":{
        "name":"kapil"
    }
}

print(nested["student1"]["name"])

## Iterating over nested dict
for student_id, student_info in nested.items():
    print(student_id, end=" -> ")
    for key, value in student_info.items():
        print(key," -> ", value)


## Dict Comphrehension
squares = {x:x**2 for x in range(1, 11)}
print(squares)


## Find the frequency of element
members = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = {}

ans = {x: freq.get(x, 0) + 1 for x in members}

print(ans)