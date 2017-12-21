from itertools import islice

def next_n_lines(file_opened, N):
    return [x.strip() for x in islice(file_opened, N)]

with open("Test.txt", 'r') as ip:
    while True:
        lines_1_to_5 = next_n_lines(ip, 3)
        if lines_1_to_5:
            print(lines_1_to_5)
        else:
            break
