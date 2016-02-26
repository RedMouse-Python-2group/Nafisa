

print('Welcom to "Crystal ball"')
print('------------------------')
x = raw_input('Ask you question\n')
import random
array = random.choice(["In the future", "Don't ask question you don't understand", "Reed more books", 
"Do you realy want to know it?", "You need some rest", "I'm sure something similar has been asked before", "I don't know", 
"I can't answer", "You shouldn't know it" ])
z = x + '-' + array
print (z)

raw_input() 