from tkinter import *
import tkinter as tk

# variables
from tkinter import Tk

currentBalance: float = 0
transactionRecord = []
DisplayTransactions = str(transactionRecord).split("[")


# class EntryonlyNumbers was found on https://www.reddit.com/r/learnpython/comments/985umy/limit_user_input_to_only_int_with_tkinter/
# used in order to limit entry input to only numbers (slightly changed as it did not add "."
class EntryonlyNumbers(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ""
        self.var.trace("w", self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isnumeric():
            self.old_value = self.get()
        else:
            self.set(self.old_value)


win = Tk()
win.geometry("400x600")
win.configure(background="black")


def ErrorMessage():
    ErrorWin = Tk()
    ErrorWin.title("Error")
    msg = Label(ErrorWin, text="You are spending more than you have!", fg="white", background="red")
    msg.grid(row=0, column=0)
    closeButton = Button(ErrorWin, text="Okay", command=ErrorWin.destroy)
    closeButton.grid(row=1, column=0)
    ErrorWin.mainloop()


def depositMoney(event):
    global currentBalance
    amount = DepositEntry.get()
    currentBalance += float(amount)
    transactionRecord.append(["added:", amount])
    return currentBalance


def spendMoney(event):
    global currentBalance
    amount = float(SpendEntry.get())
    if amount<currentBalance:
        currentBalance -= float(amount)
        transactionRecord.append(["spent:", amount])
        return currentBalance
    else:
        ErrorMessage()


def clearEntry():  # to delete the entry box to be deleted once submitted
    DepositEntry.delete()
    SpendEntry.delete()
    return


def update_label():  # to get the current balance update as transactions are added
    currentBalanceDisplay.config(text="Current Balance: " + str(currentBalance), bg="yellow")
    currentBalanceDisplay.after(1000, update_label)


def update_Transactions():  # to get the transactions list to update as they get added
    Transactions.config(text="Transactions List:" + str(transactionRecord), fg="white", bg="blue")
    Transactions.after(1000, update_Transactions)


def getReport(event):
    f = open("Spending Report.txt", "w+")
    f.write(str(transactionRecord))


win.title("Expense Tracker")

welcomeMessage = Label(win, text="Welcome to the Expense Tracker", fg="white", background="black")
welcomeMessage.grid(row=0, column=1)

currentBalanceDisplay = Label(win, text="Current Balance: " + str(currentBalance), bg="yellow")
currentBalanceDisplay.grid(row=1, column=1)

DepositLabel = Label(win, text="Deposit Amount:", fg="white", background="black")
DepositLabel.grid(row=2, column=0, sticky=E)

DepositEntry = EntryonlyNumbers(win)
DepositEntry.grid(row=2, column=1)

Deposit = Button(win, text="Deposit", fg="green", bg="white")
Deposit.bind("<Button-1>", depositMoney, clearEntry)
Deposit.grid(row=2, column=2)

SpendLabel = Label(win, text="Amount Spent:", fg="white", background="black")
SpendLabel.grid(row=3, column=0, sticky=E)

SpendEntry = EntryonlyNumbers(win)
SpendEntry.grid(row=3, column=1)

Spend = Button(win, text="Spend", fg="red", bg="white")
Spend.bind("<Button-1>", spendMoney, clearEntry)
Spend.grid(row=3, column=2)

ReportButton = Button(win, text="Report of all Transactions")
ReportButton.bind("<Button-1>", getReport)
ReportButton.grid(row=4, column=1)

Transactions = Label(win, text="Transactions List:" + str(transactionRecord), fg="white", bg="blue")
Transactions.grid(row=5, column=1)
Transactions.update()

# loops
update_Transactions()
update_label()
win.mainloop()
