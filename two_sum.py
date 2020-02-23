# 题目描述 leetcode 1
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

'''
class Solution:
    def twoSum1(self, nums, target):
        for num in nums:
            res = target - num
            if res in nums:
                if (nums.count(res) == 1) and (res == num):
                    continue
                else:
                    return [nums.index(num), nums.index(res, nums.index(num)+1)]

    def twoSum2(self, nums, target):
        for i in range(1, len(nums)):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                return [j, i]
                break

    def twoSum3(self, nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind

        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9


solution = Solution()
res1 = solution.twoSum1(nums, target)
res2 = solution.twoSum2(nums, target)
res3 = solution.twoSum3(nums, target)
print(res3)