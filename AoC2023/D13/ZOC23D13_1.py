'''
def problem_13_1():
    Paste_qn_statement
'''

import os

dirname = os.path.dirname(__file__) + "\\"

filename = dirname + "AOC23D13_input.txt"

test = dirname + "AOC23D13_test_1.txt"
test2 = dirname + "AOC23D13_test2.txt"

def process_data(RD):
    # * dump data for processing here

    relevant_data = 0

    return RD #relevant_data

def problem13_1(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")

    # * processing data
    #! swap out with actual var names
    var_name = process_data(Rawdata)
    #* to test if code works, comment out when running input
    print(f"data looks like:\n{var_name}")
    #? Dump solution here

    thing = 0

    return thing

print(problem13_1(test))
