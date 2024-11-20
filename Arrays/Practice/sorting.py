
# Python program to find second largest element in an array
# using Sorting

def getSecondLargest(arr):

    arr.sort()
    n  = len(arr)

    for i in range(n-2, -1, -1):

        if arr[i] != arr[n-1]:
            return arr[i]
        
    return -1
    
if __name__ == '__main__':
    arr = [12, 23, 34, 54, 23, 42, 543]
    print(getSecondLargest(arr)) 