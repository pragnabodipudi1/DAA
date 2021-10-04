
class Node:
    next_node = data = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return 'data of the node is %s' %(self.data)


class linked_list:

    def __init__(self):
        self.head = None
    
    def isempty(self):
        return self.head == None

    def size(self):
        '''
        O(n) time, linear
        '''
        count  = 0
        current = self.head
        while(current):
            count+=1
            current = current.next_node
        return count
    
    def index_value(self, index):
        '''
        Return node at a specific position in list
        O(n) time 
        '''
        
        current = self.head
        pos = 0

        while pos < index:
            current = current.next_node
            pos += 1
        return current


    def add(self, data):
        '''
        Adding node at the beginning
        O(1) time
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        '''
        Searching for a specific node
        O(n)
        '''
        current = self.head
        while(current):
            if current.data == key:
                return 'Found'
            current = current.next_node
        return 'Not Found'
    
    def __repr__(self):
        '''
        Displays the linked list
        O(n)
        '''
        current = self.head
        nodes = []
        while(current):
            if current == self.head:
                nodes.append('[Head:%s]' %current.data)
            elif current.next_node == None:
                nodes.append('[Tail:%s]' %current.data)
            else:
                nodes.append('[%s]' %current.data)
            current = current.next_node
        
        return '->'.join(nodes)
    
    def insert(self, data, pos):
        '''
        Insert at a position
        O(n) for searching for the right position, O(1) for insertion operation
        '''
        if pos == 0:
            self.add(data)
        elif pos > 0:
            current = self.head
            new_node = Node(data)
            while(pos > 1):
                pos -= 1
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    
    def remove(self, key):
        '''
        Remove key from list
        O(n) for searching, O(1) for removing
        '''

        flag = False
        current = self.head
        previous = None

        while(current and not flag):
            if current.data == key:
                if current == self.head:
                    self.head = current.next_node
                else:
                    previous.next_node = current.next_node
                flag = True
            else:
                previous = current
                current = current.next_node
    
            
