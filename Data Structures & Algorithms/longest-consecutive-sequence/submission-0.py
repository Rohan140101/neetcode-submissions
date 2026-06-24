class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        n = len(nums)
        maxSeq = 0
        for ele in hashset:
            if ele - 1 in hashset:
                continue
            length = 1
            while True:
                if ele + length in hashset:
                    length += 1
                else:
                    break

            maxSeq = max(maxSeq, length)
        return maxSeq
