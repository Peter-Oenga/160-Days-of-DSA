def naive_approach(arr):
    n = len(arr)

    temp = [] * n

    j = 0

    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1
        

        # Fill remaining positions in temp[] with zeros
        while j < n:
            temp[j] = 0
            j += 1

        # Copy all the elements from temp[] to arr[]
        for i in range(n):
            arr[i] = temp[i]
        

if __name__ == '__main__':
    arr = [12, 2, 4, 5, 5, 32, 54, 65, 76]
    naive_approach(arr)


    for num in arr:
        print(num, end=" ")
