def move_zeros(lst):
    non_zeros = [num for num in lst if num != 0]
    zeros = [num for num in lst if num == 0]
    return non_zeros + zeros