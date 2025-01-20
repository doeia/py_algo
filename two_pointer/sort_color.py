def sort_colors(colors):
    # Initialize the start, current, and end pointers
    start, current, end = 0, 0, len(colors) - 1

    # Iterate through the list until the current pointer exceeds the end pointer
    while current <= end:
        if colors[current] == 0:
            # If the current element is 0 (red), swap it with the element at the start pointer
            # This ensures the red element is placed at the beginning of the array
            colors[start], colors[current] = colors[current], colors[start]
            # Move both the start and current pointers one position forward
            current += 1
            start += 1

        elif colors[current] == 1:
            # If the current element is 1 (white), just move the current pointer one position forward
            current += 1

        else:
            # If the current element is 2 (blue), swap it with the element at the end pointer
            # This pushes the blue element to the end of the array
            colors[current], colors[end] = colors[end], colors[current]
            # Move the end pointer one position backward
            end -= 1
    return colors
