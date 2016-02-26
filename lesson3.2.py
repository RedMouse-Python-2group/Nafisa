def sep(i,x):
    for i in x:
        print i,'-', len(i)

y = list(map(str,raw_input("Enter some words\n").split()))
i=0
sep(i,y)

raw_input()
