#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
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
        values = []
        mok = self.__head
        while mok is not None:
            values.append(str(mok.data))
            mok = mok.next_node
        return ('\n'.join(values))
