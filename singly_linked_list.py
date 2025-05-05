class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insert_last(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
    
    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete(self, target):
        if not self.head:
            return
        
        # case 1: delete head node.
        if self.head.val == target:
            self.head = self.head.next
            return
        # Case 2: delete non-head node.
        cur = self.head
        while cur.next:
            if cur.next.val == target:
                cur.next = cur.next.next
                return
            cur = cur.next
            
    def print_list(self):
        cur = self.head
        while cur:
            print(cur, end=' -> ')
            cur = cur.next
        print(None)
    
    
l1 = LinkedList()
l1.insert_last(1)
l1.insert_first("First")
l1.insert_first("Second")
l1.print_list()
l1.delete_first()
l1.print_list()
l1.delete("First")
l1.print_list()