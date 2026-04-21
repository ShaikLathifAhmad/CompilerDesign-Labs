def generate_quadruple(expr):
    tokens = list(expr)
    temp = 1
    result = []

    while len(tokens) > 1:
        op_index = 1
        res = f"T{temp}"
        result.append((tokens[op_index], tokens[op_index-1], tokens[op_index+1], res))
        tokens = [res] + tokens[3:]
        temp += 1

    return result

print(generate_quadruple("a+b*c"))
