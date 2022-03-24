for word_4X in range(2):
    print("XXXXX")
    for word_2X in range(word_4X+1):
        print("XX")

print("\n")

numbers = [5,2,5,2,2]
for i in numbers:
    Word = ''
    for k in range(i):
        Word += 'X'
    print(Word)