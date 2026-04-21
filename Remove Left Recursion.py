def remove_left_recursion(grammar):
    new_grammar = {}

    for A in grammar:
        alpha = []
        beta = []

        for prod in grammar[A]:
            if prod.startswith(A):
                alpha.append(prod[len(A):])
            else:
                beta.append(prod)

        if alpha:
            A_dash = A + "'"
            new_grammar[A] = [b + A_dash for b in beta]
            new_grammar[A_dash] = [a + A_dash for a in alpha] + ['ε']
        else:
            new_grammar[A] = grammar[A]

    return new_grammar

grammar = {"A": ["Aa", "b"]}
print(remove_left_recursion(grammar))
