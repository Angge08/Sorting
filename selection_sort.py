def selection_sort(arr):

    for i in range (0, len(arr) - 1):
        minpos = i
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[minpos]:
                minpos = j

        arr[i], arr[minpos] = arr[minpos], arr[i]

        print(arr)

arr = [18, 100, 70, 64, 19, 90, 93, 8, 33, 92]
selection_sort(arr)
print(arr)
