FIRST = {}
FOLLOW = {}

def first(symbol, grammar):
    if symbol not in grammar:
        return {symbol}

    result = set()
    for prod in grammar[symbol]:
        result |= first(prod[0], grammar)
    return result

def follow(symbol, grammar, start):
    result = set()
    if symbol == start:
        result.add('$')

    for A in grammar:
        for prod in grammar[A]:
            if symbol in prod:
                index = prod.index(symbol)
                if index + 1 < len(prod):
                    result |= first(prod[index+1], grammar)
                else:
                    result |= follow(A, grammar, start)
    return result
