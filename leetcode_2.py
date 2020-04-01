# 题目描述 leetcode 2
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，

并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
解题思路：从个位开始，逐位相加
设置变量carry, 他可能有两个取值， 0和1，
最终得数比 list1 和 list2 的长度都要大
最后检查carry的值， 如果>0， 在构建一个值为1的节点
如 500 + 500 = 1000 构建一个值位1的千位
"""
"""
代码解析：
先构建一个值为0的头节点，并把它存为 pHead, 从下一个结点开始存储最终得数的个位 十位 百位...
最后 return pHead.
在 while 循环中, 计算当前位之和sum(l1.val + l2.val + carry), 如果某个链表结点已经没有了,
就不加
sum 的取值范围为[0, 19], 将其对10取整就是进位的 carry 值, 取余就是当前位的值.
然后移动一下指针, 继续向下执行
当l1 l2都遍历完了后, 检查一下carry值, 确定上一位是否进位了

复杂度分析:

时空复杂度都为: O(max(m, n))

while 循环最多执行 max(m, n) 次, 新节点最长为 max(m, n) +1
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        pNode = ListNode(0)
        pHead = pNode
        carry = 0
        while l1 or l2:
            sum = 0 
            if l1:
                sum = sum + l1.val
                l1 = l1.next
            if l2:
                sum = sum + l2.val
                l2 = l2.next
            sum = sum + carry
            carry = int(sum/10)
            pNode.next = ListNode(sum%10)
            pNode = pNode.next
        if carry > 0:
            pNode.next = ListNode(carry)
        return pHead.next




