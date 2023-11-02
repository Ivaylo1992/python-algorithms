my_list = [-2, 3, 4, 7, 8, 9, 11, 13]

target = 20


def search(lst, goal):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) //2
        if lst[mid] == goal:
            return mid
        elif lst[mid] < goal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(search(my_list, target))