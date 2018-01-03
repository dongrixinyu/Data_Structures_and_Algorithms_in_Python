#!usr/bin/python2.7
# -*- coding=utf8 -*-
# @Time   : 18-1-3 下午8:35
# @Author : Cecil Charlie


class BitAlgorithms(object):
    '''
        位运算算法合集
    '''

    def __init__(self):
        pass

    def exchage_nums(self, a, b):
        '''
            不用额外变量交换两个整数值，空间节省了，时间负责度略高一些。
        '''
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b

    def add_bit(self, a, b):
        '''
            位运算实现两个整数相加,python里只能针对正数来处理
        '''
        sum = a
        while b != 0:
            sum = a ^ b
            b = (a & b) << 1
            a = sum
        return sum

    def count1(self, a):
        '''
            整数的二进制表达里有多少个1，复杂度为a的二进制长度。
        '''
        num = 0
        while a != 0:
            num += a & 1
            a >>= 1
        return num

    def count2(self, a):
        '''
            整数的二进制表达里有多少个1，复杂度仅为1的个数
        '''
        num = 0
        while a != 0:
            a = a & (a - 1)
            num += 1
        return num

    def print_odd_times_num1(self, arr):
        '''
            给定一个数组，数据都是整数，其中只有一个数字出现了奇数次，其它都是偶数次。找出那个奇数次的数字。
            时间复杂度o(n)，空间复杂度为o(1)。
            整数 n 与 0 的异或结果为 n。整数 n 与 n的异或结果为0，异或运算满足交换律和结合律
        '''
        odd = 0
        for i in arr:
            odd ^= i
        return odd

    def print_odd_times_num2(self, arr):
        '''
            给定一个数组，数据都是整数，其中只有2个数字出现了奇数次，其它都是偶数次。找出那2个奇数次的数字。
            时间复杂度o(n)，空间复杂度为o(1)。
            如果有两个数字出现了奇数次，比如是 a 和 b，则最终 odd 结果为 a^b，但其中一定有差别。
        '''
        odd, odd_one = 0, 0
        for i in arr:
            odd ^= i
        right = odd & (~odd + 1)  # odd的第k位是1，即两个奇数个的数字的第k位一定不同
        for i in arr:
            if i & right != 0:
                odd_one ^= i
        return odd_one, odd_one ^ odd

    def get_num_from_k_arr(self, arr, k):
        '''
            在其它数都出现 k 次的数组中找到只出现一次的数。k 大于 1。
            数组 arr 中，只有一个数出现了 1 次，其它都出现了 k 次，找出那个出现1次的数。
            时间复杂度 o(n)，额外空间复杂度为 o(1)
            解法是：如果两个 k 进制数 a，b无进位相加，其结果一定是 (a(i)+b(i))%k，如果是 k 个 k进制数相加，其结果一定是 k 个 0
        '''
        e0 = 0
        for i in arr:
            e0 = (e0 + i) % k  # 错误的，有两个问题需要克服，k进制数如何处理，无进位相加如何处理。
        return e0


bit = BitAlgorithms()
print bit.add_bit(543, 240)
print bit.count1(329)
print bit.count2(329)
print bit.print_odd_times_num1([3, 4, 1, 9, 55, 55, 4, 1, 9])
print bit.print_odd_times_num2([3, 4, 1, 9, 55, 55, 3, 82, 1, 9])
print bit.get_num_from_k_arr([3, 4, 4, 1, 1, 9, 55, 9, 55, 55, 4, 1, 9],3)