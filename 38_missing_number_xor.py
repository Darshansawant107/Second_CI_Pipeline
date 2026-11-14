def find_missing_number(nums, n):
    xor_all = 0
    xor_nums = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for num in nums:
        xor_nums ^= num

    return xor_all ^ xor_nums