class Node:
    data = None
    next_node = None

    '''
    An object for storing a single node of a linked list
    Modles two attributes: data and link to the next node in the list
    '''

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<Node data: %s' % self.data


class SinglyLinkedList:
    '''
    Singly linked list
        Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    '''

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        '''
        Returns the number of nodes in the list, in linear constant time BigO(1)
        '''
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        '''
        Adds new node at the head of the list
        this operation takes constant time BigO(1)
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        '''
        Search for first node tha contains data the matches the key
        Returns the Node or Node if not found
        this operation takes Linear time BigO(n)
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        '''
        inserts a new node containing data at index position
        insertion takes constant time O(1)
        but finting node at insertion point take linear time O(n)
        '''
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            prev_nd = current
            next_nd = current.next_node

            prev_nd.next_node = new
            new.next_node = next_nd

    def remove(self, key):
        '''
        Removes node containing data that matches the key
        Returns node or none if key does not exist
        Takes O(n) time
        '''
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)

# # additional practice will be to read at an index and remove at a specific index:
#     remove a linked list at index
#     read a linked list at index


# class Node:
#     """
#     An object for storing a single node in a linked list

#     Attributes:
#         data: Data stored in node
#         next_node: Reference to next node in linked list
#     """

#     def __init__(self, data, next_node = None):
#         self.data = data
#         self.next_node = next_node

#     def __repr__(self):
#         return "<Node data: %s>" % self.data

# class SinglyLinkedList:
#     """
#     Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

#     Attributes:
#         head: The head node of the list
#     """

#     def __init__(self):
#         self.head = None
#         # Maintaining a count attribute allows for len() to be implemented in
#         # constant time
#         self.__count = 0

#     def is_empty(self):
#         """
#         Determines if the linked list is empty
#         Takes O(1) time
#         """

#         return self.head is None

#     def __len__(self):
#         """
#         Returns the length of the linked list
#         Takesn O(1) time
#         """

#         return self.__count

#     def add(self, data):
#         """
#         Adds new Node containing data to head of the list
#         Also called prepend
#         Takes O(1) time
#         """

#         new_head = Node(data, next_node=self.head)
#         self.head = new_head
#         self.__count += 1

#     def search(self, key):
#         """
#         Search for the first node containing data that matches the key
#         Returns the node or `None` if not found
#         Takes O(n) time
#         """

#         current = self.head

#         while current:
#             if current.data == key:
#                 return current
#             else:
#                 current = current.next_node
#         return None

#     def insert(self, data, index):
#         """
#         Inserts a new Node containing data at index position
#         Insertion takes O(1) time but finding node at insertion point takes
#         O(n) time.
#         Takes overall O(n) time.
#         """

#         if index >= self.__count:
#             raise IndexError('index out of range')

#         if index == 0:
#             self.add(data)
#             return
#         if index > 0:
#             new = Node(data)
#             position = index
#             current = self.head

#             while position > 1:
#                 current = current.next_node
#                 position -= 1

#             prev_node = current
#             next_node = current.next_node

#             prev_node.next_node = new
#             new.next_node = next_node

#         self.__count += 1

#     def node_at_index(self, index):
#         """
#         Returns the Node at specified index
#         Takes O(n) time
#         """

#         if index >= self.__count:
#             raise IndexError('index out of range')

#         if index == 0:
#             return self.head

#         current = self.head
#         position = 0

#         while position < index:
#             current = current.next_node
#             position += 1

#         return current

#     def remove(self, key):
#         """
#         Removes Node containing data that matches the key
#         Returns the node or `None` if key doesn't exist
#         Takes O(n) time
#         """

#         current = self.head
#         previous = None
#         found = False

#         while current and not found:
#             if current.data == key and current is self.head:
#                 found = True
#                 self.head = current.next_node
#                 self.__count -= 1
#                 return current
#             elif current.data == key:
#                 found = True
#                 previous.next_node = current.next_node
#                 self.__count -= 1
#                 return current
#             else:
#                 previous = current
#                 current = current.next_node

#         return None

#     def remove_at_index(self, index):
#         """
#         Removes Node at specified index
#         Takes O(n) time
#         """

#         if index >= self.__count:
#             raise IndexError('index out of range')

#         current = self.head

#         if index == 0:
#             self.head = current.next_node
#             self.__count -= 1
#             return current

#         position = index

#         while position > 1:
#             current = current.next_node
#             position -= 1

#         prev_node = current
#         current = current.next_node
#         next_node = current.next_node

#         prev_node.next_node = next_node
#         self.__count -= 1

#         return current


#     def __iter__(self):
#         current = self.head

#         while current:
#             yield current
#             current = current.next_node


#     def __repr__(self):
#         """
#         Return a string representation of the list.
#         Takes O(n) time.
#         """
#         nodes = []
#         current = self.head
#         while current:
#             if current is self.head:
#                 nodes.append("[Head: %s]" % current.data)
#             elif current.next is None:
#                 nodes.append("[Tail: %s]" % current.data)
#             else:
#                 nodes.append("[%s]" % current.data)
#             current = current.next_node
#         return  '-> '.join(nodes)
