'''
最长回文子串
难度：中等

问题：给定一个字符串 s, 找到其中最长的回文子串。
示例：
Input: s = "babad"
Output: "bab"
'''

def longest_palindrome(s: str) -> str:
    if not s or len(s) == 0:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    
    for i in range(len(s)):
        # 奇数长度的回文，中心是单个字符
        odd_palindrome = expand_around_center(i, i)
        # 偶数长度的回文，中心是两个字符之间
        even_palindrome = expand_around_center(i, i + 1)
        
        # 更新最长的回文子串
        longest = max(longest, odd_palindrome, even_palindrome, key=len)

    return longest

# 获取用户输入
s = input('Input String: ')
print(longest_palindrome(s))


