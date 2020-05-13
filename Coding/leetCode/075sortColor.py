from typing import List

class Solution:
    #my solution
    def sortColors01(self, nums: List[int]) -> None:
        zero_nums = 0
        one_nums = 0
        two_nums = 0
        for elem in nums:
            if elem == 0:
                zero_nums += 1
            elif elem == 1:
                one_nums += 1
            else:
                two_nums += 1
        for i in range(len(nums)):
            if i < zero_nums:
                nums[i] = 0
            elif i < one_nums+zero_nums:
                nums[i] = 1
            else:
                nums[i] = 2
    def sortColors02(self, nums: List[int]) -> None:
        left_ptr = 0
        right_ptr = len(nums)-1
        curr_ptr = 0

        while curr_ptr <= right_ptr:
            if nums[curr_ptr] == 0:
                nums[left_ptr],nums[curr_ptr] = nums[curr_ptr],nums[left_ptr]
                curr_ptr += 1
                left_ptr += 1
            elif nums[curr_ptr] == 2:
                nums[curr_ptr],nums[right_ptr] = nums[right_ptr],nums[curr_ptr]
                right_ptr -=1
            else:
                curr_ptr+= 1

a = Solution()
a.sortColors1([1])