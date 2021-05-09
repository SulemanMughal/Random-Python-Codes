def common_end(listA, listB):
    if listA[0] == listB[0] or listA[len(listA)-1] == listB[len(listB)-1]:
        return True
    return False

print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))
