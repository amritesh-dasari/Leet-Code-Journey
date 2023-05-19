def getConcatenation(nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums