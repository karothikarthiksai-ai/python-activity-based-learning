appliances = ["Fan", "TV", "Fridge"]
consumption = [
    [2, 3, 2, 3, 2, 3, 2],
    [1, 2, 1, 2, 1, 2, 1],
    [4, 4, 4, 4, 4, 4, 4]
]

limit = 20

for i in range(3):
    total = sum(consumption[i])
    print(appliances[i], "weekly consumption:", total, "units")

    if total > limit:
        print("Consumption exceeds limit!")

for day in range(7):
    daily_total = 0

    for i in range(3):
        daily_total += consumption[i][day]

    print("Day", day + 1, "total:", daily_total, "units")