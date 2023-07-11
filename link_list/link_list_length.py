class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1 -> 2 -> 3 -> 4 -> 5 -> None
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

#-------------------link list 長度------------------------#
#第一種
def get_linked_list_length(head):
    length = 0
    current = head

    while current is not None:
        length += 1
        current = current.next

    return length

#第二種
def get_link_leng(head):
    if(head is None) :
        return 0
    else :
        return(1+get_link_leng(head.next))



# link list 长度
length1 = get_linked_list_length(head)
length2 = get_link_leng(head)

print("第一種link长度为:", length1)
print("第二種link长度为:", length2)


#-------------------link list 長度------------------------#

