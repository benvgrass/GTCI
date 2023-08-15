# from educative.io (with some changes)
from linked_list_node import LinkedListNode


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    @classmethod
    def from_node(cls, node: LinkedListNode):
        new_list = cls()
        new_list.insert_node_at_head(node)
        return new_list

    @classmethod
    def from_list(cls, lst: list):
        new_list = cls()
        new_list.create_linked_list(lst)
        return new_list

    # insert_node_at_head method will insert a LinkedListNode at
    # head of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of insert at head method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


def linked_list_to_list(linked_list: LinkedList):
    head = linked_list.head
    result = []
    while head:
        result.append(head.data)
        head = head.next

    return result
