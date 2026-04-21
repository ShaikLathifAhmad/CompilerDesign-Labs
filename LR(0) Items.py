def closure(items, grammar):
    closure_set = set(items)

    while True:
        new_items = set()
        for item in closure_set:
            dot_pos = item.find('.')
            if dot_pos + 1 < len(item):
                symbol = item[dot_pos+1]
                if symbol in grammar:
                    for prod in grammar[symbol]:
                        new_items.add(symbol + "->." + prod)
        if new_items.issubset(closure_set):
            break
        closure_set |= new_items

    return closure_set
