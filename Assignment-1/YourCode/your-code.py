# Skeleton for commit and roll-back exercise
# Darylle, Jon, Jordan, Shargeel
# *** Your Code goes Here ***
from tabulate import tabulate
import csv

dataPath = "Assignment-1/Data-Assignment-1/csv/"


def myreader(filename: str):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        yourList = list(reader)

    return yourList


def mywriter(filename: str, mylist: list):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write multiple rows
        writer.writerows(mylist)

# Your main program


def main():
    # print("First Output:")
    # print("Print Original Contents of Databases")
    # print("Print current status of Log Sub-system\n\n")

    # loading lists
    mainMemory = myreader(dataPath + 'customer.csv')
    accList = myreader(dataPath + 'account.csv')
    balList = myreader(dataPath + 'account-balance.csv')

    # linking accounts to users
    for m in mainMemory:
        key = m[0]
        for a in accList:
            id = a[0]
            if (key == id):
                m.append(a[1])
                m.append(a[2])

    # # linking balances to accounts
    for m in mainMemory:
        cheq = m[6]
        sav = m[7]
        for b in balList:
            if (b[0] == cheq):
                m.insert(7, b[1])
            if (b[0] == sav):
                m.append(b[1])

    # column headers
    user_column = ["ID", "LastName", "FirstName",
                   "Address", "City", "Age", "Chequing Account", "Chequing Balance", "Savings Account", "Savings Balance"]

    # # printing columns
    print("\nBEFORE Transaction")
    print(tabulate(mainMemory, headers=user_column))

    amt = 100000

    # Transaction 1
    emma = '3'
    for m in mainMemory:
        if (m[0] == emma):
            emmaCheq = m[6]
            intChequing = int(m[7])
            intChequing = intChequing - amt
            m[7] = str(intChequing)

    for m in mainMemory:
        if (m[0] == emma):
            emmaSav = m[8]
            intSavings = int(m[9])
            intSavings = intSavings + amt
            m[9] = str(intSavings)

    print("\nAFTER Transaction")
    print(tabulate(mainMemory, headers=user_column))

    print('\n$100,000 withdrawed from', emmaCheq)
    print('$100,000 deposited into', emmaSav, '\n')

    mywriter(dataPath + 'main-memory.csv', mainMemory)

    # Transaction Block 1: Successful
    # print("BLOCK TRANSACTION 1")
    # print("Subtract money from one account.")
    # print("Add money to second one")
    # print("COMMIT all your changes")
    # print("Print Contents of Databases")
    # print("Print current status of Log Sub-system\n\n")

    # Transaction Block 1: Fails!
    # print("BLOCK TRANSACTION 2")
    # print("Subtract money from one account (Same Transaction than before)")
    # print("Failure occurs!!!!!!! ACTION REQUIRED")
    # print("Must either AUTOMATICALLY Roll-back Database to a state of equilibrium (Bonus), OR\nSTOP Operations and show: (a) Log-Status, and (b) Databases Contents.\n")
    # print("\nThe Log Sub-system contents should show the necessary operations needed to fix the situation!")


main()
