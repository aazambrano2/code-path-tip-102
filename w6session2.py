

"""

u: find the middle of a linked list return second middle if even
m: fast and slow pointers
p:

fast -> head
slow - > head

while fast and fast.next:
    slow one
    fast two times

return slow

E:
T: O(N)
S: O(1)

"""

#I



class Node:
    def __init__(self, data, next=None):
        self.data = data
        
        self.next = next


# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()

def find_middle(head):

    if not head: return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.data

#test cases

list1 = Node(1,Node(2,Node(3,Node(4,Node(5)))))
list2 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))

#
print(find_middle(list1)) # 3
print(find_middle(list2)) # 4

"""
u: write a function if there is a cycle or not
m: fast and slow pointer tech
p:
    empty list: return head
    have a fast and slow pointer
    while fast and fast.next:
        slow one time
        fast two times
        if fast == slow:
        return True
    return False
"""
#I
def is_circular(head):
    if not head: return head
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
#R
# c1 -> c2 -> c3 -> c1
#                   s
#                   f

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

