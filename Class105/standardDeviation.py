import math
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]

def mean(data):
    n = len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean

square_list=[]
for num in data:
    a=int(num) - mean(data)
    a**2
    square_list.append(a)

sum = 0 
for i in square_list:
    sum=sum+1
result = sum / (len(data)-1)
standardDeviation = math.sqrt(result)
print("Mean: ", result)