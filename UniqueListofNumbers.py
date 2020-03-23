'''
Function to return unique elements from list
'''

def uniqui_list(list1):
    ulist = []
    
    for x in list1:
        if x not in ulist:
            ulist.append(x)
    
    for x in ulist:
        print (x)

list1 = [1,2,3,4,3,2,3,7,8]

print(list1)
print("---------- Result -------- ")
uniqui_list(list1)

print('End of file and program')    