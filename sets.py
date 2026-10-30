numbers = {10, 20, 30, 40, 50}
print(numbers)
print(type(numbers))

numbers = [10, 20, 10, 30, 20, 40]
print(set(numbers))

fruits = {"apple", "banana", "mango"}
fruits.add("orange")
print(fruits)


numbers = {1, 2, 3, 4}
numbers.remove(3)
print(numbers)


numbers = {10, 20, 30, 40}
if 20 in numbers:
    print("Element exists")
else:
    print("Element does not exist")

numbers = {10, 20, 30, 40, 10}
print(len(numbers))

fruits = {"apple", "banana", "mango"}
for fruit in fruits:
    print(fruit)

#union
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)

#intersecton
A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)

#diifrence
A = {1, 2, 3}
B = {3, 4, 5}
print(A - B)
print(B - A)

#subset
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))


# common elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(set(list1) & set(list2))


# missing numbers
numbers = {1, 2, 4, 6, 7}
expected = set(range(1, 8))
print(expected - numbers)

# numbers occuring obly once
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(set(list1) ^ set(list2))