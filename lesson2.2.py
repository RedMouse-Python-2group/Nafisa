words = list(map(str,raw_input(" Enter some words\n ").split()))
maxword = " "
for element in words:
    if len(element) > len(maxword):
        maxword = element

print maxword


raw_input() 