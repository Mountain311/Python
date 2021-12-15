import math
import statistics

newinput= True

nlist=[]

while (newinput==True):
    
    
    choice=int(input("Enter (1) to input new Value: \nEnter (2) to Finalize List\n"))
    
    if (choice==1):
        value=int(input("Enter New Value for List:\n"))
        nlist.append(value)
        
    else:
        newinput=False
        
mean=(sum(nlist)/len(nlist))


          
print(f"Sum of Values in List = {sum(nlist)} ")
print(f"Product of Values in List = {math.prod(nlist)} ")
print(f"Maximum Value in List = {max(nlist)} ")
print(f"Miniimum Value in List = {min(nlist)} ")
print(f"Mean Value of List = {mean} ")
print(f"Standard Deviation of List = {statistics.stdev(nlist)} ")

