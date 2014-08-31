prefixes = "JKLMNOPQ"
suffix= "ack"

for letter in prefixes:
    if letter=="Q" or letter=="O":
        letter = letter + "u"
    print(letter + suffix)

fruit = "banana"
print(fruit[:])
