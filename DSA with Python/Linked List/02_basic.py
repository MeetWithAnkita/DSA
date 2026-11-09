class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
'''
Code	            Meaning
self.data = data	Stores the node's value
self.next = None	Initially, it doesn't point to another node
'''
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
# Traverse a linked list
current = head
while current is not None:
    print(current.data, end = "->")
    current = current.next
print("None")