class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlength = 0
        for i in nums:
            length = 0
            if (i-1) not in numset:
                while(i+length in numset):
                    length = length+1
            maxlength = max(maxlength,length)
        return(maxlength)
