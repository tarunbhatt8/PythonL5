''' Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list. '''

l1=[]
l2=[]
ch='y'
while ch=='y':
	el=int(input("Enter an integer input: "))
	l1.append(el)
	l2.append(el**2)
	ch=input("Want to enter more integers? y//n")

print("You entered the following integers: ")
print(l1)
print("The squares of entered integers are: ")
print(l2)

	
	
	
