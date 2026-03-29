
print("Welcome to the Sentence-to-Binary Machine!")

sentence = input("Type a sentence: ")

binary_sentence = ""

for letter in sentence:
    binary_letter = format(ord(letter), "08b")
    binary_sentence += binary_letter + " "

print("Here is your binary code for '" + sentence + "':")
print(binary_sentence)
