class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
            
        top_k = sorted(count.items(), key = lambda x : x[1], reverse=True)[:k]
        result = [item[0] for item in top_k]
        return result


