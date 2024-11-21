# platform - leetcode
#link - https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
# concept -  Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        count=0
        for i in s:
            if i=='(':
                count+=1
                maxi=max(count,maxi)
            elif i==')':
                count-=1
        return maxi

        