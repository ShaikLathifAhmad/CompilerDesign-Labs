def data_flow(graph):
    IN = {}
    OUT = {}

    for node in graph:
        IN[node] = set()
        OUT[node] = set()

    return IN, OUT
