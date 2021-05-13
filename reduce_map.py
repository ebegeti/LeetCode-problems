import functools

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 50, 40, 60, 70]
list3 = [10, 20, 30, 40, 50]

if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, list1, list2), True):
    print("The list1 and list2 are the same")
else:
    print("The list1 and list2 are not the same")

if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, list1, list3), True):
    print("The list1 and list3 are the same")
else:
    print("The list1 and list3 are not the same")