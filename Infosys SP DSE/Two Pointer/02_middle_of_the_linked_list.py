class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 

def create_linked_list(list):
    head = Node(list[0])
    current = head 

    for l in list[1:]:
        current.next = Node(l)
        current = current.next 
    return head 

def middle_element(head):
    slow = head 
    fast = head 
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
    return slow.data 

list = [10, 20, 30, 40, 50]
head = create_linked_list(list)
print(middle_element(head))


'''
Complexity	                        Result
--------------------------------------------
Time	                            O(n)
Auxiliary space for middle function	O(1)
Linked-list creation space	        O(n)
'''