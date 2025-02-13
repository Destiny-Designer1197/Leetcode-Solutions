class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()

        for i in emails:
            l, d = i.split('@')
            tmp = ""

            for c in l:
                if c == "." : continue
                elif c == "+" : break
                else : tmp += c
            res.add(tmp+"@"+d)

        return len(res)
            
           


            

           
            



                
        