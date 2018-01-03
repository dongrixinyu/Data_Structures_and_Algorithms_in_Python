# -*- coding=utf-8 -*-

import math
from stack_algorithms import Stack


class Node(object):
    def __init__(self, value, next=0):
        self.value = value
        self.next = next  # 指针


class LinkedList(object):
    # 链表的数据结构
    def __init__(self):
        self.head = 0  # 头部

    def __getitem__(self, key):
        if self.is_empty():
            print 'Linked list is empty.'
            return
        elif key < 0 or key > self.get_length():
            print 'The given key is wrong.'
            return
        else:
            return self.get_elem(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print 'Linked list is empty.'
            return
        elif key < 0 or key > self.get_length():
            print 'The given key is wrong.'
            return
        else:
            return self.set_elem(key, value)

    def init_list(self, data):  # 按列表给出 data
        self.head = Node(data[0])
        p = self.head  # 指针指向头结点
        for i in data[1:]:
            p.next = Node(i)  # 确定指针指向下一个结点
            p = p.next  # 指针滑动向下一个位置

    def get_length(self):
        p, length = self.head, 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.head == 0:
            return True
        else:
            return False

    def insert_node(self, index, value):
        if index < 0 or index > self.get_length():
            print 'Can not insert node into the linked list.'
        elif index == 0:
            temp = self.head
            self.head = Node(value, temp)
        else:
            p, post = self.head, self.head
            for i in xrange(index):
                post = p
                p = p.next
            temp = p
            post.next = Node(value, temp)

    def delete_node(self, index):
        if index < 0 or index > self.get_length()-1:
            print "Wrong index number to delete any node."
        elif self.is_empty():
            print "No node can be deleted."
        elif index == 0:
            temp = self.head
            self.head = temp.next
        elif index == self.get_length():
            p = self.head
            for i in xrange(self.get_length()-2):
                p = p.next
            p.next = 0
        else:
            p = self.head
            for i in xrange(index-1):
                p = p.next
            p.next = p.next.next

    def show_linked_list(self):  # 打印链表中的所有元素
        if self.is_empty():
            print 'This is an empty linked list.'
        else:
            p, container = self.head, []
            for _ in xrange(self.get_length()-1):  #
                container.append(p.value)
                p = p.next
            container.append(p.value)
            print container

    def clear_linked_list(self):  # 将链表置空
        p = self.head
        for _ in xrange(0, self.get_length()-1):
            post = p
            p = p.next
            del post
        self.head = 0

    def get_elem(self, index):
        if self.is_empty():
            print "The linked list is empty. Can not get element."
        elif index < 0 or index > self.get_length()-1:
            print "Wrong index number to get any element."
        else:
            p = self.head
            for _ in xrange(index):
                p = p.next
            return p.value

    def set_elem(self, index, value):
        if self.is_empty():
            print "The linked list is empty. Can not set element."
        elif index < 0 or index > self.get_length()-1:
            print "Wrong index number to set element."
        else:
            p = self.head
            for _ in xrange(index):
                p = p.next
            p.value = value

    def get_index(self, value):
        p = self.head
        for i in xrange(self.get_length()):
            if p.value == value:
                return i
            else:
                p = p.next
        return -1

    def reverse_linked_list(self):  # 将链表逆序反转，返回的是头指针。
        if self.head == 0:  # 空链表
            return self.head
        length = self.get_length()
        if length == 1:
            return self.head
        p = self.head
        head = self.head
        pre = 0
        while head != 0:
            p = p.next
            head.next = pre
            pre = head
            head = p
        self.head = pre
        return pre

    def reverse_part_linked_list(self, a, b):
        p = self.head
        if a == 0:
            tail, head = p, p
            pre = 0
            for _ in xrange(a, b+1):
                p = p.next
                head.next = pre
                pre = head
                head = p
            self.head = pre
            tail.next = p
        else:
            for _ in xrange(1, a):
                p = p.next
            front = p
            p = p.next
            tail = p
            pre = 0
            head = p
            for _ in xrange(a+1, b+2):
                p = p.next
                head.next = pre
                pre = head
                head = p
            front.next = pre
            tail.next = p


l = LinkedList()
print "The length of linked list now is: ", l.get_length()
print l.is_empty()
l.init_list([1, 5, 12, "fjd", 45, 999])
print "The length of linked list now is: ", l.get_length()
print l.is_empty()
l.insert_node(4, 100)
l.insert_node(6, "cecil")
#l.show_linked_list()
print "The value of index 0 is: ", l.get_elem(0)
l.set_elem(0,1000)
#l.show_linked_list()
print "the index of *** is: ", l.get_index(1009)
print "The length of linked list now is: ", l.get_length()
l.delete_node(3)
#l.clear_linked_list()
#l.reverse_linked_list()
#l.show_linked_list()
l.reverse_part_linked_list(4, 6)
#l.show_linked_list()
print "****************************************"


class RingLinkedList(object):
    # 链表的数据结构
    def __init__(self):
        self.head = 0  # 头部

    def __getitem__(self, key):
        if self.is_empty():
            print 'Linked list is empty.'
            return
        elif key < 0 or key > self.get_length():
            print 'The given key is wrong.'
            return
        else:
            return self.get_elem(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print 'Linked list is empty.'
            return
        elif key < 0 or key > self.get_length():
            print 'The given key is wrong.'
            return
        else:
            return self.set_elem(key, value)

    def init_list(self, data):  # 按列表给出 data
        self.head = Node(data[0])
        p = self.head  # 指针指向头结点
        for i in data[1:]:
            p.next = Node(i)  # 确定指针指向下一个结点
            p = p.next  # 指针滑动向下一个位置
        p.next = self.head

    def get_length(self):
        p, length = self.head, 0
        while p != 0:
            length += 1
            p = p.next
            if p == self.head:
                break
        return length

    def is_empty(self):
        if self.head == 0:
            return True
        else:
            return False

    def insert_node(self, index, value):
        length = self.get_length()
        if index < 0 or index > length:
            print 'Can not insert node into the linked list.'
        elif index == 0:
            temp = self.head
            self.head = Node(value, temp)
            p = self.head
            for _ in xrange(0, length):
                p = p.next
            #print "p.value", p.value
            p.next = self.head
        elif index == length:
            elem = self.get_elem(length-1)
            elem.next = Node(value)
            elem.next.next = self.head
        else:
            p, post = self.head, self.head
            for i in xrange(index):
                post = p
                p = p.next
            temp = p
            post.next = Node(value, temp)

    def delete_node(self, index):
        if index < 0 or index > self.get_length()-1:
            print "Wrong index number to delete any node."
        elif self.is_empty():
            print "No node can be deleted."
        elif index == 0:
            tail = self.get_elem(self.get_length()-1)
            temp = self.head
            self.head = temp.next
            tail.next = self.head
        elif index == self.get_length()-1:
            p = self.head
            for i in xrange(self.get_length()-2):
                p = p.next
            p.next = self.head
        else:
            p = self.head
            for i in xrange(index-1):
                p = p.next
            p.next = p.next.next

    def show_linked_list(self):  # 打印链表中的所有元素
        if self.is_empty():
            print 'This is an empty linked list.'
        else:
            p, container = self.head, []
            for _ in xrange(self.get_length()-1):  #
                container.append(p.value)
                p = p.next
            container.append(p.value)
            print container

    def clear_linked_list(self):  # 将链表置空
        p = self.head
        for _ in xrange(0, self.get_length()-1):
            post = p
            p = p.next
            del post
        self.head = 0

    def get_elem(self, index):
        if self.is_empty():
            print "The linked list is empty. Can not get element."
        elif index < 0 or index > self.get_length()-1:
            print "Wrong index number to get any element."
        else:
            p = self.head
            for _ in xrange(index):
                p = p.next
            return p

    def set_elem(self, index, value):
        if self.is_empty():
            print "The linked list is empty. Can not set element."
        elif index < 0 or index > self.get_length()-1:
            print "Wrong index number to set element."
        else:
            p = self.head
            for _ in xrange(index):
                p = p.next
            p.value = value

    def get_index(self, value):
        p = self.head
        for i in xrange(self.get_length()):
            if p.value == value:
                return i
            else:
                p = p.next
        return -1

ring = RingLinkedList()
ring.init_list([2,5,9,12,37,49,88,91,100])
ring.show_linked_list()
ring.insert_node(0, 100)
ring.show_linked_list()
ring.delete_node(3)
ring.show_linked_list()
ring.clear_linked_list()
ring.show_linked_list()
print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"


class LinkedListAlgorithms(object):
    # 所有的链表算法题
    def __init__(self):
        pass

    def print_common_part(self, head1, head2):  # 给定两个链表的头指针，打印出公共的部分
        if head1.next == 0 or head2.next == 0:
            print 'No common part between two linked lists.'
        common = []
        while head1 is not None and head2 is not None:
            if head1.value > head2.value:
                head2 = head2.next
            elif head1.value < head2.value:
                head1 = head1.next
            else:
                common.append(head1.value)
                head1, head2 = head1.next, head2.next
                if head1 == 0 or head2 == 0:
                    break
        print 'Common part: ', common

    def rm_last_kth_node(self, k, linked_list):  # 删除倒数第 K 个节点，针对单链表的
        if linked_list.is_empty():
            print 'The given linked_list is empty.'
        if k < 1 or k > linked_list.get_length():
            print 'Wrong kth number out of index.'
        k = linked_list.get_length() - k
        if k == 0:
            p = linked_list.head
            linked_list.head = p.next
        else:
            p = linked_list.head
            for i in xrange(k-1):
                p = p.next
            p.next = p.next.next

    def rm_mid_node(self, head):  # 给定一个链表，删除它的中间的一个结点，返回头指针
        if head == 0:
            return head
        p = head
        length = 1
        while p != 0:
            length += 1
            p = p.next
        if length == 1:
            return head
        mid = length / 2
        for _ in xrange(1, mid-1):
            head = head.next
        head.next = head.next.next
        return head

    def rm_by_ratio(self, head, a, b):  # 给定一个链表，删除它按比例的 a/b处的一个结点，返回头指针
        if a > b:
            print "The given a should be lower than b."
            return head
        if head == 0:
            return head
        p = head
        length = 1
        while p != 0:
            length += 1
            p = p.next
        if length == 1:
            return head
        ratio = length*float(a)/float(b)
        for _ in xrange(1, int(math.ceil(ratio))-1):
            head = head.next
        head.next = head.next.next
        return head

    def reverse_linked_list(self, head):  # 将链表逆序反转,返回头指针
        if head == 0:  # 空链表
            return head
        p = head
        length = 1
        while p != 0:
            length += 1
            p = p.next
        if length == 1:
            return head
        p = head
        pre = 0
        while head != 0:
            p = p.next
            head.next = pre
            pre = head
            head = p
        return pre

    def reverse_part_linked_list(self, head, a, b):  # 反转部分链表结点，a, b分别为索引值
        if head == 0:
            print "Empty linked list. No need to reverse."
            return head
        p = head
        length = 1
        while p != 0:
            length += 1
            p = p.next
        if length == 1:
            print "No need to reverse."
            return head
        if a < 0 or b > length-1 or a >= b:
            raise Exception("The given 'from' value and 'to' value is wrong.")
        p = head

        if a == 0:  # 由于 for 循环中 xrange 的范围问题，我就分情况写了。
            tail, head = p, p
            pre = 0
            for _ in xrange(a, b+1):
                p = p.next
                head.next = pre
                pre = head
                head = p
            tail.next = p
            return head
        else:
            for _ in xrange(1, a):
                p = p.next
            front, tail, head = p, p, p
            p = p.next
            pre = 0
            for _ in xrange(a+1, b+2):
                p = p.next
                head.next = pre
                pre = head
                head = p
            front.next = pre
            tail.next = p
            return head

    def is_palindrome1(self, head):
        '''
        判断一个链表是否是回文结构，如果是返回 True，否则返回 False
        方法1：时间复杂度o(n),空间复杂度o(n)
        '''
        if head == 0 or head.next == 0:
            return True
        p = head
        stack = Stack()  # 自定义的 Stack 数据结构，也可以使用python内置的 list来实现
        while p != 0:
            stack.push(p.value)
            p = p.next
        p = head
        while p != 0:
            if p.value != stack.pop():
                return False
            p = p.next
        return True

    def is_palindrome2(self, head):
        '''
        判断一个链表是否是回文结构，如果是返回 True，否则返回 False
        方法2：时间复杂度o(n),空间复杂度o(1)，方法是将链表的右半边逆序反转一下，然后逐个比较，如果有不同，则返回错误
        '''
        p, length = head, 0
        while p != 0:
            length += 1
            p = p.next

        mid = (length+1) / 2 - 1
        p = head
        for _ in xrange(mid):
            p = p.next

        mid_node = p  # 获取中间节点
        tail = mid_node.next
        mid_node.next = 0

        pre = mid_node
        while tail != 0:
            p = tail.next
            tail.next = pre
            pre = tail
            tail = p

        p = head
        tail = pre
        #print "p.value", p.value, p.next.value, p.next.next.value, p.next.next.next
        #print "tail.value:", pre.value, pre.next.value, pre.next.next.value, pre.next.next.next.value
        while p != 0:
            #print "p.value:", p.value, "tail.value:", tail.value
            if p.value != pre.value:  # 分别从两头遍历链表，如果遍历到0，则说明已经遍历到头了。
                pre = 0
                while tail != 0:
                    next = tail.next
                    tail.next = pre
                    pre = tail
                    tail = next
                mid_node.next = pre.next
                return False
            else:
                p = p.next
                pre = pre.next
        pre = 0
        while tail != 0:
            next = tail.next
            tail.next = pre
            pre = tail
            tail = next
        mid_node.next = pre.next
        return True

    def josephus_kill_1(self, head, m):
        '''
        环形单链表，使用 RingLinkedList 数据结构，约瑟夫问题。
        :param head:给定一个环形单链表的头结点，和第m个节点被杀死
        :return:返回最终剩下的那个结点
        本方法比较笨拙，就是按照规定的路子进行寻找，时间复杂度为o(m*len(ringlinkedlist))
        '''
        if head == 0:
            print "This is an empty ring linked list."
            return head
        if m < 2:
            print "Wrong m number to play this game."
            return head
        p = head
        while p.next != p:
            for _ in xrange(0, m-1):
                post = p
                p = p.next
            #print post.next.value
            post.next = post.next.next
            p = post.next
        return p

    def list_partition(self, head, pivot):
        '''
        将单向链表按某个值划分成左边小，中间相等，右边大的形式
        :param head:单向普通链表的头结点
        :param pivot:中间相等的那个数值
        :return:返回新的单向链表，左边和右边的结点顺序和原链表中的顺序一致。
        方法1：最常见的算法就是重新开辟三个链表，分别存储small ，middle，和large的值，时间复杂度为链表长度，空间复杂度也是
        方法2：把空间复杂度降到o(1)，就是需要不停地调整链表中的位置
        '''
        if head == 0:
            print "This is an empty linked list."
            return
        sh, st, eh, et, lh, lt = 0, 0, 0, 0, 0, 0
        p = head
        while p != 0:
            if p.value < pivot:
                if sh == 0:
                    sh = p
                    st = p
                else:
                    st.next = p
                    st = st.next
            elif p.value == pivot:
                if eh == 0:
                    eh = p
                    et = p
                else:
                    et.next = p
                    et = et.next
            else:
                if lh == 0:
                    lh = p
                    lt = p
                else:
                    lt.next = p
                    lt = lt.next
            p = p.next

        if sh != 0 and eh != 0 and lh != 0:
            head = sh
            st.next = eh
            et.next = lh
            lt.next = 0
        elif sh == 0 and eh != 0 and lh != 0:
            head = eh
            et.next = lh
            lh.next = 0
        elif sh == 0 and eh == 0 and lh != 0:
            head = lh
            lh.next = 0
        elif sh == 0 and eh != 0 and lh == 0:
            head = eh
            et.next = 0
        elif sh != 0 and eh == 0 and lh == 0:
            head = sh
            st.next = 0
        elif sh != 0 and eh != 0 and lh == 0:
            head = sh
            st.next = eh
            et.next = 0
        elif sh != 0 and eh == 0 and lh != 0:
            head = sh
            st.next = lh
            lt.next = 0
        return head

    def copy_list_with_random_pointer(self, head):
        '''
        一种特殊类型的链表结构，每一个节点都有一个随机指针域，指针指向该链表中随机一个结点，也有可能指向0.
        复制含有随机指针结点的链表，比如一个单链表中有1->2->3->None，其中1还指向了3,2指向了None。
        将整个数据结构都复制一遍，并返回头结点head，时间复杂度为一遍遍历该种链表，空间复杂度为o(1)。
        '''









l1 = LinkedList()
l1.init_list([1, 5, 12, 33, 45, 171, 999, 1001, 2000])
l2 = LinkedList()
l2.init_list([2, 5, 12,198, 12, 5, 2])
l3 = LinkedList()
l3.init_list([21, 5, 120, 19, 72, 50, 312])

ll_algo = LinkedListAlgorithms()
# ll_algo.print_common_part(l1.head, l2.head)
# ll_algo.rm_last_kth_node(6, l1)
# ll_algo.rm_mid_node(l2.head)
# ll_algo.rm_by_ratio(l1.head, 41, 170)
print "999"
#l1.show_linked_list()
# ll_algo.reverse_linked_list(l1.head)
print "is palindrome1: ", ll_algo.is_palindrome1(l2.head)
print "is palindrome2: ", ll_algo.is_palindrome2(l2.head)
print "888"
l2.show_linked_list()
print "##################################################"

ring = RingLinkedList()
ring.init_list([2,5,9,12,37,49,88,91,100])
print ll_algo.josephus_kill_1(ring.head, 4).value
ll_algo.list_partition(l3.head, 100)
l3.show_linked_list()

