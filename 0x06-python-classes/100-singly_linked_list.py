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
        new_node = Node(value)
        # Special case for the empty linked list
        if self.__head is None:
            new_node.next = self.__head
            self.__head = new_node

        # Special case for head at end
        elif self.__head.data >= new_node.data:
            new_node.next = self.__head
            self.__head = new_node

        else:

            # Locate the node before the point of insertion
            current = self.__head
            while(current.next is not None and current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node
        print("added node: {} -> {}".format(new_node, new_node.next))

    def __str__(self):
        res = ""
        tmp = self.__head
        print("head: {} -> {}".format(self.__head, self.__head.next_node))
        while (tmp):
            res += "{}\n".format(tmp)
            print("str")
            print(tmp)
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
