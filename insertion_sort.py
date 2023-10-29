def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        current_num = arr[i]

        j = i - 1
        
        while j >= 0 and current_num < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current_num


arr = [64, 12, 33, 55, 25, 8]

print('Unsorted List:', arr )

insertion_sort(arr)
print('Sorted list:', arr)
