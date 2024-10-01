'''
旋转数组： 编写一个函数，将给定的列表向右旋转 k 个位置。
例如，输入列表 [1, 2, 3, 4, 5, 6, 7] 和 k = 3, 
应返回 [5, 6, 7, 1, 2, 3, 4]。
'''
# 这种方式更加高效，因为它是更加底层的操作。
tar_list = [1, 2, 3, 4, 5, 6, 7]
k = 123

def rotate_list(list: list, k: int) -> list:
    # 处理k大于列表长度的情况
    k = k % len(list)
    
    # 使用切片进行旋转
    return list[-k:] + list[:-k]

result = rotate_list(tar_list, k)
print(result)
