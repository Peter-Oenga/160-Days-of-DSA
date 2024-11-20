# Python program to find the second largest element in the array
# using one traversal

# function to find the second largest element in the array

def getSecondLargest(arr):
    n = len(arr)

    largest = -1
    second_largest = -1

    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]

    return second_largest
    

if __name__ == '__main__':
    arr = [12,43,54,23,56,64,65,74]
    print(getSecondLargest(arr))