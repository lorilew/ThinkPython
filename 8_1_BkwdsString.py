def go_backwards(s):
    index = 1
    while index <= len(s):
        letter = s[len(s)-index]
        print(letter)
        index+=1

go_backwards("Lauren")

