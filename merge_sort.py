
def merge_sort(input_list):
    '''
    Divide and merge
    O(n logn) time
    O(n) space 
    '''

    if len(input_list) <= 1:
        return input_list

    left_list, right_list = split(input_list)
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(left_list, right_list)


def split(input_list):
    '''
    Divide step
    O(log n) time
    '''
    mid = len(input_list) // 2

    return input_list[:mid], input_list[mid:]

def merge(left_list, right_list):
    '''
    Merge step
    O(n) time
    '''
    l = []
    i = j = 0

    while i<len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            l.append(left_list[i])
            i += 1
        else:
            l.append(right_list[j])
            j += 1
    while i < len(left_list):
        l.append(left_list[i])
        i += 1
    while j < len(right_list):
        l.append(right_list[j])
        j += 1
    return l

def verify_sort(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return True
    return input_list[0] <= input_list[1] and verify_sort(input_list[1:])

input_list = [2,7,1,5,3,0,5,4]

result = merge_sort(input_list)

print(result)
print(verify_sort(result))
print(verify_sort(input_list))