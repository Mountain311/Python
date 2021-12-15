nlist=[]

for i in range (0,10,1):
    value=int(input(f"Enter Value {i+1} of 10 : \n"))
    nlist.append(value)
    
print ("The original list is : " +  str(nlist))
  
nlist.sort()

res = []
for i in nlist:
    if i not in res:
        res.append(i)
   
nlist=res    

print ("The List after of : " +  str(nlist))