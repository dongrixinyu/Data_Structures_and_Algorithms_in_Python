# -*- coding=utf-8 -*-

import time
import random
import unittest


def timeCount(func):  # 装饰器计算时间
    def wrapper(*arg,**kwarg):
        start = time.clock()
        func(*arg,**kwarg)
        end =time.clock()
        print 'used:', end - start
    return wrapper


class Executor:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.do()

    @timeCount
    def do(self):
        print '-----start:',self.func,'-----'
        self.ret = self.func(*self.args, **self.kwargs)

    def __del__(self):
        print '-----end-----'


class TestSort(unittest.TestCase):  # 测试类的使用

    def test_01_bubbleSort(self):
        Executor(SortingAlgorithms().bubble_sort, L[:])

    def test_11_builtinSort(self):
        Executor(sorted, L[:])


class SortingAlgorithms(object):
    '''
    冒泡法：对比模型，原数组上排序，稳定，慢
    插入法：对比模型，原数组上排序，稳定，慢
    选择法：对比模型，原数组上排序，稳定，慢
    归并法：对比模型，非原数组上排序，稳定，快
    快速法：对比模型，原数组上排序，不稳定，快
    堆排序：对比模型，原数组上排序，不稳定，快，空间复杂度为1个辅助空间
    二叉树排序：对比模型，非数组上排序，不稳定，快
    桶排序：非对比模型，非原数组上排序，不稳定，快
    基数排序：非对比模型，非原数组上排序，稳定，快
    基于比较模型的排序算法的复杂度最高可以做到 o(n*log2 n)，这是二叉树形比较结构决定的，再有其他方法就只能是空间换时间。
    一种广泛采取的排序算法，是在数据量很大的时候，采取快速排序的方式，而在当分组很小的时候，使用其他稳定的排序方法。
    这样的混合型算法，综合效果是最好的，也就是一般内置排序使用的方法
    '''
    def __init__(self):
        pass

    def straight_insertion_sort(self, lists):
        # 直接插入排序, 空间复杂度 o(1)，时间复杂度为o(n^2)，稳定排序
        if lists == [] or len(lists) == 1:
            return
        for i in range(1, len(lists)):
            key = lists[i]
            j = i-1
            while j >= 0:
                if lists[j] > key:
                    lists[j+1] = lists[j]
                    lists[j] = key
                j -= 1
        return lists

    def bubble_sort(self, lists):
        # 冒泡排序，快速排序的一种，稳定排序
        if lists == [] or len(lists) == 1:
            return lists
        for i in range(0, len(lists)):
            for j in range(i+1, len(lists)):
                if lists[i] > lists[j]:
                    lists[j], lists[i] = lists[i], lists[j]
        return lists

    def quick_sort_1(self, lists):
        # 快速排序，对冒泡排序的改进，不稳定排序,时间复杂度为o(n*log 2n)，目前公认的常数项因子最小的先进排序算法.
        # 其中的关键是分治策略，但是在 Python 中的分治要比 C 语言中的简单得多,但是我仍然用 Python 具体写了一下分治策略
        if lists == [] or len(lists) == 1:
            return lists
        low, high = 0, len(lists) - 1
        pivot = 0
        while low < high:
            while low < high:
                if lists[pivot] > lists[high]:
                    lists[high], lists[low] = lists[low], lists[high]
                    pivot = high
                    break
                high -= 1
            while low < high:
                if lists[pivot] < lists[low]:
                    lists[high], lists[low] = lists[low], lists[high]
                    pivot = low
                    break
                low += 1
        return self.quick_sort_1(lists[:pivot]) + [lists[pivot]] + self.quick_sort_1(lists[pivot+1:])

    def quick_sort_2(self, lists):
        # 快速排序的另外一种写法，简单写法，但是时间消耗要比分治多一些
        if lists == [] or len(lists) == 1:
            return lists
        left = [i for i in lists[1:] if i < lists[0]]
        right = [i for i in lists[1:] if i >= lists[0]]
        return self.quick_sort_2(left) + [lists[0]] + self.quick_sort_2(right)

    def shell_sort(self, lists):
        '''
        希尔排序，插入排序的一种，时间复杂度为o(n^3/2)，不稳定排序，基本思想是如果是正序的话，比较次数就少了很多
        i,j k 三个变量折腾的我有点懵逼，
        :param lists:
        :return:
        '''
        if lists == [] or len(lists) == 1:
            return lists
        count = len(lists)
        step = 2
        group = count / step
        while group > 0:
            for i in range(0, group):
                j = i + group
                while j < count:
                    k = j - group
                    key = lists[j]
                    while k >= 0:  # 直接插入排序的方法
                        if lists[k] > key:
                            lists[k + group] = lists[k]
                            lists[k] = key
                        k -= group
                    j += group
            group /= step
        return lists

    def simple_select_sort(self, lists):
        '''
        简单选择排序，稳定排序，时间复杂度为 o(n^2)，查找每一次最小值的时候都要经过 n-1 次比较
        '''
        length = len(lists)
        for i in xrange(0, length):
            key = i
            for j in xrange(i+1, length):
                if lists[key] > lists[j]:
                    key = j
            lists[i], lists[key] = lists[key], lists[i]
        return lists

    def heap_sort(self, L):
        '''
        堆排序，是选择排序的一种优化，利用了树形结构，避免了选择最小元素时每次都经过 n-1 次比较，不稳定排序
        辅助空间只需要一个，空间复杂度为o(1)，时间复杂度为 o(n*log 2n)，在最坏的情况下，复杂度依然是 o(n*log 2n)
        这是相比快速排序优秀的地方，但是在序列中记录较少的时候不提倡使用，因为建立堆比较耗时。
        '''
        if L == [] or len(L) == 1:
            return L

        def sift_down(L, start, end):  # 调整找到一颗根节点最小的树
            root = start
            while True:
                child = 2*root + 1  # 左子节点，一个辅助空间，指针指示哪一个节点
                if child > end:  # 子节点超出范围
                    break
                if child+1 <= end and L[child] < L[child+1]:  # 左子节点比右子节点小，转换到右子节点
                    child += 1
                if L[root] < L[child]:  # 若根节点比 相对较大的一个子节点小，则互换
                    L[root], L[child] = L[child], L[root]
                    root = child  # 进行树下面下一层的替换
                else:
                    break
            return
        for start in range((len(L)-2)/2, -1, -1):  # 逆序构建一个堆，堆顶的值最大，
            sift_down(L, start, len(L)-1)
        #print L
        for end in range(len(L)-1, 0, -1):  # 取堆顶的一个值，放在序列尾部
            L[0], L[end] = L[end], L[0]
            sift_down(L, 0, end-1)
        return L

    def merging_sort(self, lists):
        '''
        归并排序，需要的辅助空间大小和待排记录数量相等，时间复杂度也是 o(n*log 2n)，稳定排序
        '''
        if lists == [] or len(lists) == 1:
            return lists

        def merge(list1, list2):
            i, j = 0, 0  # 分别指向两个序列的指针
            result = []
            while i < len(list1) and j < len(list2):
                if list1[i] > list2[j]:
                    result.append(list2[j])
                    j += 1
                else:
                    result.append(list1[i])
                    i += 1
            result += list1[i:]
            result += list2[j:]
            return result

        num = len(lists) / 2
        left = self.merging_sort(lists[:num])
        right = self.merging_sort(lists[num:])
        return merge(left, right)

    def bucket_sort(self, lists):
        '''
        桶排序，非比较模型，适用于数据量非常大，数据紧凑，相同数据很多的情况，比如统计每年高考学生的分数
        '''
        if lists == [] or len(lists) == 1:
            return lists
        mini = min(lists)  # 查找方法
        maxi = max(lists)
        bucket = []
        for _ in xrange(0, maxi+1-mini):
            bucket.append(0)
        for i in lists:
            bucket[i-mini] += 1
        res = []
        for i in xrange(0, len(bucket)):
            while bucket[i] > 0:
                res.append(i+mini)
                bucket[i] -= 1
        return res

    def radix_sort(self, lists):
        '''
        基数排序，针对“正整数”来写的算法函数，稳定排序，按照千位、百位、十位来排序
        '''
        import math
        k = int(math.ceil(math.log(max(lists), 10)))
        bucket = [[] for _ in range(10)]
        for i in range(1, k+1):
            for j in lists:
                #num =
                bucket[(j%(10**i))/10**(i-1)].append(j)
            del lists[:]
            for z in bucket:
                lists += z
                del z[:]
        return lists


class ExternalSortingAlgorithms(object):
    '''
    败者树外部排序的全部实现：
    1、使用gen_k_data 函数产生一个 data，这个data中，k表示归并的路数，l表示每一路中包含数字的个数
        e.g. data = gen_k_data(10, 200)
             print "generate the data for loser tree: ", data
    2、在 merging_soring 函数中，接收上一步产生的数据。并首先生成一个败者树，在这一步中，关键点就是创建败者树，以及调整败者树。
        然后，每次产生一个 compare，用来存放当前需要比较的10个数值，取出最小的一个，再从对应的那一路中取出下一个数值放在compare里
        对应的位置上。如果某一路都取完了，我们就给该路的compare值赋一个很大的值，比如说我在这里赋了10000，当compare里全部都是10000
        说明已经排序完毕，返回result 就是我们的排序结果。
        e. g. merging_sorting(data)
    '''
    def __init__(self):
        pass

    def gen_k_data(self, k, l):  # 生成k 路随机数，并排序，存放在列表中， k表示归并的路数，l表示每一路多少个数
        if k < 0 or l < 0:
            print "Wrong given k number or l number."
        data = []
        sort = SortingAlgorithms()
        for n in xrange(0, k):
            merge = []
            small = random.randint(0, 100)
            large = random.randint(800, 1000)
            for _ in xrange(0, l):
                merge.append(random.randint(small, large))  # small 和 large 用来控制取值范围的。
            data.append(sort.heap_sort(merge))
        return data

    def merging_sorting(self, data):  # 生成一个归并序列，把每一路中的元素挨个排入compare数组中
        k = len(data)
        compare = []
        for i in xrange(0, k):
            compare.append(data[i][0])
            #data[i].remove(data[i][0])
        print compare

        def adjust(loserTree, dataArray, n, s):  # 败者树的核心代码
            t = (s + n) / 2
            while t > 0:  # 从败者树的尾部开始进行比较
                if dataArray[s] > dataArray[loserTree[t]]:  # 和败者结点比较
                    s, loserTree[t] = loserTree[t], s  # 如果比某个败者结点大，说明该结点失败了，将s结点存入败者树，把败者树的现在的胜结点拿去和其父节点比较。
                t /= 2
            loserTree[0] = s

        def createLoserTree(loserTree, dataArray, n):
            for i in range(n):
                loserTree.append(0)
                dataArray.append(i-n)  # 这里是为了生成败者树用的，

            for i in range(n):
                adjust(loserTree, dataArray, n, n-1-i)

        loserTree = []
        dataArray = []
        createLoserTree(loserTree, dataArray, k)

        for i in xrange(k):
            dataArray[i] = compare[i]  # 将数据替换成待排数据
            adjust(loserTree, dataArray, k, i)  # 此步执行完毕，败者树才完全创建初始化完毕，正式开始排序归并

        result = []
        while True:
            if data[loserTree[0]][0] > 9999:
                break
            result.append(data[loserTree[0]][0])  # 添加到 result 中，这是我们需要的结果
            data[loserTree[0]].remove(data[loserTree[0]][0])  # 从data 中删除头一个元素
            if data[loserTree[0]] == []:
                data[loserTree[0]].append(10000)
            compare[loserTree[0]] = data[loserTree[0]][0]  # 将下一个元素添加到 compare数组中
            adjust(loserTree, compare, k, loserTree[0])

        return result

if __name__ == "__main__":
    sort = SortingAlgorithms()
    l = [4,90,125,2,9,47,999,-6,111,908,13,78,345,3,10]
    print "lists is :", l
    #print "Straight insertion sort: ", sort.straight_insertion_sort(l)
    # print "Bubble sort: ", sort.bubble_sort(l)
    # print "Quick sort 1: ", sort.quick_sort_1(l)
    # print "Quick sort 2: ", sort.quick_sort_2(l)
    #print "Shell sort: ", sort.shell_sort(l)
    #print "Simple select sort: ", sort.simple_select_sort(l)
    print "Heap sort: ", sort.heap_sort(l)
    print "Merging sort: ", sort.merging_sort(l)
    #print sort.bucket_sort(l)

    L = range(5000)
    random.shuffle(L)

    if __name__=="__main__":
        #unittest.main()
        print "radix_sort: ", sort.radix_sort(l)

