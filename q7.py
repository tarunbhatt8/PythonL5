''' Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop. '''

dict={}

num=int(input("Enter no. of elements for adding in  dictionary"))

for j in range(num):

    n=input("Enter name and marks as name:marks of student" +str(j+1)+": ")

    li=n.split(':')

    dict[li[0]]=li[1]

print(dict)