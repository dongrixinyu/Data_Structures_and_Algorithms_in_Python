# -*- coding=utf-8 -*-

import random


class EightQueensPuzzle(object):
    '''
    八皇后问题求解
    代码使用方法：
        eight_q = EightQueensPuzzle(4, 5)
        print "EIGHT QUEEDS PUZZLE:"
        result = eight_q.eight_queens_puzzle()
        for i in result:
            print i
    '''
    def __init__(self, n, char):
        self.n = n  # 棋盘维度
        self.char = char  # 皇后标记字符

    def init_chess_board(self, n):
        '''
        初始化一个棋盘，棋盘规格可以按参数 n 随意选定,一般都讨论八皇后，就选择 8
        :return: 返回棋盘，是一个 8*8 矩阵
        '''
        chess_board = []
        for i in xrange(0, n):
            line = []
            for j in xrange(0, n):
                line.append(0)
            chess_board.append(line)
        return chess_board

    def update_conflict_board(self, conflict_board, position):
        for k in xrange(0, self.n):  # 为行添加 1
            conflict_board[position[0]][k] = 1
        for id in xrange(position[0]+1, self.n):
            conflict_board[id][position[1]] = 1  # 为列添加 1
            if position[0] + position[1] - id >= 0:  # 为左斜添加 1
                conflict_board[id][position[0] + position[1] - id] = 1
            if position[1] - position[0] + id < self.n:  # 为右斜添加 1
                conflict_board[id][position[1] - position[0] + id] = 1

    def queens_conflict(self, conflict_board, position):
        '''
        当前棋盘的状态是 conflict_board, 判定如果在 position 位置给一个皇后的话，会不会出现问题。
        如果有问题则返回 False，如果没有问题返回 True
        '''
        if conflict_board[position[0]][position[1]] != 0:
            return False
        else:
            return True

    def eight_queens_puzzle(self):
        '''
        给出一个八皇后的求解答案。
        :return:返回一个结果并打印.
        '''
        import random
        while True:  # 不停寻找符合条件的八皇后排列
            chess_board = self.init_chess_board(self.n)
            conflict_board = self.init_chess_board(self.n)
            for i in xrange(0, self.n):
                flag = 0
                for cnt in conflict_board[i]:
                    if cnt != 0:
                        flag += 1
                if flag == self.n:  # 如果已经1被填满了，说明这个答案错误
                    break

                while True:
                    pos = [i, random.randint(0, self.n-1)]  # 元组构成皇后的位置
                    if self.queens_conflict(conflict_board, pos):  # 如果没有冲突
                        chess_board[i][pos[1]] = self.char
                        self.update_conflict_board(conflict_board, pos)
                        break
            if self.char in chess_board[self.n-1]:
                return chess_board

