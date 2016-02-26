
w = str('Python Java JavaScript  Ruby Pascal')
w.split()
print(w)

print("------------------------------------")

sym = raw_input("Enter symbol: \n")

import re
newline = re.sub(" +", sym, w)
newline.split(sym)

print(newline)

print("------------------------------------")

print min(newline, key = lambda element:len(element))

raw_input()  


