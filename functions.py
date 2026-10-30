# # def count_vowels(s):
# #     count = 0

# #     for ch in s.lower():
# #         if ch in "aeiou":
# #             count = count + 1

# #     return count

# # print(count_vowels("Hello World"))

# def largest(numbers):
#     big = numbers[0]

#     for n in numbers:
#         if n > big:
#             big = n

#     return big

# print(largest([10, 25, 8, 40, 15]))


# def power(base, exponent):
#     return base ** exponent

# print(power(2, 3))



# def natural_sum(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#     return total

# print(natural_sum(5))


# def area_circle(r):
#     return 3.14 * r * r

# print(area_circle(5))


# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# print(is_prime(7))



# def simple_interest(p, r, t):
#     return (p * r * t) / 100

# print(simple_interest(1000, 5, 2))



# def greater(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print(greater(10, 20))

# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact

# print(factorial(5))