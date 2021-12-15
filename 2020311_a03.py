class  MyVector:
    
    def __init__(self, *dimensions):
        self.d_list=[]
        for i in dimensions:
            if type(i)!=type(1):
                raise Exception("Argument not an Integer")
            else:
                self.d_list.append(i)
    
    def __str__(self):
        return (str(self.d_list))
    
    def __len__(self):
        return (len(self.d_list))
    
    def __abs__(self):
        temp=0
        for i in self.d_list:
            temp=temp+(i**2)   
        return (temp)**0.5
    
    def __bool__(self):
        if (abs(self)<0 or len(self)==0):
            return False
        else:
            return True
        
    def __mul__(self,S):
        temp=[]
        for i in self.d_list:
            i=i*S
            temp.append(i)
        return MyVector(*temp)
    
    def __rmul__(self,S):
        temp=[]
        for i in self.d_list:
            i=i*S
            temp.append(i)
        return MyVector(*temp)
    
    def __add__(self,O):
        if len(self)==len(O):
            temp=[]
            for i in range(0,len(self)):
                temp.append(self.d_list[i]+O.d_list[i])
            return MyVector(*temp)
        
    def __getitem__(self, I):
        if I>=len(self):
            raise IndexError
        else:
            return self.d_list[I]
        
    def __setitem__(self,i,v):
        if type(v)!=type(1):
                raise TypeError
        elif i>=len(self):
            raise IndexError
        else:
            self.d_list[i]=v
    
    def __lshift__(self,rot):
        for  y in range(0,rot):
            temp=[]
            for i in self.d_list:
                temp.append(i)
            for i in range(1,len(self)):
                temp[i-1]=self.d_list[i]
            temp[len(self)-1]=self.d_list[0]
        return MyVector(*temp)
    
        


if __name__ == '__main__':

	#####################################
	## Builtins
	#####################################
	x0 = MyVector()
	# print() prints all the elements as below in comment
	print (x0)		# MyVector()

	# passing illegal type to constructor
	#xx = MyVector(33, 'str2') # raises 'ValueError' exception


	x1 = MyVector(3,5,99,0)
	# len() returns number of elements
	print (len(x1))	# 4
	# print() prints all the elements as below in comment
	print (x1)		# MyVector(3,5,99,0)

	# MyVector should can be used as an iterable in loops
	for elem in x1:
		print(elem)	# prints 3 5 99 0 on separte lines

	print(x1[2])	# 99
	#print(x1[5])	# raises 'IndexError' exception
	x1[2] = 33
	print(x1)		# MyVector(3,5,33,0)

	# abs() should return absolute value: sqrt(sum(square_of_each_elemnent))
	x2 = MyVector(3,4)
	print(abs(x2))	# 5.0


	# MyVector should be false if empty or abs()>0, otherwise true 
	if x1:	# True
		print("this line will print")
	if x0:	# True
		print("this line will NOT print")

	#####################################
	## Arithmetic
	#####################################
	x1 = MyVector(1,2,3)
	x2 = MyVector(4,5,6)
	# + should add corresponding elements and return result
	x3 = x1+x2
	print(x1)	# MyVector(1,2,3)	
	print(x2)	# MyVector(4,5,6)	
	print(x3)	# MyVector(5,7,9)

	x1 += x2
	print(x1)	# MyVector(5,7,9)
	print(x2)	# MyVector(4,5,6)	

	# * should multiply constant with each element
	x1 = MyVector(1,2,3)
	x2 = x1*3
	x3 = 3*x1
	print(x1)	# MyVector(1,2,3)	
	print(x2)	# MyVector(3,6,9)	
	print(x3)	# MyVector(3,6,9)


	# << should rotate elements
	x1 = MyVector(1,2,3)
	x2 = x1<<1
	print(x2) 	# MyVector(2,3,1)