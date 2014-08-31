def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) == 0:
        print("You did not type anything")
        return None
    elif len(word)==1 or len(word)==2:
        if first(word) == last(word):
            return True
        else:
            return False
    else:
        if first(word) == last(word):
            return is_palindrome(middle(word))
        else:
            return False
        

print(is_palindrome("Lauren"))

