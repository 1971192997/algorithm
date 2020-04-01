def rob(nums):
    """
    :param nums: type list[int]
    :return: int
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    maxCash = [nums[0], max(nums[0], nums[1])]

    for i in range(2, len(nums)):
        maxCash.append(max(nums[i] + maxCash[i - 2], maxCash[i - 1]))
    return maxCash[-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(rob(nums))
