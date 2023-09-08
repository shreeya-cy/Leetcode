class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        res = [-1,-1]
        for i,val in enumerate(nums):
            if(target-val in d):
                res[0] = i
                res[1] = d[target-val]
            d[val] = i
        return res
