def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    higher = []
    lower = []

    for item in arr:
        if item > pivot:
            higher.append(item)

        else:
            lower.append(item)

    print(arr)
    return quick_sort(lower) + [pivot] + quick_sort(higher)


arr = [18, 100, 70, 64, 19, 90, 93, 8, 33, 92]
print(quick_sort(arr))