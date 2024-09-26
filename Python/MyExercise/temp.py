'''
最长回文子串
难度：中等

问题：给定一个字符串 s, 找到其中最长的回文子串。
示例：
Input: s = "babad"
Output: "bab"
'''

def longest_palindrome(s:str) -> str:
    if not s or len(s) == 0:
        return ''

    def check_both_sides(left: int, right: int) -> str:
        while left != 0 and right < len(s) and s[left] == s[right]: 
            left -= 1
            right += 1
        return s[left+1:right]
    
    longest = ''

    for i in range(len(s)):
        odd = check_both_sides(i, i)
        even = check_both_sides(i, i+1)
        longest = max(longest, odd, even, key=len)

    return longest

s = input('Input String: ')
print(longest_palindrome(s))