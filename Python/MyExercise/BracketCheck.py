'''
有效的括号： 编写一个函数，检查输入的字符串中括号是否有效。
例如，输入 "()[]{}" 应返回 True, 
而输入 "(]" 应返回 False。
'''

def is_valid_brackets(text: str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    left_brackets = set(bracket_map.values())  # 左括号集合 ('(', '[', '{')
    
    for char in text:
        if char in left_brackets:  # 如果是左括号
            stack.append(char)  # 压入栈中
        elif char in bracket_map:  # 如果是右括号
            top_element = stack.pop() if stack else '#'  # 弹出栈顶元素，或返回占位符
            if bracket_map[char] != top_element:  # 检查栈顶是否匹配
                return False  # 不匹配则返回False
    
    return not stack  # 如果栈为空，说明所有括号匹配正确

# 示例测试
text = "this is a test ("
print(is_valid_brackets(text))  # 输出：False

text = "this is a test (I assume true, but what do I know?)"
print(is_valid_brackets(text))  # 输出：True
