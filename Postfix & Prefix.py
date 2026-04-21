def infix_to_postfix(expr):
    stack = []
    output = ""
    priority = {'+':1, '-':1, '*':2, '/':2}

    for ch in expr:
        if ch.isalnum():
            output += ch
        elif ch in priority:
            while stack and priority.get(stack[-1],0) >= priority[ch]:
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output

print(infix_to_postfix("a+b*c"))
