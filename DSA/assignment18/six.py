def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for i in range(1, len(points)):
        start = points[i][0]
        if start > end:
            arrows += 1
            end = points[i][1]

    return arrows

# Example usage
points = [[10,16],[2,8],[1,6],[7,12]]
min_arrows = findMinArrowShots(points)
print(min_arrows)
