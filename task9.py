balance = 5000
limit = 2000
transactions = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount!")

    elif choice == 1:
        balance += amount
        transactions += 1
        print("Deposit successful!")

    elif choice == 2:
        if amount > limit:
            print("Withdrawal limit exceeded!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            transactions += 1
            print("Withdrawal successful!")

    else:
        print("Invalid choice!")

print("\n--- Transaction Summary ---")
print("Total transactions:", transactions)
print("Final balance: Rs.", balance)