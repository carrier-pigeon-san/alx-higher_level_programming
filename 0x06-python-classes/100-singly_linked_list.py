#!/usr/bin/python3
class Node:
    """
    defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None:
            if not isinstance(value, Node):
                raise TypeError('next_node must be a node object')
        self.__next_node = value

class SinglyLinkedList:
    """
    defines a singly linked list
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value, None)
        if self.__head is None or value <= self.__head.data:
            node.next_node = self.__head
            self.__head = node
        else:
            this_node = self.__head;
            while (this_node.next_node is not None and value > this_node.next_node.data):
                this_node = this_node.next_node
            node.next_node = this_node.next_node
            this_node.next_node = node

    def __repr__(self):
        node = self.__head
        node_list = []
        while node:
            node_list.append(str(node.data))
            node = node.next_node
        return '\n'.join(node_list)
