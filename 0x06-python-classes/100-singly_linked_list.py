#!/usr/bin/python3
class SinglyLinkedList():
    """A single linked list of int nodes
    Attributes:
        head: head node of the list
    """
    def __init__(self):
        """Creates and empty list"""
        print("created list")
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in the list (sorted)"""
        print("head: {}".format(self.__head))
        if (self.__head == None):
            new_node = Node(value)
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node):
                tmp = tmp.next_node

            new_node = Node(value)
            tmp.next_node = new_node

        

    def __str__(self):
        res = ""
        tmp = self.__head
        while (tmp):
            res += "{}\n".format(tmp)
            tmp = tmp.next_node
        return(res)

class Node():
    """A node from a singly linked list of integers

    Attributes:
        data (int): data of the node
        next_node (Node): next node in the linked list
    """
    def check_values(self, data, node):
        """checks the value for the node"""
        """
        if (type(data) != int):
            raise TypeError("data must be an integer")
        #if ((node != None) and (type(node) != type(self))):
        #    raise TypeError("next_node must be a Node object")

        """
    def __init__(self, data=0, next_node=None):
        """data must be an integer"""
        self.check_values(data, Node)
        self.__data = data
        self.__next_node = next_node
        print("next_node: {}".format(self.__next_node))

    @property
    def data(self):
        """int: returns the data of the node"""
        return(self.__data)

    @data.setter
    def data(self, value):
        """int: sets data value of the node"""
        self.check_values(value, None)
        self.__data = value

    @property
    def next_node(self):
        """Node: returns next_node of the node"""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, node):
        """Node: sets the next_node of the node"""
        self.check_values(None, node)
        self.__next_node = node

    def __str__(self):
        return ("{}".format(self.__data))
