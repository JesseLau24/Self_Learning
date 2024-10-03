'''
斐波那契数列： 编写一个函数，接受一个整数 n
返回前 n 个斐波那契数的列表。斐波那契数列的定义为：
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)。
'''
def fibonacci_sequence(n: int) -> list:
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list

n = int(input('n: '))
print(fibonacci_sequence(n))
