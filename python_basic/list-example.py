fruits = ["apple", "mango", "banana"]

fruits.pop(0)

print(fruits)

# iterating over list
for [index, fruit] in enumerate(fruits):
    print(index, " -> ", fruit)

ans = [x**2 for x in range(10)]
print(ans)

even = [x for x in range(10) if x%2==0]
print(even)

# Nested list Comphrension
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

print([[i, j] for i in list1 for j in list2])