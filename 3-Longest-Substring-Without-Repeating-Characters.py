class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        chars= set()
        left=0
        max_Len = 0

        for right in range(n):
            if s[right] not in chars:
                chars.add(s[right])
                max_Len = max(max_Len,right-left+1)
            
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left +=1
                chars.add(s[right])
            
        return max_Len
        