class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head

        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        
        if current is None:
            print("Data not found.")
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.display()  

    llist.prepend(5)
    llist.display() 

    llist.delete(20)
    llist.display()  
