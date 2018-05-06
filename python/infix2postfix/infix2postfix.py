def infix2postfix(infix):
    if not infix:
        return

    res = []
    stack = []
    for c in infix:
        if c.isspace():
            continue
        elif c.isalnum():
            res.append(c)
        elif c in ['*', '/']:
            stack.append(c)
        elif c in ['+', '-']:
            if stack and stack[-1] in ['*', '/']:
                while stack and stack[-1] in ['+', '-', '*', '/']:
                    res.append(stack.pop())
                stack.append(c)
            else:
                stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
        else:
            raise TypeError('unrecognised char in infix')

    while stack:
        res.append(stack.pop())

    return ''.join(res)
