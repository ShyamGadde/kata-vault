def valid_parentheses(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not bool(stack)