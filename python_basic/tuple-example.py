# intro to tuple
# order collection of item which are immutable

empty_tuple = ()
print(type(empty_tuple))
tpi = tuple()
print(type(tpi))

# example of tuple
exam = (1 ,2, 3, 4)

# exam[1] = 19 Error
print(exam)

print(exam[::-1]) # reverse of the tuple

print(exam * 3)

## Packing 
packed_tuple = 1, "Hello", 3.14
print(packed_tuple)

## unPacking
a, b, c = packed_tuple
print(a, b, c)

## unpacking with *
numbers= (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(first)
print(middle)
print(last)