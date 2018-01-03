#!usr/bin/python2.7
# -*- coding=utf-8 -*-

import math

class MathAlgorithms(object):
    def __init__(self):
        pass

    def greatest_common_divisor_1(self, num1, num2):
        '''
        数值计算寻找最大公约数，给定两个整数，计算其最大公约数，时间复杂度为 o(min(num1,num2))，取余运算复杂度高
        '''
        gbc = 1
        for i in xrange(2, min(num1, num2)+1):
            if num2 % i == 0 and num1 % i == 0:
                gbc = i
        return gbc

    def greatest_common_divisor_2(self, num1, num2):
        '''
        辗转相减法，时间复杂度最差为 o(min(num1,num2))，一般情况下都比这个要好。相减运算要比除法方便很多
        '''
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return num1

    def greatest_common_divisor_3(self, num1, num2):
        '''
        求余数法，取模运算比较麻烦，时间复杂度低 o(log max(num1, num2))
        '''
        while num1 != num2:
            if num1 > num2:
                if num1 % num2 == 0:
                    return num2
                num1 = num1 % num2
            else:
                if num2 % num1 == 0:
                    return num1
                num2 = num2 % num1
        return num1

    def greatest_common_divisor(self, num1, num2):
        '''
        求两个数的最大公约数
        综合取余法和辗转相减法，既能得到较好的时间复杂度，又能避免取余运算，时间复杂度稳定 o(log max(num1,num2))
        如果取两个非常大的数的话，前面的方法很容易爆栈、取余困难等等，但是该方法没有问题
        a = 999999342353200
        b = 777774234
        print greatest_common_divisor(a, b)
        '''
        factor = 1
        if num1 < num2:
            return greatest_common_divisor_1(num2, num1)
        while num1 != num2:
            if num1 & 1 is False and num2 & 1 is False:  # 均为偶数
                num1 = num1 >> 1
                num2 = num2 >> 2
                factor *= 2
            elif num1 & 1 is False and num2 & 1 is True:
                num1 = num1 >> 1
            elif num1 & 1 is True and num2 & 1 is False:
                num2 = num2 >> 1
            else:
                if num1 > num2:
                    num1 = num1 - num2
                else:
                    num2 = num2 - num1
        return factor*num1


a = 454242353200
b = 1400
mathalgorithms = MathAlgorithms()
print mathalgorithms.greatest_common_divisor(a, b)





