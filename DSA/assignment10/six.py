def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return 1

    count1 = tower_of_hanoi(n - 1, source, auxiliary, destination)
    print("move disk", n, "from rod", source, "to rod", destination)
    count2 = tower_of_hanoi(n - 1, auxiliary, destination, source)

    return count1 + 1 + count2

n = int(input("Enter the number of discs: "))
total_moves = tower_of_hanoi(n, 1, 3, 2)
print("Total moves:", total_moves)
