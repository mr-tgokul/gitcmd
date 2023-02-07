def find_index(list, object):
    for i, obj in enumerate(list):
        if obj == object:
            return i
    return -1


my_list = [1, 2, 3, 4, 5]
object = 3
index = find_index(my_list, object)
print(index) # Output: 2
