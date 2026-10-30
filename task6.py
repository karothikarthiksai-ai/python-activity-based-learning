students = [
    ["Ravi", 85, 75, 80, 90, 12000],
    ["Raju", 90, 80, 85, 95, 10000],
    ["Sita", 78, 70, 75, 80, 8000],
    ["Kiran", 90, 80, 85, 95, 9000]
]

eligible = []

for s in students:
    name = s[0]
    aggregate = s[1]
    subject1 = s[2]
    subject2 = s[3]
    attendance = s[4]
    income = s[5]

    if (aggregate >= 80 and subject1 >= 60 and
        subject2 >= 60 and attendance >= 75 and income <= 10000):
        eligible.append(s)

# Rank by aggregate marks, then attendance
eligible.sort(key=lambda s: (s[1], s[4]), reverse=True)

print("Eligible Students:")

rank = 1

for s in eligible:
    print("Rank:", rank, "Name:", s[0],
          "Marks:", s[1], "Attendance:", s[4])
    rank += 1