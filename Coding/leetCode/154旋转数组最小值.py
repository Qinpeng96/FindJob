from typing import List

class Solution:
    #遍历
    def findMin(self, nums: List[int]) -> int:

        arr_len = len(nums)
        for i in range(arr_len-1):
            if nums[i+1]<nums[i]:
                return nums[i+1]
        return nums[0]
    #二分法
    def findMin2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while mid > left and nums[left] >= nums[mid]:
            mid -= 1
        while mid < right and nums[right] <= nums[mid]:
            mid += 1
        ans = min(nums[left], nums[mid])
        return ans

a = Solution()
print(a.findMin([1,3,5]))
