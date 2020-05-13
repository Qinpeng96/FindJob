''' 042 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6 
'''
from typing import List
class Solution:
    def trap01(self, height: List[int]) -> int:
        #暴力法
        ans = 0
        for i in range(1,len(height)-1):
            right_max = 0
            left_max = 0
            for j in range(0,i+1):
                left_max = max(left_max,height[j])
            for j in range(i,len(height)):
                right_max = max(right_max,height[j])
            ans += min(left_max,right_max)-height[i]
        return ans
        
    def trap01(self, height: List[int]) -> int:




