#!/usr/bin/python3
"""Node class"""


class Node:
    """Definition of a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self._next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __str__(self):
        node = self._head
        string = ""
        while node:
            string += f"{node.data}\n"
            node = node.next_node
        return string.strip()

    def sorted_insert(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
            return

        previous_node = None
        current_node = self._head
        while current_node and value > current_node.data:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            new_node.next_node = self._head
            self._head = new_node
        else:
            new_node.next_node = current_node
            previous_node.next_node = new_node
