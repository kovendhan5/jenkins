class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  
    

    def append(self, data):
        new_node = Node(data)  

        if self.head is None: 
            self.head = new_node
        else:
            current = self.head 
 
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  
  
    def print_list(self):
        current = self.head 
        while current:
            print(current.data, end=" -> ") 
            current = current.next  
        print("None")  # End of the list


    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next  
            current = None  # Free old head
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
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)


linked_list.print_list()  

linked_list.delete(20)

linked_list.print_list()
