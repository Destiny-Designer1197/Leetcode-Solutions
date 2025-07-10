class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res =""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1 
            leng =  int(s[i:j])
            word = s[j+1: j+1+leng]
            dec.append(word)
            i = 1+ j +leng
        return dec


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))