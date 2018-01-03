# -*- coding=utf-8 -*-


class Node(object):
    # 栈结点
    def __init__(self, value, next=0):
        self.value = value
        self.next = next  # 指针


class Stack(object):
    # 由于 Python 难以对内存地址进行操作，所以这里给出了链栈的数据结构
    # 由于栈的操作比线性表少很多，所以顺序栈的表示法要比链栈方便快捷
    def __init__(self):
        self.head = 0

    def init_stack(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

    def clear_stack(self):
        self.head = 0

    def is_empty(self):
        if self.head == 0:
            return True
        else:
            return False

    def get_length(self):
        p, length = self.head, 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def push(self, value):  # 向栈中添加一个结点
        if self.is_empty():
            self.head = Node(value)
        else:
            p = self.head
            for _ in xrange(self.get_length() - 1):
                p = p.next
            p.next = Node(value)

    def get_top(self):  # 获得栈顶元素
        if self.is_empty():
            print 'This is an empty stack.'
            return
        else:
            p = self.head
            for _ in xrange(self.get_length()):
                p = p.next
            return p.value

    def pop(self):  # 弹出栈顶元素
        length = self.get_length()
        if self.is_empty():
            print 'This is an empty stack.'
            return
        elif length == 1:
            p = self.head
            self.head = 0
            return p.value
        elif length == 2:
            p = self.head
            value = p.next.value
            self.head.next = 0
            return value
        else:
            p = self.head
            for _ in xrange(1, length - 1):
                p = p.next
            pop = p.next
            p.next = 0
            return pop.value

    def show_stack(self):  # 打印栈中的所有元素
        if self.is_empty():
            print 'This is an empty stack.'
        else:
            p, container = self.head, []
            for _ in xrange(self.get_length() - 1):
                container.append(p.value)
                p = p.next
            container.append(p.value)
            print container

    def get_min(self):
        '''
            返回链栈中的最小的元素的值，要求时间复杂度为 o(1)，主要方法是用空间换时间，构建一个存放最小栈元素的栈 stackmin。
            每次向栈中添加元素的时候，都判断这个元素是不是比栈中的元素小，如果是相等或更小，则将该数放在 stackmin 中。
            每次弹出一个栈顶元素，判断该数是不是比 stackmin的栈顶元素大，如果大，则 stackmin不需要任何操作。
            在查询时，直接返回stackmin的栈顶元素即可。
        '''
        self.stackmin.pop()


s = Stack()
s.init_stack([1])
print s.get_length()
s.show_stack()
# print "top node: ", s.get_top()
s.push(999)
s.show_stack()
print "pop: ", s.pop()
s.show_stack()


class StackAlgorithms(object):
    def __init__(self):
        pass



class SpecialStack(object):
    def __init__(self):
        self.head = 0
        self.stackmin = []

    def init_stack(self, data):
        self.head = Node(data[0])
        if self.stackmin =[]:
            self.stackmin.append(data[0])
        p = self.head
        for i in data[1:]:
            p.next = Node(i)
            pop = self.stackmin.pop()
            if pop >= i:
                self.stackmin.append(pop)
                self.stackmin.append(i)
            else:
                self.stackmin.append(pop)
            p = p.next

    def clear_stack(self):
        self.head = 0
        self.stackmin = []

    def is_empty(self):
        if self.head == 0:
            return True
        else:
            return False

    def get_length(self):
        p, length = self.head, 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def push(self, value):  # 向栈中添加一个结点
        if self.is_empty():
            self.head = Node(value)
        else:
            p = self.head
            for _ in xrange(self.get_length() - 1):
                p = p.next
            p.next = Node(value)
            pop = self.stackmin.pop()
            if pop >= value:
                self.stackmin.append(pop)
                self.stackmin.append(value)
            else:
                self.stackmin.append(pop)

    def get_top(self):  # 获得栈顶元素
        if self.is_empty():
            print 'This is an empty stack.'
            return
        else:
            p = self.head
            for _ in xrange(self.get_length()):
                p = p.next
            return p.value

    def pop(self):  # 弹出栈顶元素
        length = self.get_length()
        if self.is_empty():
            print 'This is an empty stack.'
            return
        elif length == 1:
            p = self.head
            self.head = 0
            self.stackmin = []
            return p.value
        elif length == 2:
            p = self.head
            value = p.next.value
            self.head.next = 0
            if len(self.stackmin) == 2:
                self.stackmin.pop()
            return value
        else:
            p = self.head
            for _ in xrange(1, length - 1):
                p = p.next
            pop = p.next
            p.next = 0
            stack_min = self.stackmin.pop()
            if stack_min < pop.value:
                self.stackmin.append(stack_min)
            return pop.value

    def show_stack(self):  # 打印栈中的所有元素
        if self.is_empty():
            print 'This is an empty stack.'
        else:
            p, container = self.head, []
            for _ in xrange(self.get_length() - 1):
                container.append(p.value)
                p = p.next
            container.append(p.value)
            print container

    def get_min(self):
        '''
            返回链栈中的最小的元素的值，要求时间复杂度为 o(1)，主要方法是用空间换时间，构建一个存放最小栈元素的栈 stackmin。
            每次向栈中添加元素的时候，都判断这个元素是不是比栈中的元素小，如果是相等或更小，则将该数放在 stackmin 中。
            每次弹出一个栈顶元素，判断该数是不是比 stackmin的栈顶元素大，如果大，则 stackmin不需要任何操作。
            在查询时，直接返回stackmin的栈顶元素即可。
        '''
        pop = self.stackmin.pop()
        self.stackmin.append(pop)
        return pop
