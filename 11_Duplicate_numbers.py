numbers = [5,8,2,3,12,4,9,3,18,8,10,6,10]
numbers_copy = numbers.copy()
duplicates = []
for X in numbers:
    if numbers.count(X) == 2:
        duplicates.append((X))
        numbers.remove(X)
print(f"The old list is: {numbers_copy}")
print(f"New list without duplicates is: {numbers}")
print(f"Deleted numbers: {duplicates}")