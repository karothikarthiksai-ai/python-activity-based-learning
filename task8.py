# Campus Event Financial Planning

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per student: "))

total = venue + equipment + catering + transport + certificates

print("\nTotal Event Cost:", total)

remaining = total - sponsorship

if remaining < 0:
    remaining = 0

print("Amount needed after sponsorship:", remaining)

if fee > 0:
    students = int(remaining / fee)

    if students * fee < remaining:
        students += 1

    print("Minimum students needed:", students)

    participants = int(input("Enter actual participants: "))
    contribution = participants * fee

    print("Participant Contributions:", contribution)

    if contribution + sponsorship < total:
        print("Sponsorship shortfall:", total - contribution - sponsorship)
    else:
        print("Event budget covered!")
else:
    print("Registration fee must be greater than zero.")