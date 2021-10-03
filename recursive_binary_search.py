
def binary_search(input_list, target):
    if len(input_list) == 0:
        return 'Not Found'
    else:
        midpoint = len(input_list) // 2
        if input_list[midpoint] == target:
            return 'Found'
        elif input_list[midpoint] < target:
            return binary_search(input_list[midpoint+1:], target)
        else:
            return binary_search(input_list[:midpoint], target)

input_list = [1,2,3,4,5,6,7,8,9,10]
target = 2

print(binary_search(input_list, target))
