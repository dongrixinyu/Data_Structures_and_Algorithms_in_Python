# -*- coding=utf-8 -*-
# @Time   : 20-05-15 下午5:15
# @Author : Cecil Charlie
# ------------------------------------------------------------------------
# 计算耗时的工具

import time
import typing


class TimeStat(object):
    def __init__(self, name: str = None):
        self.name = name
        self.total_time = 0
        self.start_time = 0
        
    def __enter__(self,):
        self.start_time = time.time()
        
    def __exit__(self, *args):
        
        self.total_time = time.time() - self.start_time
        if self.name is not None:
            print('`{0:s}` costs {1:.4f} seconds'.format(
                self.name. self.total_time))
        else:
            print('Costs {:.4f} seconds'.format(self.total_time))
        


