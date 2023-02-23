class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # create a set to store the values in the union
    union_set = set()

    # traverse the first linked list and add the values to the set
    current_node = llist_1.head
    while current_node:
        union_set.add(current_node.value)
        current_node = current_node.next

    # traverse the second linked list and add the values to the set
    current_node = llist_2.head
    while current_node:
        union_set.add(current_node.value)
        current_node = current_node.next

    # create a new linked list with the values in the union set
    union_list = LinkedList()
    for value in union_set:
        union_list.append(value)

    return union_list

def intersection(llist_1, llist_2):
    common = dict()
    output = LinkedList()

    curr = llist_1.head
    while curr is not None:
        common[curr.value] = True
        curr = curr.next

    curr = llist_2.head
    while curr is not None:
        if curr.value in common:
            output.append(curr.value)
            del common[curr.value] # remove deplicates from output
        curr = curr.next

    return output


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3]
element_2 = [3, 4]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) #
print (intersection(linked_list_1,linked_list_2))
# Test Case 2

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [6, 6, 6]
element_2 = [6, 6, 6, 7]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) #
print (intersection(linked_list_1,linked_list_2))
# Test Case 3


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) #
print (intersection(linked_list_1,linked_list_2))

