from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        arr_len = len(candidates)
        if arr_len == 1:
            if target == candidates[0]:
                return True   
            else:
                return False
        res = []
        for i in range(arr_len):
            if candidates[i] <= target:
                if target%candidates[i]:
                    _res = [candidates[i]]*(target/candidates[i])
                else:
                    _res = []
                    _res.append()
                    


