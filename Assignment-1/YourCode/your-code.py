# Skeleton for commit and roll-back exercise
# Darylle, Jon, Jordan, Shargeel
# *** Your Code goes Here ***
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

    balList = myreader(dataPath + 'account-balance.csv')
    accList = myreader(dataPath + 'account.csv')
    cusList = myreader(dataPath + 'customer.csv')

    # print(balList)
    # print(accList)
    # print(cusList)

    for c in cusList:
        if (c[0] == '3'):
            print(c)

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
