a = [5,10,3,7,6]

b = [10,5,3,2,1,0]

def sortToAscending(array):
    y = len(array)
    z = array
    
    for n in range(y):
        if n == y - 1:
            break
        if z[n] > z[n+1]:
            z[n+1], z[n] = z[n], z[n+1]
        # else
            
            
    return z

sortedArray = sortToAscending(a)
print(sortedArray)
