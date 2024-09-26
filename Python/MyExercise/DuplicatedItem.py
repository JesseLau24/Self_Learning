'''
寻找重复的数字： 编写一个函数，接收一个整数列表，找出其中的重复数字,
并返回一个新的列表。例如，输入 [1, 2, 3, 1, 2, 4] 应返回 [1, 2]。
'''
import time

tar = [34, 76, 2, 3, 54, 45, 5, 34, 72, 11, 19, 82, 20, 93, 
       99, 25, 33, 92, 37, 4, 14, 68, 70, 96, 61, 8, 44, 17, 
       12, 74, 31, 84, 38, 39, 60, 88, 1, 13, 79, 30, 6, 58, 
       85, 64, 27, 66, 23, 77, 48, 69, 10, 36, 73, 26, 53, 65, 
       9, 86, 24, 62, 15, 80, 81, 35, 16, 63, 71, 75, 90, 87, 
       18, 59, 46, 7, 32, 52, 40, 41, 50, 47, 49, 78, 94, 42, 
       55, 56, 57, 95, 100, 91, 97, 98]

def find_duplicated(l:list) -> list:
    dup_l = []
    for i in range(len(l)):
        temp = i + 1
        while temp < len(l):
            if l[i] in dup_l:
                break
            else:
                if l[i] == l[temp]:
                    dup_l.append(l[i])
                    break
                else:
                    temp += 1
    return dup_l

start_time = time.time()

print(find_duplicated(tar))

end_time = time.time()
print(f"Elapsed time: {end_time - start_time} seconds")