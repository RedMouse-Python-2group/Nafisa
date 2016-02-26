def first(x,y):
    print(x*y)

def second(x,y):
    print(x**y)

def third(x):
    z = 0
    while z < 10:
        x = x + 1
        z = z + 1
        print(x)
    
num = [x for x in range(1,10)]
print (num)

x = input("Choose your number\n") 

if x <=3:
   s = str(input("Enter several numbers\n"))
   n = int(input("How many times repeat?\n"))
   first(s,n) # вызов первой функции

elif x in range(4,7):
    m = input("Raising to the power\n")
    second(x,m) # вызов второй функции

elif x in range(7,10):
    third(x) # вызов третей функции

else:
    print("Error")

raw_input()
