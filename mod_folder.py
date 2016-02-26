num = [x for x in range(1,10)]
print (num)

x = input("Choose your number\n") 
import module

if x <=3:
   s = str(input("Enter several numbers\n"))
   n = int(input("How many times repeat?\n"))
   print module.mult(s,n)

elif x in range(4,7):
    m = input("Raising to the power\n")
    print module.exponent(x,m)

elif x in range(7,10):
    print module.prog(x)

else:
    print("Error")

raw_input()
