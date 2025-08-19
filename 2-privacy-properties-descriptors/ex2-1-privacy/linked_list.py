class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.__size = 0

    def append(self, value):
        """Append a new node to the tail of the list O(1)"""
        self.__size += 1
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node


    def remove_tail(self):
        """Remove the tail node from the list O(1)"""
        if self.tail is None:
            return

        self.__size -= 1
        if self.tail == self.head:
            self.head = self.tail = None
            return

        to_delete = self.tail
        self.tail = to_delete.prev
        self.tail.next = None


    def get_data(self):
        data = []
        node = self.head
        while node:
            data.append(str(node.value))
            node = node.next
        return data

    def __str__(self):
        return " -> ".join(self.get_data()) if self.head else "List is empty"

    def size(self):
        return self.__size


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
print(list1.get_data(), str(list1.size()))
print(list1)