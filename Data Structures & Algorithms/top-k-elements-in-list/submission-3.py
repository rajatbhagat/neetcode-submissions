class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            hashmap[val] = (hashmap.get(val, (0, val))[0] + 1, val)
        vals = list(hashmap.values())
        print(vals)
        vals.sort(key=lambda x: x[0], reverse=True)
        i = 0
        res = []
        while i < k:
            res.append(vals[i][1])
            i += 1
        return res
            