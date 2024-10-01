'''
统计单词频率： 编写一个函数，接收一个字符串，返回每个单词的出现次数。
例如，输入 "hello world hello" 应返回 {'hello': 2, 'world': 1}
'''
str = input('Input text: ')

list = str.split()
freq = dict()

for i in list:
    freq[i] = freq.get(i, 0) + 1

print(freq)

