words = ["apple", "banana", "grapes", "cat", "orange"]
result = list(filter(lambda word: len(word) > 5, words))
print(result)

numbers = [10, 55, 30, 70, 45, 90]
result = list(filter(lambda n: n > 50, numbers))
print(result)

numbers = [-5, 3, -2, 8, 0, 4]
result = list(filter(lambda n: n > 0, numbers))
print(result)


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11]

is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

result = list(filter(is_prime, numbers))
print(result)


numbers = [1, 2, 3, 4, 5]
result = list(map(lambda n: n * n, numbers))
print(result)


maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))


square = lambda n: n * n
print(square(5))


cube = lambda n: n * n * n
print(cube(3))