# Skeleton for commit and roll-back exercise
# Darylle, Jon, Jordan, Shargeel
# *** Your Code goes Here ***
from tabulate import tabulate
import csv

dataPath = "Assignment-1/Data-Assignment-1/csv/"
mainMemory = []
log_transactions = []

# column headers
cust_columns = ["ID", "LastName", "FirstName",
                "Address", "City", "Age"]
account_columns = ["ID", "Checking Account", "Savings Account"]
accbal_columns = ["Account", "Balance"]


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


def print_log():
    # Printing log contents
    print("Transaction Log System")
    print('----------------------')
    if (len(log_transactions) != 0):
        for l in log_transactions:
            print(l)
    else:
        print("No transaction logs present")
    print("\n")


def print_tables():
    print("\n")
    print(tabulate(mainMemory[0], headers=cust_columns))
    print("\n")
    print(tabulate(mainMemory[1], headers=account_columns))
    print("\n")
    print(tabulate(mainMemory[2], headers=accbal_columns))
    print("\n")


# Your main program

def main():
    # print("First Output)
    # print("Print Original Contents of Databases")
    # print("Print current status of Log Sub-system\n\n")

    # loading lists
    cust_csv = myreader(dataPath + 'customer.csv')
    mainMemory.append(cust_csv)
    accList = myreader(dataPath + 'account.csv')
    mainMemory.append(accList)
    balList = myreader(dataPath + 'account-balance.csv')
    mainMemory.append(balList)

    # all these variables are hard coded. Can make loops and find them iteratively if we need to.
    emma_id = mainMemory[0][2][0]
    emma_sav_acc = mainMemory[1][2][2]
    emma_cheq_acc = mainMemory[1][2][1]
    emma_init_sav_bal = mainMemory[2][9][1]
    emma_init_cheq_bal = mainMemory[2][4][1]

    # printing main memory before transactions
    print("\nBEFORE Transaction")
    print_tables()

    # printing log
    print_log()

    transaction_amt = 100000

    # taking the money out of chequing
    logID = 1
    for m in mainMemory[2]:
        if (m[0] == emma_cheq_acc):
            int_cheq_bal = int(m[1])
            int_cheq_bal -= transaction_amt
            m[1] = str(int_cheq_bal)
            log_transactions.append(
                str(logID) + ": Subtracted $" + str(transaction_amt) + " from chequing account " + emma_cheq_acc)
            logID += logID

    # depositing the money into savings
    for m in mainMemory[2]:
        if (m[0] == emma_sav_acc):
            int_sav_bal = int(m[1])
            int_sav_bal += transaction_amt
            m[1] = str(int_sav_bal)
            log_transactions.append(
                str(logID) + ": Added $" + str(transaction_amt) + " to savings account " + emma_sav_acc)
            logID += logID

    # Printing contents of main memory after the transaction
    print("\nAFTER Transaction")
    print_tables()

    # printing log
    print_log()

    # COMMIT changes
    mywriter(dataPath + 'customer.csv', mainMemory[0])
    mywriter(dataPath + 'account.csv', mainMemory[1])
    mywriter(dataPath + 'account-balance.csv', mainMemory[2])

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

    # transaction block 2


main()
