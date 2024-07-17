def print_lines(filename, start_line, end_line):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(start_line - 1, end_line):
            print(lines[i].strip())



