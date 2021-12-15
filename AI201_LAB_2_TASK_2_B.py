rows=int(input("Enter Number of Rows for The Pattern \n"))


for i in range(rows+1):
    print(" "*(rows-i), end="")
    for num in range(i,0,-1):
        print(num, end="")
    for num in range(1,i,+1):
        print(num+1, end="")
    print()
    
for i in range(rows, -1, -1):
    print(" "*(rows-i+1), end="")
    for num in range(i-1,0,-1):
        print(num, end="")
    for num in range(1,i-1,+1):
        print(num+1, end="")
    print()