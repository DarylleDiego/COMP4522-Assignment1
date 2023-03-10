# Darylle, Jon, Jordan, Shargeel
from tabulate import tabulate
import csv

# variables
dataPath = "Assignment-1/Data-Assignment-1/csv/"
mainMemory = []
log_transactions = []
log = None
transaction_success = ""

# table column headers
cust_columns = ["ID", "LastName", "FirstName",
                "Address", "City", "Age"]
account_columns = ["ID", "Checking Account", "Savings Account"]
accbal_columns = ["Account", "Balance"]
log_columns = ["Transaction ID", "Amount", "Completed",
               "User ID", "Account Number", "Account Type", "Balance Before", "Current Balance"]

# reads .csv files and turns them into/returns an array


def myreader(filename: str):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        yourList = list(reader)
    return yourList

# writes an array to a .csv file


def mywriter(filename: str, mylist: list):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write multiple rows
        writer.writerows(mylist)

# prints the log to a table


def print_log(logList):
    print("Log Transactions")
    print("----------------")
    print(tabulate(logList, headers=log_columns))
    print("\n")

# prints tables


def print_tables():
    print("\n")
    print(tabulate(mainMemory[0], headers=cust_columns))
    print("\n")
    print(tabulate(mainMemory[1], headers=account_columns))
    print("\n")
    print(tabulate(mainMemory[2], headers=accbal_columns))
    print("\n")

# log object


class Log:

    def __init__(self, trans_id, acct_type, amount, completed, userID, acc_num, funds_before, funds_after) -> None:
        self.trans_id = trans_id
        self.amount = amount
        self.completed = completed
        self.userID = userID
        self.acc_num = acc_num
        self.acct_type = acct_type
        self.funds_before = funds_before
        self.funds_after = funds_after

    # returns values of log
    def __dir__(self):
        return [self.trans_id, self.amount, self.completed, self.userID, self.acc_num, self.acct_type, self.funds_before, self.funds_after]


def main():
    global transaction_success

    # loading lists
    cust_csv = myreader(dataPath + 'customer.csv')
    mainMemory.append(cust_csv)
    accList = myreader(dataPath + 'account.csv')
    mainMemory.append(accList)
    balList = myreader(dataPath + 'account-balance.csv')
    mainMemory.append(balList)

    emma_sav_acc = mainMemory[1][2][2]
    emma_cheq_acc = mainMemory[1][2][1]

    # printing main memory before transactions
    print("\nBEFORE Transaction Block 1")
    print_tables()

    # printing log
    print_log(tabulate(log_transactions))

    transaction_amt = 100000

    # BLOCK 1 --------------------------------------------------
    # taking the money out of chequing
    logID = 1
    for m in mainMemory[2]:
        if (m[0] == emma_cheq_acc):
            int_cheq_bal = int(m[1])
            cheq_before_bal = int(m[1])
            int_cheq_bal -= transaction_amt
            m[1] = str(int_cheq_bal)
            # if balance before == balance after, transaction is unsuccessful and prints error message
            if (cheq_before_bal == int_cheq_bal):
                log = Log(logID, "Chequing", -transaction_amt,
                          False, '3', emma_cheq_acc, cheq_before_bal, int_cheq_bal)
                transaction_success = "Transaction failed, action required"
            else:
                log = Log(logID, "Chequing", -transaction_amt,
                          True, '3', emma_cheq_acc, cheq_before_bal, int_cheq_bal)
                transaction_success = "Transaction successful"
            log_transactions.append(log.__dir__())
            logID += 1

    # depositing the money into savings
    for m in mainMemory[2]:
        if (m[0] == emma_sav_acc):
            int_sav_bal = int(m[1])
            sav_before_bal = int(m[1])
            int_sav_bal += transaction_amt
            m[1] = str(int_sav_bal)
            # if balance before == balance after, transaction is unsuccessful and prints error message
            if (sav_before_bal == int_sav_bal):
                log = Log(logID, "Savings", transaction_amt,
                          False, '3', emma_sav_acc, sav_before_bal, int_sav_bal)
                transaction_success = "Transaction failed, action required"
            else:
                log = Log(logID, "Savings", transaction_amt,
                          True, '3', emma_sav_acc, sav_before_bal, int_sav_bal)
                transaction_success = "Transaction successful"
            log_transactions.append(log.__dir__())
            logID += 1

    # Printing contents of main memory after the transaction
    print("\nAFTER Transaction Block 1 / BEFORE Transaction Block 2")
    print_tables()

    # printing log
    print_log(log_transactions)

    # COMMIT changes
    mywriter(dataPath + 'customer.csv', mainMemory[0])
    mywriter(dataPath + 'account.csv', mainMemory[1])
    mywriter(dataPath + 'account-balance.csv', mainMemory[2])

    # BLOCK 2 -------------------------------------------------------
    # taking the money out of chequing
    for m in mainMemory[2]:
        if (m[0] == emma_cheq_acc):
            int_cheq_bal = int(m[1])
            cheq_before_bal = int(m[1])
            int_cheq_bal -= transaction_amt
            m[1] = str(int_cheq_bal)
            # if balance before == balance after, transaction is unsuccessful and prints error message
            if (sav_before_bal == int_sav_bal):
                log = Log(logID, "Chequing", -transaction_amt,
                          False, '3', emma_cheq_acc, cheq_before_bal, int_cheq_bal)
                transaction_success = "Transaction failed, action required"
            else:
                log = Log(logID, "Chequing", -transaction_amt,
                          True, '3', emma_cheq_acc, cheq_before_bal, int_cheq_bal)
                transaction_success = "Transaction successful"
            log_transactions.append(log.__dir__())
            logID += 1

    # depositing the money into savings (failure)
    for m in mainMemory[2]:
        if (m[0] == emma_sav_acc):
            int_sav_bal = int(m[1])
            sav_before_bal = int(m[1])
            #int_sav_bal += transaction_amt
            m[1] = str(int_sav_bal)
            # if balance before == balance after, transaction is unsuccessful and prints error message
            if (sav_before_bal == int_sav_bal):
                log = Log(logID, "Savings", transaction_amt,
                          False, '3', emma_sav_acc, sav_before_bal, int_sav_bal)
                transaction_success = "Transaction failed, action required"
            else:
                log = Log(logID, "Savings", transaction_amt,
                          True, '3', emma_sav_acc, sav_before_bal, int_sav_bal)
                transaction_success = "Transaction successful"

            log_transactions.append(log.__dir__())
            logID += 1

    # Printing contents of main memory after the transaction
    print("\nAFTER Transaction Block 2")
    print_tables()

    # printing log
    print_log(log_transactions)

    # printing transaction success status
    print(transaction_success)
    print("\n")

    # externally save log
    mywriter(dataPath + 'log.csv', log_transactions)

    # COMMIT changes
    mywriter(dataPath + 'customer.csv', mainMemory[0])
    mywriter(dataPath + 'account.csv', mainMemory[1])
    mywriter(dataPath + 'account-balance.csv', mainMemory[2])


main()
