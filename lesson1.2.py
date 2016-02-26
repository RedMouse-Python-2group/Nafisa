x = int(input("Enter number from 1 to 9\n"))
if x <=3:
   s = str(input("Enter several numbers\n"))
   n = int(input("How many times repeat?\n"))
   print(s*n)

elif 4 <= x <= 6:
    m = input("Raising to the power  \n")
    print x**m

elif 7 <= x <= 9:
    z = 0
    while z < 10:
        x = x + 1
        z = z + 1
        print(x)
else:
    print("Error")

raw_input()