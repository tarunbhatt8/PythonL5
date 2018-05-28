# Q.5- Using range(1,101), make a list containing only prime numbers.



l1=[]
for i in range(1,101):
	c=0
	for j in range(1,i+1):
		if i%j==0:
			c+=1
	if c<=2:
		l1.append(i)

print(l1)
