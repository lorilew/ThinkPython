def counter(s,l):
    count = 0
    index = 0
    while index < len(s):
        if s[index] == l:
            count+=1
        index+=1
    return count

word = "banana"
letter = "a"

print(counter(word,letter))
print(word.count(letter))
