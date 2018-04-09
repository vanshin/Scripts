def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = 0
    for i in nums:
        two = target - i
        new_nums = nums[nums.index(i)+1:]
        n = n + 1
        
        print("new_nums:",new_nums)
        print(n)
        if two in new_nums:
            return [nums.index(i), new_nums.index(two)+n]
def main():
    nums = [3,2,4]
    # nums = [1,3,3,3]
    target = 6
    result = twoSum(nums, target)
    print(result)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
    