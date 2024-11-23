def analyze(numbers):
    result = []
    index = {}
    min = None
    max = None
    for n in numbers:
        index[n] = True
        if not max or n > max:
            max = n
        if not min or n < min:
            min = n
    for n in range(min + 1, max):
        if n not in index:
            result.append(n)
    return result


def analyze_fix(numbers):
    if not numbers:
        return []

    result = []
    index = {}

    # Initialize min and max with the first number
    min = numbers[0]
    max = numbers[0]

    # Determine min and max, and populate the index
    for n in numbers:
        index[n] = True
        if n > max:
            max = n
        if n < min:
            min = n

    # Find missing numbers between min and max
    for n in range(min + 1, max):
        if n not in index:
            result.append(n)

    return result
