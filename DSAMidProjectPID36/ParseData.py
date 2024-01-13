import re
def extract_integers_from_list(input_list):
    integers = []

    for item in input_list:
        if isinstance(item, str):
            # Use regular expression to find all integers in the string
            numbers = re.findall(r'\d+', item)

            # Convert the found strings to actual integers and add them to the result list
            integers.extend([int(number) for number in numbers])

    return integers