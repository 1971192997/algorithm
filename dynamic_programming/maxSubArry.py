def maxSubArry(nums):
    """
    :param nums: type list[int]
    :return: int
    """
    maxCount = 0
    subCount = nums[0]
    for i in range(len(nums)):
        subCount += nums[i]
        if subCount > maxCount:
            maxCount = subCount
        if subCount < 0:
            subCount = 0
    return maxCount


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArry(nums))
