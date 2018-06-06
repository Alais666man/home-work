class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, *args):
        self.head = None
        self.last = None
        self.len = 0
        for i in args:
            self.add(i)

    def __str__(self):
        linkedList = 'LinkedList '
        node = self.head
        if self.head is None:
            return 'Linked list is empty'
        for i in range(self.len):
            if node == self.last:
                linkedList += (str(node.value))
            else:
                linkedList += (str(node.value) + ', ')
            cell = node.next
        return linkedList

    def add(self, value):
        self.len += 1
        if self.head is None:
            self.last = self.head = Node(value, None)
        else:
            self.last.next = self.last = Node(value, None)

    def insert(self, index, value):
        if index == 0:
            self.len += 1
            if self.head is None:
                self.head = Node(value, None)
                self.last = self.head
            else:
                self.head = Node(value, self.head)
                return

        # if index >= self.len:
        #     self.add(value)
        # else:
        #     count = 0
        #     node = self.head
        #     while node is not None:
        #         count += 1
        #         if count == index:
        #             node.next = Node(value, node.next)
        #             self.len += 1
        #             if node.next.next is None:
        #                 self.last = node.next
        #                 self.len += 1
        #             break
        #         node = node.next

    def get(self, index):
        if index >= self.len:
            raise IndexError

        count = -1
        node = self.head
        while node is not None:
            count += 1
            if count == index:
                return node.value
            node = node.next
    # def len(self):
    #     return self.len



if __name__ == '__main__':
    ll = LinkedList(1, 2, 3, 4, 5)

    print(ll)


    # class Node:
    #     def __init__(self, value):
    #         self.value = value
    #         self.next = None
    #
    #
    #  def len(self):
    #     current = self.head
    #     total = 0
    #     while current.next is not None:
    #         total += 1
    #         current = current.next
    #     return total
    #
    # class LinkedList:
    #     def __init__(self, *args):
    #         self.head = Node(args)
    #         for values in args:
    #             self.add(values)
    #
    #
    #     def add(self, value):
    #         new_node = Node(value)
    #
    #         if self.head is None:
    #             self.head = new_node
    #             return
    #
    #         last_node = self.head
    #         while last_node.next:
    #             last_node = last_node.next
    #         last_node.next = new_node

    #

    #
    # def get(self, index):
    #     if index >= self.len():
    #         raise IndexError
    #     current_index = 0
    #     current_node = self.head
    #     while True:
    #         current_node = current_node.next
    #         if current_index == index:
    #             return current_node.value
    #         current_index += 1
    #
    # def remove(self, value):
    #     previous = None
    #     current = self.head
    #     while current:
    #         if current.get_value() == value:
    #             if previous:
    #                 previous.set_next(current.get_next())
    #             else:
    #                 self.head = current.get_next()
    #             return True
    #
    #         previous = current
    #         current = current.get_next()
    #
    #     return False











    # def insert(self, index, value):
    #     if index >= self.len():
    #         return self.add(value)
    #     else:
    #         current = self.head
    #         prior_node = self.head
    #         current_index = 0
    #         while True:
    #             current =
    #             if current_index == index:
    #                 new_node = Node(value)
    #                 prior_node.next = new_node
    #                 new_node.next = current
    #                 # return
    #
    #                 prior_node = current
    #                 current_index += 1


















# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
#
# class LinkedList:
#     def __init__(self, *args):
#         self.head = None
#         self.tail = None
#         self.len = 0
#         for elements in args:
#             self.add(elements)
#
#     def __str__(self):
#         if self.head is not None:
#             current = self.head
#             res = str(current.value)
#             while current.next:
#                 current = current.next
#                 res = res + str(current.value)
#             return 'LinkedList({})'.format(res)
#         else:
#             return 'LinkedList()'
#
#     def add(self, *value):
#         if self.head is None:
#             self.tail = self.head = Node(value)
#         else:
#             self.tail.next = self.tail = Node(value)
#
#     def insert(self, index, value):
#         if index == 0:
#             newnode = Node(value)
#             newnode.next = self.head
#             self.head = newnode
#         elif index >= self.len:
#             self.add(value)
#         else:
#             current = self.head
#             count = 0
#             while current is not None:
#                 if count == index - 2:
#                     break
#                 else:
#                     count += 1
#                     current = current.next
#             newnode = Node(value)
#             newnode.next = current.next
#             current.next = newnode
#
#     def get(self, index):
#         current = self.head
#         count = 0
#
#         while current is not None:
#             if self.index == count:
#                 return current.value
#             current = current.next
#             count += 1
#         if index >= self.len:
#             raise IndexError
#         elif self.head is None:
#             return
#         else:
#             current == self.head:
#             count = 0
#             return current.data
#         count += 1
#         current = current.next
#
#
#
# if __name__ == '__main__':
#     l = LinkedList(1, 2)
#     l.get(1)
#     print(l)




    # class LinkedList(object):
    #     def __init__(self):
    #         self.first = None
    #         self.last = None
    #         self.len = 0
    #
    #     def __str__(self):
    #         result = ''
    #         if self.first is not None:
    #             current_node = self.first
    #             result += 'LinkedList' + str(current_node.value)
    #             while current_node.next is not None:
    #                 current_node = current_node.next
    #                 result += str(current_node.value)
    #             return result
    #         return result
    #
    #     def add(self, *value):
    #         self.len += 1
    #         if self.first is None:
    #             self.last = self.first = Node(value, None)
    #         else:
    #             self.last.next = self.last = Node(value, None)
    #
    #     def insert(self, index, value):
    #         if self.first is Node:
    #             self.last = self.first = Node(value, None)
    #             return
    #         elif index == 0:
    #             self.first = Node(value, self.first)
    #             return
    #         curr = self.first
    #         count = 0
    #         while curr is not None:
    #             count += 1
    #             if count == index:
    #                 curr.next = Node(value, curr.next)
    #                 if curr.next.next is None:
    #                     self.last = curr.next
    #                 break
    #             curr = curr.next
    #
    #
    # class IndexError(Exception):
    #     pass
    # def get(self, index, value):
    #     current_node = self.first
    #     if current_node.get_next() >= self.len:
    #         raise IndexError
    #     elif current_node.get_next() == index:
    #         return value
    #
    # def remove(self, value):
    #     current_node = self.first
    #     prev_node = None
    #     while current_node is not None:
    #         if current_node.get_value() == value:
    #             if prev_node is not None:
    #                 prev_node.set_next(current_node.get_next())
    #             else:
    #                 self.first = current_node.get_next()
    #             self.len -= 1
    #             return True
    #         else:
    #             prev_node = current_node
    #             current_index = current_index.get_next()
    #     return False


    # def clear(self):
    #     self.__init__()

    # if not isinstance(value, Node):
    #     value = Node(value)
    # if self.head is None:
    #     self.head = value
    # else:
    #     self.tail.next = value
    # self.tail = value


