# def fib_gen(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# # Example usage:
# for num in fib_gen(6):
#     print(num, end=" ")


## Example -> Reading Large file
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line 

file = read_large_file("example.txt")
print(file)

# for line in read_large_file("example.txt"):
#     print(line)