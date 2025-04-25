class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        for i in range(len(s)):
            # print(i)
            seen =  set()
            for j in range(i,len(s)):
                # print(j)
                if s[j] in seen:
                    break
                seen.add(s[j])
                # print(len(s))
                max_len = max(max_len,j-i+1)
        return max_len
