
from tkinter import *

class loanCal():
 
    def __init__(self):

        window = Tk()
 
        window.title("Bosco's loan calculator system")
 
        window.config(background= "#00ffff")
 
        Label(window, text='Annual Interest Rate', bg='navajowhite', borderwidth=4).grid(row=1, column=1, sticky=W)
 
        Label(window, text='Numbers of Years', bg='navajowhite', borderwidth=4).grid(row=2, column=1, sticky=W)
 
        Label(window, text='Loan Amount', bg='navajowhite', borderwidth=4).grid(row=3, column=1, sticky=W)
 
        Label(window, text='Monthly Payment', bg='navajowhite', borderwidth=4).grid(row=4, column=1, sticky=W)
 
        Label(window, text='Total Payment', bg='navajowhite', borderwidth=4).grid(row=5, column=1, sticky=W)

        self.Int_for_Annual = StringVar()
        Entry(window, textvariable=self.Int_for_Annual, justify=RIGHT).grid(row=1, column=2, sticky=E)
 
        self.yrs = StringVar()
        Entry(window, textvariable=self.yrs, justify=RIGHT).grid(row=2, column=2, sticky=E)
 
        self.amt = StringVar()
        Entry(window, textvariable=self.amt, justify=RIGHT).grid(row=3, column=2, sticky=E)
 
        self.mon_payment = StringVar()
        Label(window, textvariable=self.mon_payment).grid(row=4, column=2, sticky=E)
 
        self.tot_payment = StringVar()
        Label(window, textvariable=self.tot_payment).grid(row=5, column=2, sticky=E)
 

        computation = Button(window, text='Compute Loan', command=self.Payment_Computation).grid(row=6, column=2, sticky=E)
 
        window.mainloop()

    def Payment_Computation(self):
        month = self.Getting_Payment_in_Monthly(
        float(self.amt.get()),
        float(self.Int_for_Annual.get()) / 1200,
        int(self.yrs.get()))
 
        self.mon_payment.set(format(month, '10.2f'))
 
        tot = float(self.mon_payment.get()) * 12 * int(self.yrs.get())
 
        self.tot_payment.set(format(tot, '10.2f'))
 
    def Getting_Payment_in_Monthly(self, Amount_Loan, mon_rate_interest, no_of_yrs):

        month = Amount_Loan * mon_rate_interest / (1- 1 / (1 + mon_rate_interest) ** (no_of_yrs * 12))
        return month;
 
 
loanCal()