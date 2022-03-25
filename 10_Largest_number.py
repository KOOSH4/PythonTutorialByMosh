numbers = [5,8,2,0,12,4,9,3,18,15,10,6]
largest = 0
for x in numbers:
    if x > largest:
        largest = x
print(f"{largest} is the largest number in the list!")