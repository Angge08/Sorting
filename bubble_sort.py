def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

        print(arr)


arr = [18, 100, 70, 64, 19, 90, 93, 8, 33, 92]
bubble_sort(arr)
print(arr)