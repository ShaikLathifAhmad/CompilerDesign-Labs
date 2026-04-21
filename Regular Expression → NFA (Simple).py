class NFA:
    def __init__(self):
        self.states = {}
        self.start = 0
        self.end = 1
        self.states[0] = {}
        self.states[1] = {}

def regex_to_nfa(regex):
    nfa = NFA()
    nfa.states[0][regex] = [1]
    return nfa

nfa = regex_to_nfa('a')
print(nfa.states)

