# -*- coding: utf-8 -*-


class StringAlgorithm(object):
    def __init__(self):
        pass

    def is_rotation(self, str1, str2):  # 判断两子串是否互为变形词
        if str1 == "" or str2 == "" or len(str1) != len(str2):
            return False
        str_double = str1 + str1
        if str2 in str_double:
            return True
        else:
            return False

    def str_2_int(self, string):  # 将符合规范的数字字符串转为数字
        if string == "":
            return 0
        if len(string) == 1:
            if 48 < ord(string) <= 57:
                return ord(string) - 48
            else:
                return 0
        else:  # 字符串长度大于 1
            num = 0
            if 48 < ord(string[0]) <= 57:
                num = ord(string[0])
                posi = 1
            elif string[0] == "-":
                if string[1] == "0":
                    return 0
                posi = -1
            else:
                return 0
            for i in xrange(1, len(string)):
                if 48 <= ord(string[i]) <= 57:
                    num = num * 10 + ord(string[i])
                else:
                    return 0
            return num * posi

    def replace_str(self, string, from_str, to_str):  # 替换字符串中连续出现的指定字符串,有问题####
        pass

    def get_count_str(self, string):  # 获取字符串的统计字符串
        if string == "":
            return ""
        count = 0
        char = string[0]
        count_str = ""
        for i in xrange(0, len(string)):
            if char != string[i]:
                count_str += char + "_" + str(count) + "_"
                char = string[i]
                count = 1
            else:
                count += 1
        count_str += char + "_" + str(count)
        return count_str

    def is_unique_1(self, str_list):  # 判断字符类型数组中的字符是否均只出现过一次，时间复杂度o(n)
        if str_list == "":
            return False
        i, map = 0, [0]
        while i < 256:
            map.append(0)
            i += 1
        for i in xrange(0, len(str_list)):
            map[ord(str_list[i])] += 1
            if map[ord(str_list[i])] != 1:
                return False
        return True

    def is_unique_2(self, str_list):  # 判断字符类型数组中的字符是否均只出现过一次，空间复杂度o(1)######
        if str_list == "":
            return False
        for i in xrange(0, len(str_list)):
            for j in xrange(i + 1, len(str_list)):
                if str_list[i] == str_list[j]:
                    return False
        return True

    def get_index(self, str_list, str):  # 在有序但包含None的数组中查找字符
        index = -1
        left = 0
        right = len(str_list) - 1
        if str is None:
            return -1
        while left <= right:
            mid = (left + right) / 2
            if str_list[mid] == str:
                index = mid
                right = mid - 1
            elif str_list[mid] == None:
                i = mid - 1
                while 0 < i < mid:
                    if str_list[i] != None:
                        break
                    else:
                        i -= i
                if ord(str_list[i]) == ord(str):
                    index = i
                    right = i - 1
                elif ord(str_list[i]) > ord(str):
                    right = i
                else:
                    left = mid + 1
            else:
                if ord(str_list[mid]) > ord(str):
                    right = mid - 1
                else:
                    left = mid + 1
        return index

    def replace_space(self, str_list):  # 字符串的调整与替换,时间复杂度o(n),空间复杂度o(1)
        num = 1
        for i in xrange(0, len(str_list)):
            if str_list[i] == ' ':
                num += 1
        length = len(str_list) + 2 * num - 2
        i = k = len(str_list)
        while i < length:
            str_list.append('0')
            i += 1
        i -= 1
        for j in xrange(k - 1, -1, -1):
            if str_list[j] == ' ':
                str_list[i] = "0"
                i -= 1
                str_list[i] = "2"
                i -= 1
                str_list[i] = "%"
                i -= 1
            else:
                str_list[i] = str_list[j]
                i -= 1
        return str_list

    def replace_stars(self, str_list):  # 将所有*号移动到数组的左侧
        j = len(str_list) - 1
        for i in xrange(len(str_list) - 1, -1, -1):
            if str_list[i] != '*':
                str_list[j] = str_list[i]
                j -= 1
        for i in xrange(0, j + 1):
            str_list[i] = '*'
        return str_list

    def rotate_word(self, str_list):  # 翻转字符串，将一句英文中的单词全部逆序，单词本身不变#####
        if str_list == []:
            return []

    def reverse_list(self, str_list, start, end):  # 翻转一个数组，逆序存入同样的位置######
        if str_list == [] or start == end:
            return str_list
        if start > end:
            print "WRONG index."
            return str_list
        for i in xrange(0, (end - start) / 2):
            tmp = str_list[end - i]
            str_list[end - i] = str_list[start + i]
            str_list[start + i] = tmp

    def pattern_match(self, str, pattern):  # 字符串的模式匹配，返回匹配到的索引
        index = []
        for _ in xrange(0, len(str)):
            i = _
            j = 0
            while j < len(pattern):
                if i < len(str) and str[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    break
            if j == len(pattern):
                index.append(_)
        return index

    def kmp_pattern_match(self, str, pattern):
        index = []
        j = 0
        for i in xrange(0, len(str)):

            def get_next(pattern, index):  # index 范围为 1 到 len(pattern)，算上 len(pattern)

                def next_index(pattern):  # 返回一个列表，表示对应索引的下一跳索引
                    next_list = [0, 0]
                    for _ in xrange(2, len(pattern)):
                        temp_list = [0]
                        for i in xrange(1, _):
                            if pattern[0:i] == pattern[_ - i:_]:
                                temp_list.append(i)
                        next_list.append(max(temp_list))
                    return next_list

                next_list = next_index(pattern)
                return next_list[index]

            j = get_next(pattern, j)
            while j < len(pattern):
                if i < len(str) and str[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    break
            if j == len(pattern):
                index.append(i - j)
                j = 0
        return index

    def min_distance_1(self, strs, str1, str2):
        '''
        数组中两个字符串的最小距离，这是方法1，时间复杂度 o(n^2)
        :param strs: 给定的数组中存放有多个字符串
        :param str1: 第一个字符串
        :param str2: 第二个字符串
        :return: 如果其中给定的一个字符串不在数组 strs 中，那么返回-1，否则返回两个字符串之间的最小间距
        '''
        if str1 not in strs or str2 not in strs:
            return -1
        if str1 == str2:
            return 0
        dist, min = 1, len(strs)
        pos1, pos2 = 0, len(strs)
        for i in xrange(0, len(strs)):
            if str1 == strs[i]:
                pos1 = i
                for j in xrange(0, len(strs)):
                    if str2 == strs[j]:
                        pos2 = j
                    dist = abs(pos1 - pos2)
                    if dist < min:
                        min = dist
        return min

    def min_distance_2(self, strs, str1, str2):
        '''
        数组中两个字符串的最小距离，这是方法2，如果查询的次数非常多，把每次查询的时间复杂度下降到 o(1)。
        Python 的内置 dict 类型就是哈希表，实现方法也是hash 表，其查询的时间复杂度就是 o(1)。哈希表的构造也分很多种：
        比如，构造 Hash 表，key值是strs中的每一个字符串，value值是一个hash表，里面存放着该字符串到其它字符串的最小距离。
            写成代码就是：hash_table = {"*":{"3":1, "5":1, "10":2, "9":3, "7":2, "1":1}}
        当然这种方法的空间复杂度是 o(n^2)
        :param strs: 给定的数组中存放有多个字符串['*','3','*','5','10','9','7','1','*']
        :param str1: 第一个字符串, '*'
        :param str2: 第二个字符串, '9'
        :return: 如果其中给定的一个字符串不在数组 strs 中，那么返回-1，否则返回两个字符串之间的最小间距
        '''
        if str1 not in strs or str2 not in strs:
            return -1
        if str1 == str2:
            return 0

        def create_hash(strs):  # 创建 Hash 表的过程，其实创建完后就不再更改了，这里为了方便说明就具体写了一下
            strs_set = list(set(strs))
            dist_hash = {}
            for i in xrange(0, len(strs_set)):
                temp = {}
                for j in xrange(0, len(strs_set)):
                    if strs_set[i] != strs_set[j]:
                        dist = self.min_distance_1(strs, strs_set[i], strs_set[j])
                        temp[strs_set[j]] = dist
                dist_hash[strs_set[i]] = temp
            return dist_hash

        return create_hash(strs)[str1][str2]

    def brackets_is_valid_1(self, str):
        '''
        判断括号字符串是不是有效括号字符串，比如："()()"为 True，"(()())"为 True，"())"，"（())"等等均为 False
        方法1：建立一个栈操作,时间复杂度为一遍遍历，但是空间复杂度较高。
        :param str: 括号字符串
        :return: True 或者 False
        '''
        stack = []
        for i in xrange(0, len(str)):
            if str[i] != "(" and str[i] != ")":
                return False
            if str[i] == "(":
                stack.append("(")
            else:
                stack.pop()
        if stack != []:
            return False
        else:
            return True

    def brackets_is_valid_2(self, str):
        '''
        判断括号字符串是不是有效括号字符串，比如："()()"为 True，"(()())"为 True，"())"，"（())"等等均为 False
        方法2：时间复杂度不变，仍是一遍遍历的，但是空间复杂度只有o(1)。
        :param str: 括号字符串
        :return: True 或者 False
        '''
        num1, num2 = 0, 0
        for i in xrange(0, len(str)):
            if str[i] != "(" and str[i] != ")":
                return False
            if str[i] == "(":
                num1 += 1
            else:
                num2 += 1
            if num1 < num2:
                return False
        if num1 == num2:
            return True
        else:
            return False

    def longest_sub_brackets(self, str):
        '''
        给定一个括号字符串 str，返回最长的有效括号字符串
        方法：动态规划求解，做到时间复杂度 o(n)，空间复杂度 o(n)。创建一个与字符串同等长度的数组 dp[]，
            其含义是对应 str[i]结尾的字符串的最长有效子串的长度。然后即可开始求解。
        :param str: 给定的括号字符串
        :return: 最长有效子串
        '''
        print str
        dp = []
        for _ in xrange(0, len(str)):
            dp.append(0)
        for i in xrange(0, len(str)):
            if str[i] == "(":
                dp[i] = 0
            if str[i] == ")":
                if i != 0:
                    pre = i - dp[i - 1] - 1
                    if str[pre] == "(":
                        dp[i] = dp[i - 1] + 2 + dp[pre - 1]
        return max(dp)







str_algo = StringAlgorithm()
# print "is_deformation: ", str_algo. is_deformation("fefdw", "wef")
# print "sum_of_num: ", str_algo.sum_of_num("a12b--2fe.8")
# print "remove_k_zeros: ", str_algo.remove_k_zeros("0000fw300001203h000ui0000re3_0000", 4)
# print "is_rotation: ", str_algo.is_rotation("bhfj", "jbfh")
# print "str_2_int: ", str_algo.str_2_int("-3761aa29"), type(str_algo.str_2_int("376129"))
# print "replace_str: ", str_algo.replace_str()
print "get_count_str: ", str_algo.get_count_str("fffjkk99999022____")
print "get_char_at: ", str_algo.get_char_at(str_algo.get_count_str("fffjkk99999022"), 14)
print "is_unique_1: ", str_algo.is_unique_1("hdslegtr")
print "is_unique_2: ", str_algo.is_unique_2("hdslecvb")
print "get_index: ", str_algo.get_index(['a', None, 'b', None, 'd', 'd', None, 'k', 'm'], 'd')
print "replace_space: ", str_algo.replace_space([' ', 'a', ' ', 'b', ' ', ' ', 'g'])
print "replace_stars: ", str_algo.replace_stars(['*', '3', '*', '5', '9', '1', '*'])

# print "min_distance_1: ", str_algo.min_distance_1(['*','3','*','5','10','9','7','1','*'], '*', '7')
# print "min_distance_2: ", str_algo.min_distance_2(['*','3','*','5','10','9','7','1','*'], '*', '7')
print "brackets_is_valid: ", str_algo.brackets_is_valid_1("(()(())())")
print "brackets_is_valid: ", str_algo.brackets_is_valid_2("(()(())())")
print "longest_sub_brackets", str_algo.longest_sub_brackets("(()(((&))(())")
