def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted_lst = False
    
    while not sorted_lst:
        sorted_lst = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted_lst = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
                
    return list_a


print(bubble([4, 6, 8, 3, 2, 5, 7, 8, 9]))
