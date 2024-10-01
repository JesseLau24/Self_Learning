'''
字符串压缩： 编写一个函数，接收一个字符串并返回一个压缩后的版本，
其中连续重复的字符用字符加上其出现次数来表示。
例如，输入 "aaabbc" 应返回 "a3b2c1"。
'''
def str_compress(s:str) -> str:
    i = 0
    compressed = ''
    while i < len(s) - 2:
        count = 1
        temp = i + 1
        while s[i] == s[temp]:
            count += 1
            temp += 1
        compressed += s[i] + str(count)
        i = temp
    return compressed

string = input('Input String: ')
print(str_compress(string))