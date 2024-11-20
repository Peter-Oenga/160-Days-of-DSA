def getSecondLargest(arr):
    n = len(arr)

    largest = -1
    second_largest = -1

    for i in range(n):

        if arr[i] > largest:
            largest = arr[i]

            
    for i in range(n):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
           
    return second_largest

if __name__ == '__main__':
    arr = [12, 32, 42, 31, 54,65, 76,23]
    print(getSecondLargest(arr))
    