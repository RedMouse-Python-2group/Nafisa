w = "Python;Java;JavaScript;Ruby;C"
print(w)
print("--------------------------------------------")
print(max(w.split(';'), key=lambda i: len(i)))

raw_input() 