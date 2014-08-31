def find(word,letter,index):
    """
    index: index in which to start looking
       includes that index number.
    """
    while index<len(word):
        if word[index] == letter:
            return index
        index+=1
    return -1

print("index:", find("potato","t",3))
