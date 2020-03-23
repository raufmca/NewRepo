
#Sum of arrays function

def sumArray(lst1):
    sum=0
    for i in lst1:
        sum = sum + i
    print(f'Sum of list item = ', sum)



s = int(input("Enter the size of array " ))

lst1=[]
while s != 0:
    i = int(input("Enter you number = "))
    lst1.append(i)
    s = s-1

sumArray(lst1)

