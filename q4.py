''' Q.4- From a list containing ints, strings and floats, make three lists to store them separately  '''

l1=['apple',1,3.2,'banana','grapes',10,66.6,11,'oranges',4.0,'peaches',5]

l2=[]
l3=[]
l4=[]

for index in range(len(l1)):
	if type(l1[index])==str:
		l2.append(l1[index])
	elif type(l1[index])==int:
		l3.append(l1[index])
	elif type(l1[index])==float:
		l4.append(l1[index])
print(l2)
print(l3)
print(l4)
