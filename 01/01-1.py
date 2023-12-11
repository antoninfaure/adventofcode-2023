from utils import load_input, print_result

def find_first_int(string, reverse=False):
    if reverse:
        string = string[::-1]
    for i, char in enumerate(string):
        if char.isdigit():
            return int(char)
    return None


input = load_input()

# For each line, find the first and last integer
total = 0
for line in input:
    
    first_int = find_first_int(line)
    last_int = find_first_int(line, reverse=True)

    # Concatenate the integers and add to result
    calibration_value = int(str(first_int) + str(last_int))
    
    # Add to result
    total += calibration_value

print_result(total)