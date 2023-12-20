#!/usr/bin/python3
"""defines classes Node and SiinglyLinkedList"""


class Node:
    """
    defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """instantiation of Node class with data and next_node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """attribute property for getting attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        """validate attribute is integer"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """next_node attribute property to get attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """validate attribute is object of Node class"""
        if value is not None:
            if not isinstance(value, Node):
                raise TypeError('next_node must be a node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    defines a singly linked list
    """

    def __init__(self):
        """instantiation of class with head"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts node in order of increaseing data value """
        node = Node(value, None)
        if self.__head is None or value <= self.__head.data:
            node.next_node = self.__head
            self.__head = node
        else:
            this_node = self.__head
            while (this_node.next_node is not None and
                    value > this_node.next_node.data):
                this_node = this_node.next_node
            node.next_node = this_node.next_node
            this_node.next_node = node

    def __repr__(self):
        """represents class objects as strings to be printable"""
        node = self.__head
        node_list = []
        while node:
            node_list.append(str(node.data))
            node = node.next_node
        return '\n'.join(node_list)
