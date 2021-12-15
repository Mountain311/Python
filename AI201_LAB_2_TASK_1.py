var=int(input("Enter value of Variable \n"))

bi=bin(var)

print(bi)

count1=bi.count("1")
count0=bi.count("0")

if (count1==1):
    print("The  Number is a Whole power of 2\n")
    
    print(f"The number is Equal to 2^{count0-1}")