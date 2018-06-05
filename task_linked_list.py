class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



class LinkedList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.len = 0
        for elements in args:
            self.add(elements)

    def __str__(self):
        if self.head is not None:
            current = self.head
            res = str(current.value)
            while current.next:
                current = current.next
                res = res + str(current.value)
            return 'LinkedList({})'.format(res)
        else:
            return 'LinkedList()'

    def add(self, *value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = self.tail = Node(value)

    def insert(self, index, value):
        if index == 0:
            newnode = Node(value)
            newnode.next = self.head
            self.head = newnode
        elif index >= self.len:
            self.add(value)
        else:
            current = self.head
            count = 0
            while current is not None:
                if count == index - 2:
                    break
                else:
                    count += 1
                    current = current.next
            newnode = Node(value)
            newnode.next = current.next
            current.next = newnode

    def get(self, index):
        current = self.head
        count = 0

        while current is not None:
            if self.index == count:
                return current.value
            current = current.next
            count += 1
        if index >= self.len:
            raise IndexError
        elif self.head is None:
            return
        else:
            current == self.head:
            count = 0
            return current.data
        count += 1
        current = current.next



if __name__ == '__main__':
    l = LinkedList(1, 2)
    l.get(1)
    print(l)




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


