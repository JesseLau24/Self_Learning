'''
旋转数组： 编写一个函数，将给定的列表向右旋转 k 个位置。
例如，输入列表 [1, 2, 3, 4, 5, 6, 7] 和 k = 3, 
应返回 [5, 6, 7, 1, 2, 3, 4]。
'''
tar_list = [1, 2, 3, 4, 5, 6, 7]
k = 7

def rotate_list(list: list, k: int) -> list:
    new_list = []
    k = k % len(list)

    for i in range(1, k+1):
        new_list.append(list[-i])

    new_list.reverse()

    for i in range(0, len(list) - k):
        new_list.append(list[i])
    return new_list

result = rotate_list(tar_list, k)
print(result)
