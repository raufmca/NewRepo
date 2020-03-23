'''
sorting of an list
'''

myList = [9,3,5,10,0,2,4,13,7,6]
print("My list {}".format(myList))

n = len(myList)

for i in range(n):
    
    for j in range(1, n-i):
        
        if myList[j] < myList[j-1]:
            (myList[j],myList[j-1])=(myList[j-1], myList[j])

print(f"Sorted List {myList}")
