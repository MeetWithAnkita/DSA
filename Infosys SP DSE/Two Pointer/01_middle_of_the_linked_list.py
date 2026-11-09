class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None 
# manually create linked list...................

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1

def middle_node(head):
    slow = head 
    fast = head
    while (fast is not None) and (fast.next is not None):
        slow = slow.next 
        fast = fast.next.next 
    return slow.data

print("Middle Node: ",middle_node(head))