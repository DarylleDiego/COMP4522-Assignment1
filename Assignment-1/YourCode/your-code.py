# Skeleton for commit and roll-back exercise
# Darylle, Jon, Jordan, Shargeel
# *** Your Code goes Here ***
import csv
from tabulate import tabulate

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
    balList = myreader(dataPath + 'account-balance.csv')
    accList = myreader(dataPath + 'account.csv')
    cheqList = myreader(dataPath + 'customer.csv')
    savList = myreader(dataPath + 'customer.csv')

    # linking chequing accounts to user
    for c in cheqList:
        key = c[0]
        for a in accList:
            id = a[0]
            if (key == id):
                c.append(a[1])

    # linking chequing balance to accounts
    for c in cheqList:
        num = c[6]
        for b in balList:
            if (b[0] == num):
                c.append(b[1])

    # linking savings accounts to user
    for s in savList:
        key = s[0]
        for a in accList:
            id = a[0]
            if (key == id):
                s.append(a[2])

    # linking saving balance to accounts
    for s in savList:
        num = s[6]
        for b in balList:
            if (b[0] == num):
                s.append(b[1])

    # column headers
    user_column = ["ID", "LastName", "FirstName",
                   "Address", "City", "Age", "Account No.", "Balance"]

    # printing columns
    print('\nChequing Accounts')
    print(tabulate(cheqList, headers=user_column))
    print('\nSavings Accounts')
    print(tabulate(savList, headers=user_column))

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
