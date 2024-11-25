# platform - leetcode
#link - https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/
# concept - Sum of Beauty of All Substrings


from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        sum1=0
        for i in range(len(s)):
            count=Counter()
            for j in range(i,len(s)):
                count[s[j]]+=1
                maxi=max(count.values())
                mini=min(count.values())
                sum1=sum1+(maxi-mini)
        return sum1
        