from collections import Counter

def group_by_frequency(arr):
    counter = Counter(arr)
    grouped = {}
    for key, value in counter.items():
        if value not in grouped:
            grouped[value] = [key]
        else:
            grouped[value].append(key)
    return grouped

# Example usage:
elements = [1, 2, 2, 3,3,3 3, 3, 4, 4, 4, 4]
print("Grouped by frequency:", group_by_frequency(elements))
