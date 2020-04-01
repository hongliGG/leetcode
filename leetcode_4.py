# # 题目描述 leetcode 4

# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

# 你可以假设 nums1 和 nums2 不会同时为空。



class Solution:
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

A = [1, 2]
B = [3, 4]
solution = Solution()
res = solution.findMedianSortedArrays(A, B)
print(res)


# 快排
# def ErFenFa(array,key):
#       print ('列表长度为:',len(array)) #先计算列表的长度
#       mid = int((len(array)-1)/2)
#       print ('列表中间位数为:',mid)
#       min = 0
#       max = len(array)-1
#       print ('即将开始判断，初始化最小数为0，最大数为:%s'%max)
#       print ('-'*10)
#       while True:
#           center = int((min + max) / 2)
#           print ('本次查找的位置:',center)
#           if array[center] > key:
#             #这种说明查找到的数字大于我们要找的数字
#             max = center - 1
#           elif  array[center] < key:
#             #这种说明查找到的数字小于我们要找的数字
#             min = center + 1
#           elif  array[center] == key:
#             return ('找到了,在数组的第%s个位置'%center)
# if __name__ == '__main__':
#   print (ErFenFa([1,2,3,10,34,56,57,78,87],87))