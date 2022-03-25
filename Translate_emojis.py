emojies = {
    ":(" : "🙁",
    ":)" : "😀"
}
newText = ""
userInput = input("Type...")
text = userInput.split()
for X in text:
   newText +=  emojies.get(X, X) + " " # get methode : search for a value and replace it. if it doesnt exist, it replace it with a default value in second argument.
print(newText)
