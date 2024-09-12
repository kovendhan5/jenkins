class Node:
    def __init__(self, data):
        self.data = data  # data node
        self.next = None  # Pointer to next node (initially None)


class LinkedList:
    def __init__(self):
        self.head = None  # head of the linked list

    # Add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with  data
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            current = self.head  # Start from the head of the list
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node

    # Print the entire list in a readable format
    def print_list(self):
        current = self.head  # Start from the head node
        while current:
            print(current.data, end=" -> ")  # Print the current node's data
            current = current.next  # Move to the next node
        print("None")  # End of the list

    # Delete the first node with the given data
    def delete(self, data):
        current = self.head

        # If the head node itself holds the key to be deleted
        if current and current.data == data:
            self.head = current.next  # Change head to next node
            current = None  # Free the old head
            return

        # Search for the node to be deleted, keep track of the previous node
        prev = None
        while current and current.data != data:
            prev = current  # Move the previous pointer to current
            current = current.next  # Move to the next node

        # If the data was not found
        if current is None:
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None  # Free the memory of the deleted node

# Create a new linked list
linked_list = LinkedList()

# Add elements to the linked list
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)


linked_list.print_list()  

linked_list.delete(20)

linked_list.print_list()
