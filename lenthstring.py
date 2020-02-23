# 题目描述 leetcode 3
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
class Solution:
    def lengthOfLongestSubstring1(self, s):
        """
        先构建一个列表， 遍历字符串如果字符不在列表中，插入， 并且判断最大值
        如果在列表中，先获取已经存在的位置，切片取后面的数据，然后添加新的值。
        """
        str_list = []
        max = 0
        for s_str in s:
            if s_str not in str_list:
                str_list.append(s_str)
                str_len = len(str_list)
                if str_len > max:
                    max = str_len
            else:
                location = str_list.index(s_str)
                str_list = str_list[location + 1:]
                str_list.append(s_str)
        return max

    def lengthOfLongestSubstring2(self, s):
        """
        滑块窗口， 其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，
        当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
        """
        if not s:return 0
        left = 0
        lookup = set()
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
            print(lookup)
        return max_len
       

str = "pwwkwkew"
solution = Solution()
res1 = solution.lengthOfLongestSubstring1(str)
res2 = solution.lengthOfLongestSubstring2(str)
print(res2)