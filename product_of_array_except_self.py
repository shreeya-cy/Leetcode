class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prodz = 1
        for i in nums:
            if i==0:
                prodz = prod
                prod = 0
            else:
                prod = prod*i
                prodz = prodz*i
        res = []
        for i in nums:
            if i==0:
                res.append(prodz)
            else:
                res.append(prod//i)
        return(res)
