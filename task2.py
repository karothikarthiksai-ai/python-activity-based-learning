budget = 1000
total = 0

products = ["Book", "Pen", "Bag"]
prices = [300, 50, 600]
quantities = [2, 3, 1]

for i in range(3):
    cost = prices[i] * quantities[i]

    if quantities[i] >= 2:
        cost = cost * 0.9

    print(products[i], "Cost:", cost)
    total = total + cost

print("Total cost:", total)

if total > budget:
    print("Budget exceeded!")

    for i in range(3):
        while quantities[i] > 0 and total > budget:
            total = total - prices[i]
            quantities[i] = quantities[i] - 1
            print("Reduce quantity of", products[i])

print("Final total:", total)
print("Remaining budget:", budget - total)