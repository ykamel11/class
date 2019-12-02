from tkinter import *
import tkinter as tk


#variables
from tkinter import Tk

currentBalance: float = 0
transactionRecord = []

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

def depositMoney(event):
    global currentBalance
    amount = DepositEntry.get()
    currentBalance += float(amount)
    transactionRecord.append(["added:", amount])
    return currentBalance

def spendMoney(event):
    global currentBalance
    amount = SpendEntry.get()
    currentBalance -= float(amount)
    transactionRecord.append(["spent:", amount])
    return currentBalance

def clearEntry(): #to delete the entry box to be deleted once submitted
    DepositEntry.delete(0)
    SpendEntry.delete(0)
    return


def update_label(): #to get the current balance update as transactions are added
    currentBalanceDisplay.config(text="Current Balance: "+str(currentBalance), bg="yellow")
    currentBalanceDisplay.after(1000, update_label)

def update_Transactions(): #to get the transactions list to update as they get added
    Transactions.config(text="Transactions List:"+str(transactionRecord), fg="white", bg="blue")
    Transactions.after(1000, update_Transactions)

def getReport(event):
    f = open("Spending Report.txt", "w+")
    f.write(str(transactionRecord))

win.title("Expense Tracker")

welcomeMessage = Label(win, text="Welcome to the Expense Tracker")
welcomeMessage.grid(row=0, column=1)

currentBalanceDisplay = Label(win, text="Current Balance: "+str(currentBalance), bg="yellow")
currentBalanceDisplay.grid(row=1, column=1)

DepositLabel = Label(win, text="Deposit Amount:")
DepositLabel.grid(row=2, column=0, sticky=E)

DepositEntry = EntryonlyNumbers(win)
DepositEntry.grid(row=2, column=1)

Deposit = Button(win, text="Deposit", fg="green", bg="green")
Deposit.bind("<Button-1>", depositMoney, clearEntry)
Deposit.grid(row=2, column=2)

SpendLabel = Label(win, text="Amount Spent:")
SpendLabel.grid(row=3, column=0, sticky=E)

SpendEntry = EntryonlyNumbers(win)
SpendEntry.grid(row=3, column=1)

Spend = Button(win, text="Spend", fg="red", bg="red")
Spend.bind("<Button-1>", spendMoney, clearEntry)
Spend.grid(row=3, column=2)

ReportButton = Button(win, text="Report of all Transactions")
ReportButton.bind("<Button-1>", getReport)
ReportButton.grid(row=4, column=1)

Transactions = Label(win, text="Transactions List:"+str(transactionRecord), fg="white", bg="blue")
Transactions.grid(row=5, column=1)
Transactions.update()


#loops
update_Transactions()
update_label()
win.mainloop()