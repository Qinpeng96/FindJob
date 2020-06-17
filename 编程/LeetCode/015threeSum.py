#本题采用hash表来解决
from typing import List
class Solution:
    def threeSum02(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res
    def threeSum01(self, nums: List[int]) -> List[List[int]]:
        my_hash = {} # key为存在的数字 value为存在数字对应的个数
        key = [] #存放hash表中的key
        nums_len = len(nums)
        res_list = [] #多个List的返回结果

        #构建hash表
        for i in range(nums_len):
            if nums[i] not in key:
                my_hash[nums[i]] = 1;
                key.append(nums[i])
                for j in range (i+1,nums_len):
                    if ( nums[i] ==  nums[j]):
                        my_hash[nums[i]]+=1;
        #①考虑互不相同的元素是否有组成0的可能 调用子函数
        list_len = len(key)
        for i in range(list_len-2):
            for j in range(i+1,list_len):
                res = []
                if -(key[i]+key[j]) in key[j+1:list_len]:
                    res.append(key[i])
                    res.append(key[j])
                    res.append(-(key[i]+key[j]))
                    res_list.append(res)
        if 0 in my_hash and my_hash[0]>=3:
            res_list.append([0,0,0])
        for i in key:
            if my_hash[i] >= 2 and -(2*i) in key and i!=0:#存在两个相同的数字
                res_list.append([i,i,-2*i])
        return res_list
        
    def threeSum03(self, nums: List[int]) -> List[List[int]]:
        res = ([]) 
        num_len = len(nums)
        re_num = []
        for i in range(num_len-1):
            for j in range(i+1,num_len):
                if -nums[i]-nums[j]  in nums[j+1:num_len] :
                    res.append([nums[i],nums[j],-nums[i]-nums[j]])
    

        for i in range(len(res)-1):
            for j in range(i+1,len(res)):
                index1 = len(res)-1-i
                index2 = len(res)-1-j
                if res[index1][0] in res[index2] and res[index1][1] in res[index2] and res[index1][2] in res[index2]:
                    res.remove(res[index1])
        return res

def main():
    s = Solution()
    l = [-1,1,0,2,-1,-4]
    res = s.threeSum03(l)
    print(res)
    #res = s.threeSum([-1,1,0,2,-1,-4,])
main() 