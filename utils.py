import sys

def print_result(result):
    print(f"\u001b[38;5;2mResult: \u001b[0m{result}")
    sys.exit()

def load_input():
    with open('input.txt') as f:
        input = f.readlines()
        return input