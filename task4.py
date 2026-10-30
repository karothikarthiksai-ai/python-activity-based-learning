capacity = 50
passengers = 0
stops = 4

for i in range(1, stops + 1):
    boarding = int(input("Enter boarding passengers: "))
    alighting = int(input("Enter alighting passengers: "))

    passengers = passengers + boarding - alighting

    if passengers < 0:
        passengers = 0

    print("Stop", i, "Passengers:", passengers)

    if passengers > capacity:
        print("Capacity exceeded!")

print("Final passengers:", passengers)