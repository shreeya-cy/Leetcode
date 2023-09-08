class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for i in s:
            if(i not in d):
                d[i] = 1
            else:
                d[i] = d[i]+1
        for i in t:
            if(i not in d):
                return(False)
            else:
                d[i] = d[i]-1
        for i in d:
            if(d[i]!=0):
                return(False)
        return(True)      
