''' Q.6- Print the following patterns:
*
**
***
****
'''

for i in range(5):
    for j in range(1,i+1):
        print("*",end="")
    print('\n')
