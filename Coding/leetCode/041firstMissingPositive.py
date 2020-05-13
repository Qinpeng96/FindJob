''' 041 缺失的第一个正整数
题目描述:给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1
'''
from typing import List
class Solution:
    #my way
    def firstMissingPositive01(self, nums: List[int]) -> int:
        nums_list = len(nums)
        if nums_list  == 0:
            return 1
        i = 0
        while( i < nums_list ):
            if ( nums[i] < 0 ):
                nums.pop(i)
                nums_list -= 1
            else:
                i += 1
        array = [x+1 for x in range(nums_list)]
        res = -1;
        for j in array:
            if j not in nums:
                res = j
                return res
            else:
                continue;     
        if res == -1:
            return nums_list+1   
    #others 桶排序
    #参考网址:https://leetcode-cn.com/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
    def firstMissingPositive02(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums_len = len(nums)
            while ( nums[i] < nums_len and nums[i]>0 and nums[i]!=i+1 and ( i >0  and nums[i]!= nums[nums[i]-1]) ):
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i] 
                nums[i] = temp
        for i in range(len(nums)):
            if ( nums[i]!= i+1 ):
                return i+1
        return len(nums)+1     
            
a = Solution()
print(a.firstMissingPositive02([0,2,2,1,1]))