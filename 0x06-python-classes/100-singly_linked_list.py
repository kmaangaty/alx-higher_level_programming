#!/usr/bin/python3
""" Node class Define"""


class Node:
    """Node represented"""
    def __init__(self, data, next_node=None):
        """Initialize a new class.
        Args:
            data (int): parameter of type int.
            next_node (Node): parameter of type Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter or setter for  the data of the Node."""
        return (self.__data)

    @property
    def next_node(self):
        """getter or setter for  the data of the Node."""
        return (self.__next_node)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList represented"""
    def __init__(self):
        """Initialize SinglyLinkedList class."""
        self.__head = None

    def sorted_insert(self, value):
        """function.
        Args:
            value (Node): parameter of type node.
        """
        nd = Node(value)
        if self.__head is None:
            nd.next_node = None
            self.__head = nd
        elif self.__head.data > value:
            nd.next_node = self.__head
            self.__head = nd
        else:
            mok = self.__head
            while (mok.next_node is not None and
                    mok.next_node.data < value):
                mok = mok.next_node
            nd.next_node = mok.next_node
            mok.next_node = nd

    def __str__(self):
        """ function """
        values = []
        mok = self.__head
        while mok is not None:
            values.append(str(mok.data))
            mok = mok.next_node
        return ('\n'.join(values))
