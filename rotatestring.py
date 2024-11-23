# platform - leetcode
#link -https://leetcode.com/problems/rotate-string/
# concept - rotate-string


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False 
        if goal in (s+s):
            return True
        else:
            return  False
