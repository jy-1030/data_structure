class ListNode(object):
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_nodes(self):
        if not self.head: # if head is none
            print(self.head)
        node = self.head
        while node:
            end = " -> " if node.next else "\n"
            print(node.val, end=end)
            node = node.next
    
    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    
    #-------------------------------#
    def append(self, value):
        """
        Add a node to the end of the list
        """
        if not self.head:
            self.head = ListNode(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(value)


    def insert(self,index,value):
        """
        Insert a node into the list
        """

        if index >= self.size():
            self.append(value)
            return
        count = 0
        node = self.head
        previous = None

        while node:
            if count == index:
                if previous:
                    new_node = ListNode(value, previous.next)
                    previous.next = new_node
                else:
                    self.head = ListNode(value, node)
                return
            count += 1
            previous = node
            node = node.next

    def removeNode(self, index):
        """
        remove a node from the list (base on index)
        """
        count = 0
        node = self.head
        previous = None

        while node:
            if count == index :
                if previous :
                    previous.next = node.next
                    # node = node.next

                else:
                    self.head = node.next
                    # node = self.head

                return 
            
            else:
                count += 1
                previous = node
                node = node.next

    def removeValue(self, value, all=False):
        """
        remove the node from the the list (base on value)
        """
        node = self.head
        previous = None

        while node:
            if node.val == value:
                if previous:
                    previous.next = node.next
                    node = node.next
                else:
                    self.head = node.next
                    node = self.head
                if not all:
                    return
            else:
                previous = node
                node = node.next



            
#-----------------------------#
# create linked list
linked_list = LinkedList()

# create node and store values
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(1)



# link the list
linked_list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6



#--------------------------#
# print_nodes()
# linked_list.append(5)
# linked_list.insert(4,8)
# linked_list.removeValue(2)
# linked_list.removeValue(3, all=True)
linked_list.removeNode(3)
linked_list.print_nodes()

