class Node:
    def __init__(self, op, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right

def create_dag(expr):
    return Node(expr[1], expr[0], expr[2])
