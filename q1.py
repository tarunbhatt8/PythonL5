# Q.1- Take 10 integers from user and print it on screen.

print("Taking 10 integers as input:")
l1=[]
for i in range(10):
	element=int(input("Enter integer no.{}: ".format(i+1)))
	l1.append(element)
print("The entered integers are:")
print(l1)
