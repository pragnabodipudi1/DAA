
def binary_search(input_list, target):
    first = 0
    last = len(input_list)-1

    while(first <= last):
        mid_point = (first + last) // 2
        if input_list[mid_point] == target:
            return mid_point
        elif input_list[mid_point] < target:
            first = mid_point + 1
        else:
            last = mid_point - 1
    return None

input_list = [1,2,3,4,5,6,7,8,9,10]
target = 2

print(binary_search(input_list, target))

