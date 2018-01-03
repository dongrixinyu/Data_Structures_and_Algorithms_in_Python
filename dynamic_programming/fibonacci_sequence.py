#!usr/bin/python2.7
# -*- coding=utf8 -*-
# @Time   : 18-1-3 下午2:53
# @Author : Cecil Charlie

import sys
import copy
sys.setrecursionlimit(1000)


class Fibonacci(object):
    def __init__(self):
        pass

    def fibonacci1(self, n):
        '''
            原始的方法，时间复杂度为 o(2**n)，因此代价较大
        :param n: 数列的第n个索引
        :return: 索引n对应的值
        '''
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fibonacci1(n-1) + self.fibonacci1(n-2)

    @staticmethod
    def fibonacci2(n):
        """
            用循环替代递归，空间复杂度急剧降低，时间复杂度为o(n)
        """
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        res = 1
        tmp1 = 0
        tmp2 = 1
        for _ in xrange(1, n):
            res = tmp1 + tmp2
            tmp1 = tmp2
            tmp2 = res
        return res

    def fibonacci3(self, n):
        """
            进一步减少迭代次数，采用矩阵求幂的方法，时间复杂度为o(log n)，当然了，这种方法需要额外计算矩阵，计算矩阵的时间开销没有算在内.其中还运用到了位运算。
        """
        base = [[1, 1], [1, 0]]
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        res = self.__matrix_power(base, n-2)
        return res[0][0] + res[1][0]

    def __matrix_power(self, mat, n):
        """
            求一个方阵的幂
        """
        if len(mat) != len(mat[0]):
            raise ValueError("The length of m and n is different.")
        if n < 0 or str(type(n)) != "<type 'int'>":
            raise ValueError("The power is unsuitable.")
        product, tmp = [], []
        for _ in xrange(len(mat)):
            tmp.append(0)
        for _ in xrange(len(mat)):
            product.append(copy.deepcopy(tmp))
        for _ in xrange(len(mat)):
            product[_][_] = 1
        tmp = mat
        while n > 0:
            if (n & 1) != 0:  # 按位与的操作，在幂数的二进制位为1时，乘到最终结果上，否则自乘
                product = self.__multiply_matrix(product, tmp)
            tmp = self.__multiply_matrix(tmp, tmp)
            n >>= 1
        return product

    @staticmethod
    def __multiply_matrix(mat1, mat2):
        """
            矩阵计算乘积
        :param m: 矩阵1，二维列表
        :param n: 矩阵2
        :return: 乘积
        """
        if len(mat1[0]) != len(mat2):
            raise ValueError("Can not compute the product of mat1 and mat2.")
        product, tmp = [], []
        for _ in xrange(len(mat2[0])):
            tmp.append(0)
        for _ in xrange(len(mat1)):
            product.append(copy.deepcopy(tmp))
        for i in xrange(0, len(mat1)):
            for j in xrange(0, len(mat2[0])):
                for k in xrange(0, len(mat1[0])):
                    if mat1[i][k] != 0 and mat2[k][j] != 0:
                        product[i][j] += mat1[i][k] * mat2[k][j]
        return product


f = Fibonacci()
for i in xrange(14):
    print f.fibonacci1(i)
print f.fibonacci2(23)
mat1 = [[2,4,5],[1,0,2],[4,6,9]]
mat2 = [[2,9],[1,0],[5,7]]
print f.fibonacci3(23)

