from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = 0
        res_array = []
        for i in range(k):
            max = nums[0]
            index = 0
            for j in range(len(nums)):
                if len(nums) == 1:
                    index = 0
                else:
                    if nums[j] > max:
                        max = nums[j]
                        index = j
            res_array.append(max)
            nums.pop(index)
        return res_array[len(res_array)-1-k]
s = Solution()
print(s.findKthLargest([3,1,2,4],2))