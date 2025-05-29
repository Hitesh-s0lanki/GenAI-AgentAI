numbers = [x for x in range(1, 11)]

# print(numbers)

# lazy loading techniques

iterator = iter(numbers)
print(iterator)

for i in iterator:
    print(i, end=" ")