def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print('target found ', result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 9)
verify(result)


# def recursive_binary_search(list, target, start=0, end=None):
#     if end is None:
#         end = len(list) - 1
#     if start > end:
#         return -1

#     mid = (start + end) // 2

#     if target == list[mid]:
#         return mid
#     else:
#         if target < list[mid]:
#             return recursive_binary_search(list, target, start, mid-1)
#         else:
#             return recursive_binary_search(list, target, mid+1, end)
