def startsWith( input_list, first_substring):
    result = []
    # Iterate through the list
    for item in input_list:
        # Check if the first part of the item matches the provided first_substring
        if item.startswith(first_substring):
            result.append(item)
    print("HELLO")
    return result


def endWith( input_list, end_substring):
    result = []
    # Iterate through the list
    for item in input_list:
        # Check if the item ends with the provided end_substring
        if item.endswith(end_substring):
            result.append(item)
    return result


def contains(input_list, substring):
    result = []
    # Iterate through the list
    for item in input_list:
        # Iterate through the item string
        for i in range(len(item) - len(substring) + 1):
            # Check if the substring is present at the current position
            if item[i:i + len(substring)] == substring:
                result.append(item)
                break  # Break to avoid duplicates

    return result
