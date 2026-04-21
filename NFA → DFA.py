def nfa_to_dfa(nfa):
    dfa = {}
    start = frozenset([0])
    unmarked = [start]

    while unmarked:
        state = unmarked.pop()
        dfa[state] = {}

        for symbol in ['a', 'b']:
            new_state = set()
            for s in state:
                if s in nfa and symbol in nfa[s]:
                    new_state.update(nfa[s][symbol])
            new_state = frozenset(new_state)

            if new_state:
                dfa[state][symbol] = new_state
                if new_state not in dfa:
                    unmarked.append(new_state)
    return dfa
    
