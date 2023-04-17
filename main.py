data_tuple = ('h', 6.13, 'C', 'e', "T", True, "k", "e", 3, 'e', 1, "g")
letters = []
numbers = []

for item in data_tuple:
    if type(item) == str:
        letters.append(item)
    elif type(item) == int:
        numbers.append(item)
    else:
        numbers.append(item)

numbers.pop(0)
letters.append(numbers.pop(0))
numbers.insert(1, 2)
numbers = tuple(sorted(i * i for i in numbers))
letters[-2], letters[1] = letters[-2].upper(), letters[1].lower()
letters.reverse()
print(letters)
print(numbers)
