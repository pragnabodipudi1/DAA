from linked_list import linked_list

'''
Performing merge sort on singly linked list
'''

def merge_sort(input_sll):
    '''
    divide and merge 
    O(n log n) time
    '''

    if input_sll.size() == 1:
        return input_sll
    elif input_sll.head is None:
        return input_sll

    left, right = split(input_sll)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def split(input_sll):
    '''
    split the list
    O(log n) time
    '''

    if input_sll is None or input_sll.head is None:
        left = input_sll
        right = None
    
    else:
        mid = linked_list.size(input_sll) // 2
        mid_node = input_sll.index_value(mid-1)
        right = linked_list()

        left = input_sll
        right.head = mid_node.next_node
        mid_node.next_node = None

    return left, right

def  merge(left, right):
    '''
    Merge the list
    O(n) time
    '''

    sll = linked_list()
    sll.add(0)
    sll_head = sll.head
    left_head = left.head
    right_head = right.head

    while left_head and right_head:
        if left_head.data < right_head.data:
            sll_head.next_node = left_head
            left_head = left_head.next_node
        else:
            sll_head.next_node = right_head
            right_head = right_head.next_node
        sll_head = sll_head.next_node

    while left_head:
        sll_head.next_node = left_head
        left_head = left_head.next_node
        sll_head = sll_head.next_node

    while right_head:
        sll_head.next_node = right_head
        right_head = right_head.next_node
        sll_head = sll_head.next_node
    
    current = sll.head.next_node
    sll.head = current

    return sll

input_sll = linked_list()
input_sll.add(10)
input_sll.add(90)
input_sll.add(50)
input_sll.add(20)
input_sll.add(40)
input_sll.add(30)
input_sll.add(70)
input_sll.add(60)


print(merge_sort(input_sll))

    
    

