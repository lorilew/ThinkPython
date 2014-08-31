import math

def eval_loop():
    print("Enter done to finish\n\n")
    i = "hi"
    while True:
        i = input("Input a string to evaluate:")
        if i == "done":
            break
        else:
            print(eval(i))

eval_loop()
        
    
