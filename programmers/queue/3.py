def solution(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)  # 여는 괄호는 스택에 추가
        elif char == ')':
            if not stack:       # 스택이 비어 있으면 잘못된 괄호
                return False
            stack.pop()         # 스택에서 여는 괄호 제거

    return not stack  # 스택이 비어 있으면 올바른 괄호
