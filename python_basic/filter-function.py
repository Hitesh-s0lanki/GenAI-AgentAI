import math
import package

numbers = [x for x in range(12)]

even_number = list(filter(lambda x: x%2==0, numbers))
print(even_number)

# prime or notin one line code
num = 5
print(len([x for x in range(2, int(math.sqrt(num)) + 1) if num % x == 0]) == 0)