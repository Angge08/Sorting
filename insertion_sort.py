def insertion_sort(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = element

        print(arr)

arr = [18, 100, 70, 64, 19, 90, 93, 8, 33, 92]
insertion_sort(arr)
print(arr)