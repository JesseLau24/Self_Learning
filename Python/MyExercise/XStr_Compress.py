'''
字符串压缩： 编写一个函数，接收一个字符串并返回一个压缩后的版本，
其中连续重复的字符用字符加上其出现次数来表示。
例如，输入 "aaabbc" 应返回 "a3b2c1"。
'''
def str_compress(s: str) -> str:
    if not s:  # 如果字符串为空，直接返回空字符串
        return ''
    
    compressed = ''
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        compressed += s[i] + str(count)
        i += 1

    return compressed

# 测试
string = input('Input String: ')
print(str_compress(string))
