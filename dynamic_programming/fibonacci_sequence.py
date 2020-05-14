# -*- coding=utf8 -*-
# @Time   : 18-1-3 下午2:53
# @Author : Cecil Charlie
# ------------------------------------------------------------------------
'''
计算斐波那契数列
------------------------------------------------------------------------
斐波那契数列：
0  1  2  3  4  5  6  7  8
0  1  1  2  3  5  8  13 21

包括三种方法：
一、数列公式计算，即递归计算法，计算复杂度 o(2**n),
二、考虑到重复计算，采用循环的方式，每次保存了前一步的计算结果，速度大大加快，计算复杂度 o(n)
三、考虑采用矩阵运算，进一步利用较大的空间，使得速度上有加快，计算复杂度 o(log n)。
'''

import os
import sys
import copy

import numpy as np


__all__ = ['FibonacciRecursion', 'FibonacciIteration', 
           'FibonacciMatrix']


class FibonacciRecursion(object):
    '''
    数列公式计算，即递归计算法，计算复杂度 o(2**n),
    '''
    def __init__(self):
        # 用于指定最大迭代次数
        self.n = -1

    def __call__(self, n):
        '''
        :param n: 数列的第n个索引
        :return: 索引n对应的值
        '''
        # 配置相应的最大迭代次数
        if n < 0:
            return None
        
        if self.n < n and n > 1000:
            sys.setrecursionlimit(n)
            self.n = n
        
        if n < 1:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        return self.__call__(n-1) + self.__call__(n-2)


class FibonacciIteration(object):
    '''
    采用循环迭代的方式计算，每次保存了前一步的计算结果，速度大大加快，计算复杂度 o(n)
    '''
    def __init__(self):
        pass
    
    def __call__(self, n):
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
        for _ in range(1, n):
            res = tmp1 + tmp2
            tmp1 = tmp2
            tmp2 = res
        return res


class FibonacciMatrix(object):
    '''
    考虑采用矩阵运算，进一步利用较大的空间，使得速度上有加快，计算复杂度 o(log n)。
    当然了，这种方法需要额外计算矩阵，计算矩阵的时间开销没有算在内.其中还运用到了位运算。
    '''
    def __init__(self):
        pass
    
    def __call__(self, n):
        base = [[1, 1], [1, 0]]
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        res = self.__matrix_power(base, n-2)
        return res[0][0] + res[1][0]

    def __matrix_power(self, mat, n):
        """
            求一个方阵的幂，时间复杂度为 o(log n)
        """
        if len(mat) != len(mat[0]):
            raise ValueError("The mat is not a square array.")
            
        if n < 0 or type(n) is not int:
            raise ValueError("The power is unsuitable.")
            
        product = np.identity(len(mat))
        tmp = mat
        while n > 0:
            if (n & 1) != 0:
                # 按位与的操作，在幂数的二进制位为1时，
                # 乘到最终结果上，否则自乘
                product = self._multiply_matrix(product, tmp)
            tmp = self._multiply_matrix(tmp, tmp)
            n >>= 1
            
        return product

    @staticmethod
    def _multiply_matrix(mat1, mat2):
        """
            矩阵乘法
        :param m: 矩阵1，二维列表
        :param n: 矩阵2
        :return: numpy 格式的矩阵
        """
        if len(mat1[0]) != len(mat2):
            raise ValueError('The dimention of matrix1 and matrix2 is not same')
        
        product = np.zeros((len(mat1), len(mat2[0])))
        for i in range(0, len(mat1)):
            for j in range(0, len(mat2[0])):
                for k in range(0, len(mat1[0])):
                    if mat1[i][k] != 0 and mat2[k][j] != 0:
                        product[i][j] += mat1[i][k] * mat2[k][j]
        return product


if __name__ == '__main__':
    fib_rec = FibonacciRecursion()
    fib_iter = FibonacciIteration()
    fib_mat = FibonacciMatrix()
    n = 180
    max_iter = 1000
    import time
    start_time = time.time()
    for i in range(max_iter):
        fib_rec(n)
    print(time.time() - start_time)
    
    start_time = time.time()
    for i in range(max_iter):
        fib_iter(n)
    print(time.time() - start_time)
    
    start_time = time.time()
    for i in range(max_iter):
        fib_mat(n)
    print(time.time() - start_time)
    

