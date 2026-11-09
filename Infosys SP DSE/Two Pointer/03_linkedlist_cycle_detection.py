'''
If a cycle exists, the fast pointer will eventually catch 
up with the slow pointer.

If no cycle exists, the fast pointer will eventually reach 
None.
'''
class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 
node1 = Node(10) 
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# cylcle create 
node5.next = node2
# node5.next = None

head = node1

def valid_cycle_linkedlist(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next
        if slow == fast:
            return True 
    return False

print(valid_cycle_linkedlist(head))

'''
Complexity	    || Result
---------------------------
Time	        || O(n)
Auxiliary space	|| O(1)
'''

