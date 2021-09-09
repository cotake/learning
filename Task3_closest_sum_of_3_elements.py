""" Задача: из списка целых чисел NUMS, в том числе и отрицательных
выбрать такие ТРИ, чтобы их сумма была наиболее близкой к TARGET"""
def closest_sum(nums, target):
    current = {}
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            if j == len(nums):
                break
            for k in range(j + 1, len(nums)):
                if k == len(nums):
                    break
                else:
                    current[f'{nums[i]} {nums[j]} {nums[k]}'] = sum([nums[i], nums[j], nums[k]])
    lowest_delta = abs(target - (nums[0] + nums[1] + nums[2]))
    index_target = f'{nums[0]} {nums[1]} {nums[2]}'
    for key in current.keys():
        if abs(target - current[key]) < lowest_delta:
            lowest_delta = abs(target - current[key])
            index_target = key
    print(index_target)
    return current[index_target]


print(closest_sum([1, -5, 6, 4], 5))

