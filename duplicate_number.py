numbers = [5,8,2,3,12,4,9,3,18,8,10,6,10]
for X in numbers:
    if numbers.count(X) == 2:
        numbers.remove(X)
print(numbers)