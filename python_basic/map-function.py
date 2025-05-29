numbers = [1, 2, 3, 4, 5, 6, 7]

square = lambda x:x*x

ans = list(map(square, numbers))
print(ans)

words = ['apple', 'banana', 'cherry']
upper_word = list(map(str.upper, words))
print(upper_word)