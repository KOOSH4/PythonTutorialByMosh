Numbers = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}
user_Input = input("Enter a number (at least 3 digit): ")
for X in str(user_Input):
    print(Numbers[X])

#solution 2
numberInWord = ""
space = " "
for Y in str(user_Input):
    numberInWord = numberInWord + space + Numbers[Y]
print(numberInWord)