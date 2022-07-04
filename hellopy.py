import tkinter.messagebox
from tkinter import *
import Account_file
from tk_field_creator import create_label, create_text, create_entry, create_button

#Close Protocol

def add_closing_protocol(tk_name: Tk):
    def on_closing():
        if tkinter.messagebox.askyesno("Quit", "Do you want to quit?"):
            exit()
    tk_name.protocol("WM_DELETE_WINDOW", on_closing)


# Tks
register_bank = login_bank = deposit_bank = withdraw_bank = homepage_bank = Tk()
tk_list = [register_bank, login_bank, deposit_bank, withdraw_bank, homepage_bank]
for tk_name in tk_list:
    if tk_name != register_bank:
        tk_name.withdraw()
    add_closing_protocol(tk_name)

register_bank.geometry("470x400")
register_bank.title("Register for Bank")

create_text(register_bank, "Register", ("sans serif", 30, "bold"), (0.5, 0.1, CENTER))

fname_label_br = create_label(register_bank, "First Name: ", (0.175, 0.275, CENTER))
fname_input_br = create_entry(register_bank, 40, (0.527, 0.275, CENTER))

lname_label_br = create_label(register_bank, "Last Name: ", (0.175, 0.400, CENTER))
lname_input_br = create_entry(register_bank, 40, (0.527, 0.400, CENTER))
phone_label_br = create_label(register_bank, "Phone: ", (0.175, 0.525, CENTER))
phone_input_br = create_entry(register_bank, 40, (0.527, 0.525, CENTER))

pass_label_br = create_label(register_bank, "Password: ", (0.175, 0.650, CENTER))
pass_input_br = create_entry(register_bank, 40, (0.527, 0.650, CENTER))


def homepage_open(name, phone, password):
    # print(cash_in_bank, " ", name, " ", phone, " ", password)
    login_bank.withdraw()
    register_bank.withdraw()
    homepage_bank.deiconify()
    homepage_bank.geometry("470x400")
    homepage_bank.title("Homepage")
    h_banker_text = "Homepage Bankist"
    h_banker_lb = Label(homepage_bank, text=h_banker_text)
    h_banker_lb.configure(font=("Times New Roman", 30, "bold"))
    h_banker_lb.place(relx=0.5, anchor=CENTER, rely=0.1)

    def on_deposit():
        deposit_bank.deiconify()
        deposit_bank.geometry("470x400")
        deposit_bank.title("Deposit")
        deposit_lb = Label(deposit_bank, text="Cash Deposit: ")
        deposit_lb.place(relx=0.05, anchor=W, rely=0.1)
        deposit_field = Entry(deposit_bank, width=30)
        deposit_field.place(relx=0.5, anchor=CENTER, rely=0.1)

        def deposit_money_btn():
            real_cash_in_bank = Account_file.give_cash_info(name, phone, password)
            u_cash_to_deposit = deposit_field.get()
            my_cash_deposit = int(u_cash_to_deposit)
            deposit_errors = []
            if my_cash_deposit < 0:
                deposit_errors.append("Deposit Cash must be greater than 0")
            if my_cash_deposit > 10000000:
                deposit_errors.append("Deposit Cash must be less than 10 Million (1 Crore)")

            if len(deposit_errors) == 0:
                Account_file.deposit_money(name, phone, password, real_cash_in_bank, my_cash_deposit)
                Account_file.give_cash_info(name, phone, password)
                tkinter.messagebox.showinfo("Success", f"${my_cash_deposit} has been deposited")
                deposit_bank.withdraw()
            else:
                for error in deposit_errors:
                    tkinter.messagebox.showinfo("Warning", {error})

        deposit_btn = Button(deposit_bank, text="Deposit money", command=deposit_money_btn)
        deposit_btn.place(relx=0.5, anchor=CENTER, rely=0.2)

    def on_withdraw():
        withdraw_bank.title("Withdraw")
        withdraw_bank.deiconify()
        withdraw_bank.geometry("470x400")
        withdraw_lb = Label(withdraw_bank, text="Cash Withdraw: ")
        withdraw_lb.place(relx=0.05, anchor=W, rely=0.1)
        withdraw_field = Entry(withdraw_bank, width=30)
        withdraw_field.place(relx=0.5, anchor=CENTER, rely=0.1)

        def withdraw_money_btn():
            real_cash_in_bank = Account_file.give_cash_info(name, phone, password)
            u_cash_to_withdraw = withdraw_field.get()
            my_cash_withdraw = int(u_cash_to_withdraw)
            withdraw_errors = []
            if my_cash_withdraw < 0:
                withdraw_errors.append("Withdraw Cash must be greater than 0")
            if my_cash_withdraw > 10000000:
                withdraw_errors.append("Withdraw Cash must be less than 10 Million (1 Crore)")

            if len(withdraw_errors) == 0:
                Account_file.withdraw_money(name, phone, password, real_cash_in_bank, my_cash_withdraw)
                Account_file.give_cash_info(name, phone, password)
                tkinter.messagebox.showinfo("Success", f"${my_cash_withdraw} has been withdrawn")
                withdraw_bank.withdraw()

        withdraw_btn = Button(withdraw_bank, text="Withdraw money", command=withdraw_money_btn)
        withdraw_btn.place(relx=0.5, anchor=CENTER, rely=0.2)

    def on_account_show():
        account_bank = Tk()
        account_bank.geometry("500x500")
        account_bank.title("Account Bank")
        account_bank.deiconify()
        my_cash_info = Account_file.give_cash_info(name, phone, password)

        name_ai = Label(account_bank, text=f"Name: {name}")
        name_ai.place(relx=0.5, rely=0.3, anchor=CENTER)

        phone_ai = Label(account_bank, text=f"Phone: {phone}")
        phone_ai.place(relx=0.5, rely=0.4, anchor=CENTER)

        password_ai = Label(account_bank, text=f"Password: {password}")
        password_ai.place(relx=0.5, rely=0.5, anchor=CENTER)

        balance_current = Account_file.give_cash_info(name, phone, password)
        balance_ai = Label(account_bank, text=f"Balance: {balance_current}")
        balance_ai.place(relx=0.5, rely=0.6, anchor=CENTER)

        def reload_cash():
            reloaded_balance = Account_file.give_cash_info(name, phone, password)
            balance_ai.configure(text=f"Balance: {reloaded_balance}")

        button_reload_ai = Button(account_bank, text="Reload", command=reload_cash)
        button_reload_ai.place(relx=0.5, rely=0.8, anchor=CENTER)

        def hide_account_bank():
            account_bank.withdraw()

        button_back_ai = Button(account_bank, text="Back", command=hide_account_bank)
        button_back_ai.place(relx=0.5, rely=0.9, anchor=CENTER)

    deposit_button = Button(homepage_bank, text="Deposit", command=on_deposit)
    deposit_button.place(relx=0.5, anchor=CENTER, rely=0.3)

    withdraw_button = Button(homepage_bank, text="Withdraw", command=on_withdraw)
    withdraw_button.place(relx=0.5, anchor=CENTER, rely=0.4)

    acount_setting_button = Button(homepage_bank, text="Account Setting", command=on_account_show)
    acount_setting_button.place(relx=0.5, anchor=CENTER, rely=0.5)

    acount_setting_button = Button(homepage_bank, text="Help", command=homepage_open)
    acount_setting_button.place(relx=0.5, anchor=CENTER, rely=0.6)


def execute_log_in():
    login_bank.deiconify()
    login_bank.geometry("470x400")
    login_bank.title("Log In")
    l_banker_text = "Login Bankist"
    l_banker_lb = Label(login_bank, text=l_banker_text)
    l_banker_lb.configure(font=("Times New Roman", 30, "bold"))
    l_banker_lb.place(relx=0.5, anchor=CENTER, rely=0.1)

    l_fname_label_br = Label(login_bank, text="First Name: ")
    l_fname_label_br.place(x=50, y=100)
    l_fname_input_br = Entry(login_bank, width=40)
    l_fname_input_br.place(x=125, y=100)

    l_l_name_label_br = Label(login_bank, text="Last Name: ")
    l_l_name_label_br.place(x=50, y=150)
    l_l_name_input_br = Entry(login_bank, width=40)
    l_l_name_input_br.place(x=125, y=150)

    l_phone_label_br = Label(login_bank, text="Phone: ")
    l_phone_label_br.place(x=50, y=200)
    l_phone_input_br = Entry(login_bank, width=40)
    l_phone_input_br.place(x=125, y=200)

    l_pass_label_br = Label(login_bank, text="Password: ")
    l_pass_label_br.place(x=50, y=250)
    l_pass_input_br = Entry(login_bank, width=40)
    l_pass_input_br.place(x=125, y=250)

    def on_log():
        l_fname = l_fname_input_br.get().replace(" ", "")
        l_lname = l_l_name_input_br.get().replace(" ", "")
        l_phone = l_phone_input_br.get().replace(" ", "")
        l_password = l_pass_input_br.get().replace(" ", "")

        l_error_list = []

        if l_fname == '':
            l_error_list.append("First Name Empty")
        if l_lname == '':
            l_error_list.append("Last Name Empty")
        if l_phone == '':
            l_error_list.append("Phone Empty")
        if l_password == '':
            l_error_list.append("Password Empty")
        if len(l_password) < 8:
            l_error_list.append("Password is less than 8 characters")

        r_name = l_fname + " " + l_lname

        for error in l_error_list:
            tkinter.messagebox.showwarning("Warning", f"{error}")

        if len(l_error_list) == 0:
            if Account_file.search_contact_exist(r_name, l_phone, l_password):
                tkinter.messagebox.showinfo("Success", f"Welcome {r_name}")
                homepage_open(r_name, l_phone, l_password)

            else:
                tkinter.messagebox.showinfo("Warning", "Contact Not Found")

    l_submit_button_br = Button(login_bank, text="Log In", command=on_log)
    l_submit_button_br.place(x=225, y=300)
    login_bank.mainloop()


def on_bank_reg():
    # Get Values

    fname_in_get = fname_input_br.get()
    lname_in_get = lname_input_br.get()
    phone_in_get = phone_input_br.get()
    pass_in_get = pass_input_br.get()
    # Remove empty spaces rs = removed space
    fname_rs = fname_in_get.replace(" ", "")
    lname_rs = lname_in_get.replace(" ", "")
    phone_rs = phone_in_get.replace(" ", "")
    password_rs = pass_in_get.replace(" ", "")
    error_list = []

    if fname_rs == '':
        error_list.append("First Name Empty")
    if lname_rs == '':
        error_list.append("Last Name Empty")
    if phone_rs == '':
        error_list.append("Phone Empty")
    if password_rs == '':
        error_list.append("Password Empty")
    if len(password_rs) < 8:
        error_list.append("Password is less than 8 characters")

    full_name_rs = f"{fname_rs} {lname_rs}"
    print(full_name_rs)

    if len(error_list) != 0:
        for error in error_list:
            tkinter.messagebox.showwarning(title="Warning", message=f"{error}")
    else:
        if not Account_file.phone_exist(phone_rs):
            Account_file.Account(full_name_rs, phone_rs, pass_in_get)
            tkinter.messagebox.showinfo("Success", "Account Created")
            register_bank.withdraw()
            execute_log_in()
        else:
            tkinter.messagebox.showwarning("Warning", "Existing phone found")

    error_list = []

submit_button_br = create_button(register_bank, "Submit", (0.5, 0.775, CENTER), on_execute_command=on_bank_reg)
go_reg_br = create_button(register_bank, "Already have Account?", (0.5, 0.9, CENTER), on_execute_command=execute_log_in)
register_bank.mainloop()