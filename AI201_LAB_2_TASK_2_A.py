rows=int(input("Enter Number of Rows for The Pattern \n"))

for i in range(rows):
    print(" "*(rows-i), "*"*(i*2+1))
for i in range(rows, -1, -1):
    print(" "*(rows-i), "*"*(i*2+1))