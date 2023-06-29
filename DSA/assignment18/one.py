def merge_intervals(intervals):
    # Sort the intervals based on start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            # If the result array is empty or current interval doesn't overlap,
            # add it directly to the result array
            merged.append(interval)
        else:
            # If the current interval overlaps with the previous one,
            # update the end time of the previous interval
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge_intervals(intervals)
print(merged_intervals)
