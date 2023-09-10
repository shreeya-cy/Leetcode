class Solution:
    def isPalindrome(self, s: str) -> bool:
        ts = ''.join(i for i in s if i.isalnum())
        n = len(ts)
        for i in range(0,n//2):
            if(ts[i].lower() != ts[n-i-1].lower()):
                return(False)
        return(True)
                
