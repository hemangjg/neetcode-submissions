class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_nums = sorted(counts.keys(), key = lambda n: counts[n], reverse = True)
        return sorted_nums[:k]
        
        