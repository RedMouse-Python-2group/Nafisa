import csv
import collections

with open("shop_7.csv","r") as csv_file:
    csv_Reader = csv.reader(csv_file, delimiter=';')
    for row in csv_Reader:
        import pprint
        pprint.pprint(row)

print('-------------------------------------------------------')

measurement = collections.Counter()

with open("shop_7.csv","r") as csv_file:
    csv_Reader = csv.reader(csv_file, delimiter=';')
    for row in csv_Reader:
        measurement[row[1]]+=1

print("Total amount of products:")
x = measurement.most_common()
print x

outFile = open('shop_7.csv', "a")
writer = csv.writer(outFile, delimiter=";")
writer.writerow(['total', x])
outFile.close()

raw_input()

# In this homework i've used standart Python module 'collections' 
