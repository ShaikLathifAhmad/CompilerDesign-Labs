def leading(symbol, grammar):
    result = set()
    for prod in grammar[symbol]:
        result.add(prod[0])
    return result

def trailing(symbol, grammar):
    result = set()
    for prod in grammar[symbol]:
        result.add(prod[-1])
    return result
