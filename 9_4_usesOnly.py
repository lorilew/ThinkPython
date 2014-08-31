def uses_only(word,string):
    """
    This function returns true if all the letters
    in word exist in string.
    """
    is_true = None
    word = word.lower()
    string = string.lower()
    for char in word:
        for c in string:
            if char == c:
                is_true = True
                break
            else:
                is_true = False
        if not is_true:
            break
    return is_true

word = "The red fox jumped over the lazy dog"
string = "qwertyuiopasdfghjklzxcvbnm "
print(uses_only(word,string))

        
    
