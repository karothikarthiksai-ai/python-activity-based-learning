capacity = 1000
water = 500
threshold = 800
days = 5

for day in range(1, days + 1):
    inflow = int(input("Enter inflow: "))
    outflow = int(input("Enter outflow: "))

    water = water + inflow - outflow

    if water > capacity:
        print("Overflow!")
        water = capacity

    if water < 0:
        print("Water shortage!")
        water = 0

    print("Day", day, "Water level:", water)

    if water >= threshold:
        print("Threshold reached on day", day)
        break

print("Final water level:", water)