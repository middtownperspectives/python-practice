# this is a python list, different from a python array, but similar to javascript arrays
new_list = [1, 2, 3, 'A', 'B', 'C']
new_array = []
result = new_list[0]

print(result)


if 1 in new_list:
    print(True)


for n in new_list:
    if n == 1:
        print(True)

    break

numbers = []

print(len(numbers))

numbers.append(2)
numbers.append(4)
numbers.append(10)

print(len(numbers))

print(numbers)

numbers.insert(1, 27)

print(numbers)

numbers.extend([4, 5, 6])

print(numbers)

numbers.remove(4)

print(numbers)
