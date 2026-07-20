class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else: 
                seen[i] += 1
        print(seen)
        mx = sorted(seen.items(), key =lambda item: item[1], reverse = True)
        print(mx)
        ls = []
        for i in range(k):
            ls.append(mx[i][0])
        return ls
            