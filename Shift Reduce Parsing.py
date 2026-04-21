def shift_reduce(input_string):
    stack = []
    input_buffer = list(input_string)

    while True:
        print("Stack:", stack, "Input:", input_buffer)

        if ''.join(stack) == "E" and not input_buffer:
            print("Accepted")
            break

        if input_buffer:
            stack.append(input_buffer.pop(0))  # shift

        if ''.join(stack[-3:]) == "id+":
            stack = stack[:-3] + ['E']  # reduce
