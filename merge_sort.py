def merge_sort(arr):
    if len(arr) > 1:
        leftElem = arr[:len(arr) // 2]
        rightElem = arr[len(arr) // 2:]

        merge_sort(leftElem)
        merge_sort(rightElem)
        i = 0
        j = 0
        k = 0

        while i < len(leftElem) and j < len(rightElem):
            if leftElem[i] < rightElem[j]:
                arr[k] = leftElem[i]
                i += 1
            else:
                arr[k] = rightElem[j]
                j += 1
            k += 1

        while i < len(leftElem):
            arr[k] = leftElem[i]
            i += 1
            k += 1

        while j < len(rightElem):
            arr[k] = rightElem[j]
            j += 1
            k += 1

    print(arr)


arr = [18, 100, 70, 64, 19, 90, 93, 8, 33, 92]
merge_sort(arr)
print(arr)