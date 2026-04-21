def predictive_table(grammar, first, follow):
    table = {}

    for A in grammar:
        for prod in grammar[A]:
            for terminal in first(prod[0], grammar):
                table[(A, terminal)] = prod

    return table
