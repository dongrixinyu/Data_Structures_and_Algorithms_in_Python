# -*- coding=utf8 -*-
# @Time   : 18-1-3 下午2:53
# @Author : Cecil Charlie
# ------------------------------------------------------------------------
'''
计算两字符串的最长公共子串
------------------------------------------------------------------------
字符串1：人工智能在自然语言处理上的应用
字符串2：自然语言处理的应用非常广泛
最长公共子串：自然语言处理

包括三种方法：
一、直接计算法，计算复杂度 o(n**3)
二、采用动态规划的方法保存下已经计算的变量，计算复杂度 o(n**2)，空间复杂度 o(len(str1) * len(str2))
三、删除临时保存的矩阵，节省空间复杂度
'''

import numpy as np


class LongestCommonStringDynamicProgramming(object):
    def __init__(self):
        pass
    
    def __call__(self, string_1, string_2, flag=True):
        ''' 动态规化法记录比较矩阵，若子串 str1 和 str2 是相同的，
        则 str1[:-1] 和 str2[:-1] 一定是相同的。
        '''
        length_1 = len(string_1)
        length_2 = len(string_2)

        map_matrix = np.zeros((length_1 + 1, length_2 + 1), dtype='int')
        
        m_max = 0   #最长匹配的长度
        position = 0  #最长匹配对应在 s1 中的最后一位
        for i in range(length_1):
            for j in range(length_2):
                # 对其中不必要的比较做删减，加快计算速度
                # rule1: 子串在 string_2 上已经不可能再长过当前的最大子串
                if flag:
                    if length_2 - j + map_matrix[i][j] < m_max: 
                        break

                    # rule2: 子串在 string_1 上已经不可能再长过当前最大子串
                    if length_2 - i + map_matrix[i][j] < m_max:
                        continue
                
                if string_1[i] == string_2[j]:
                    map_matrix[i + 1][j + 1] = map_matrix[i][j] + 1
                    if map_matrix[i + 1][j + 1] > m_max:
                        m_max = map_matrix[i + 1][j + 1]
                        position = i + 1
        '''
        print('     ' + ' '.join(list(string_2)))
        for idx, i in enumerate(map_matrix):
            if idx == 0:
                print(' ', i)
            else:
                print(string_1[idx - 1], i)
        '''
        return string_1[position - m_max: position], int(m_max)   










if __name__ == '__main__':
    import time
    from time_stat import TimeStat
    
    lcs_dp = LongestCommonStringDynamicProgramming()
    string_1 = '123456778'
    string_2 = '129834567486782'
    max_iter = 10000
    
    with TimeStat() as ts:
        for i in range(max_iter):
            res = lcs_dp(string_1, string_2, flag=False)
    with TimeStat() as ts:
        for i in range(max_iter):
            res = lcs_dp(string_1, string_2, flag=True)




