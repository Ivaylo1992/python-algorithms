from math import sqrt


def jump_search(numbers, val):
    length = len(numbers)
    jump = int(sqrt(length))
    left, right = 0, 0

    while left < length and numbers[left] <= val:
        right = min(length - 1, left + jump)
        if numbers[left] <= val <= numbers[right]:
            break
        left += jump

    if left >= length or numbers[left] > val:
        return -1

    right = min(length - 1, right)
    i = left

    while i <= right and numbers[i] <= val:
        if numbers[i] == val:
            return i
        i += 1

    return -1


print(jump_search([1, 2, 3, 4, 5, 6, 7, 8], 8))
