def is_palindrome(word):
    backword = word[::-1]
    if len(word) == 0:
        return None
    elif word == backword:
        return True
    else:
        return False



print(is_palindrome(""))

