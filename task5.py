seats = [
    [101, 102, 103],
    [104, 0, 106],
    [107, 102, -1]
]

reserved = [(1, 2)]
valid_rolls = [101, 102, 103, 104, 105, 106, 107, 108]

rolls = []

for i in range(len(seats)):
    for j in range(len(seats[i])):
        roll = seats[i][j]

        if (i, j) in reserved:
            if roll != -1:
                print("Reserved seat error:", i, j)

        elif roll == 0:
            print("Empty seat:", i, j)

        elif roll not in valid_rolls:
            print("Invalid roll number:", roll)

        elif roll in rolls:
            print("Duplicate roll number:", roll)

        else:
            rolls.append(roll)

print("Seating validation completed.")