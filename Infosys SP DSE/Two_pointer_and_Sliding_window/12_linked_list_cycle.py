'''
Linked List Cycle

Given the head of a linked list, determine whether the linked list contains a cycle.
'''

class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
# cycle
node4.next = node3
# head create
head = node1

def check_cycle_linked_list(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next
        if slow == fast:
            return True 
    return False

print(check_cycle_linked_list(head))