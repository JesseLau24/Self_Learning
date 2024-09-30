'''
判断素数： 编写一个函数，接收一个整数，判断该数是否为素数。
如果是素数，返回 True, 否则返回 False。
'''
def isPrime(num: int) -> bool:
    if num <= 1:
        return False  # 1、0 或负数都不是素数
    if num == 2:
        return True  # 2 是唯一的偶数素数
    if num % 2 == 0:
        return False  # 除了 2 以外的偶数都不是素数
    
    # 从 3 开始检查，直到 sqrt(num)，只需检查奇数
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

num = int(input('Input an Intiger: '))
print(isPrime(num))
