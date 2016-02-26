num = [x for x in range(1,10)]
print (num)

x = input("Choose your number\n") 

import mod

if x <=3:
    s = str(input("Enter several numbers\n"))
    n = int(input("How many times repeat?\n"))
    print mod.mult(s,n)

elif x in range(4,7):
    m = input("Raising to the power\n")
    second(x,m)

elif x in range(7,10):
    print mod.prog(x) 

else:
    print("Error")

raw_input()
