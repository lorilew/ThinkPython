def rotate_word(string,i):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rot_alpha = alpha[i:]+alpha[:i]
    new_word = ""
    for char in string:
        print(char)
        if char == " ":
            print("space")
            return None
        else:
            new_word = new_word + rot_alpha[alpha.find(char)]
    return new_word
        

print(rotate_word("melon",-10))


