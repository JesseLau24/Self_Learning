'''
问题：给定一个整数数组 nums 和一个目标值 target
请你在数组中找出和为目标值的两个整数，并返回它们的下标。
示例：
python
Copy code
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
'''
num = [2, 7, 11, 2, 15, 3, 8, 6, 4, 1, 5]
target = int(input('Target: '))

for i in range(0, len(num)):
    for j in range(i, len(num)):
        if num[i] + num[j] == target:
            print(f'[{i}, {j}]')