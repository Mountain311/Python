def count_n(s,n):
    
    list1=[]
    list2=[]
    list3=[]
    
    for i in range (0,len(s)-(n-1)):
        
        A=s[i:n+i]

        list1.append(A)
        
    list2=set(list1)
    

    frequency=0  
    
    for i in list2:
        
        frequency=0  
        
        for j in list1:
            
            if(i==j):
                
                frequency=frequency+1
                
        list3.append(frequency)
        
        
    zip_i=zip(list2,list3)
    
    dict1=dict(zip_i)
     
    print(dict1)
    

def count_2(s):
    
    n=2
    
    list1=[]
    list2=[]
    list3=[]
    
    for i in range (0,len(s)-(n-1)):
        
        A=s[i:n+i]

        list1.append(A)
        
    list2=set(list1)
    

    frequency=0  
    
    for i in list2:
        
        frequency=0  
        
        for j in list1:
            
            if(i==j):
                
                frequency=frequency+1
                
        list3.append(frequency)
        
        
    zip_i=zip(list2,list3)
    
    dict1=dict(zip_i)
     
    print(dict1)           
              
        
strvar=input("Enter String :\n")



try:
    global intvar
    intvar=int(input("Enter Integer :\n"))
except:
    
    intvar=3
    print("Value Entered not an Integer setting default to 3")
    
print("\n\n")

print("2 letter Sequences:\n")
count_2(strvar)

print("\n\n")

print("N letter Sequences:\n")
count_n(strvar,intvar)