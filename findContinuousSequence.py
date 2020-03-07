# 题目描述 leetcode 4
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
class Solution:
    def findContinuousSequence(self, target):
        target_list = [number for number in range(1, target + 1)]

        left, right, res = 0, 1, []
        while True:
            if right == target:
                break
            if sum(target_list[left:right]) < target:
                right += 1
            elif sum(target_list[left:right]) > target:
                left += 1
            else:
                res.append(target_list[left:right])
                left += 1
        return res

    def findContinuousSequence1(self, target):
        # 初始化窗口指针和输出列表
        i, j, res = 1,2, []

        # 滑动窗口的右边界不能超过target的中值
        while j <= target//2 + 1:
            # 计算当前窗口内数字之和
            cur_sum = sum(list(range(i,j+1)))
            # 若和小于目标，右指针向右移动，扩大窗口
            if cur_sum < target:
                j += 1
            # 若和大于目标，左指针向右移动，减小窗口
            elif cur_sum > target:
                i += 1
            # 相等就把指针形成的窗口添加进输出列表中
            # 别忘了，这里还要继续扩大寻找下一个可能的窗口哦
            else:
                res.append(list(range(i,j+1)))
                # 这里用j+=1，i+=1，i+=2都可以的
                j += 1
        
        return res

target = 15
solution = Solution()
res = solution.findContinuousSequence(target)
res1 = solution.findContinuousSequence1(target)
print(res)
print(res1)