class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = dict()
        for n in nums: 
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        max_operations = 0 
        for n in nums:
            complement = k - n
            if complement in counter: 
                if counter[complement] > 0: 
                    counter[complement] -= 1
                    if counter[n] > 0:
                        counter[n] -= 1
                        max_operations += 1
                    else:
                        counter[complement] += 1

        return max_operations