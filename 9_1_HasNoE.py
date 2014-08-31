def has_no_e(fin):
    total = 0
    total_no_e = 0
    for line in fin:
        total += 1
        has_no_e = True
        for char in line:
            if char == "e":
                has_no_e = False
        if has_no_e:
            total_no_e += 1
    return int(total_no_e/total*100)

fin = open('words.txt')
print(has_no_e(fin))
