userWeight = input("Enter your Weight: ")
unitInput = input("(L)bs or (K)g: ")
oneLbs = 0.453592
oneKg = 2.20462
result = 0
unit = ""
if unitInput.lower() == "l":
    result = oneLbs * float(userWeight)
    unit = "Kg"
elif unitInput.lower() == "k":
    result = oneKg * float(userWeight)
    unit = "Lbs"

else:
    print("Invalid input.")
print(f"your weight is: {result} {unit}")