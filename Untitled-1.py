'''
class Person:
  def __init__(abc, name, age):
    abc.name = name
    abc.age = age

  def myfunc(tru):
    print(f"Hello my name is {tru.name}, I am {tru.age} years old.")

p1 = Person("John", 36)
p1.myfunc()

'''

arr = [10,9,8,7,6,5,4,3,2,1]

#for x in arr:
 # print(x)

for x in range(len(arr)):
  print(arr[x], end=" ") 

for x in range(len(arr)):
  for j in range(x+1, len(arr)):
    if (arr[x]>arr[j]):
      temp =arr[x]
      arr[x]=arr[j]
      arr[j]=temp

print("\n")

for x in range(len(arr)):
  print(arr[x], end=" ") 