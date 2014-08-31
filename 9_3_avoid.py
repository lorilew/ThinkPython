def avoids(word, avoid_string):
    """
    This funtion returns true if word contains the
    substring avoid_string.
    """
    word = word.lower()
    avoid_string = avoid_string.lower()
    #print(word, avoid_string)
    length = len(word)
    i = 0
    has_avoid = False
    while i<len(word) and not has_avoid:
        if word[i] == avoid_string[0]:
            if word[i:i+len(avoid_string)] == avoid_string:
                has_avoid = True
            else:
                has_avoid = False
        i+=1
    return has_avoid
        

avoid_string = input("Input a string of letters to avoid:")
fin = open('words.txt')
t = 0
s = 0
for line in fin:
    t+=1
    word = line.strip()
    if(not avoids(word,avoid_string)):
        s+=1
print(t-s, "words contain", avoid_string)
